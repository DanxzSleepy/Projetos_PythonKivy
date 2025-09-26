```sql
-- Criação do Banco de Dados da Biblioteca
CREATE DATABASE IF NOT EXISTS biblioteca_municipal;
USE biblioteca_municipal;

-- Tabela de Autores
CREATE TABLE autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    nacionalidade VARCHAR(50),
    data_nascimento DATE,
    biografia TEXT,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Editoras
CREATE TABLE editoras (
    id_editora INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cidade VARCHAR(50),
    telefone VARCHAR(20),
    email VARCHAR(100),
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabela de Categorias
CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao TEXT,
    cor_tag VARCHAR(7) DEFAULT '#3498db'
);

-- Tabela Principal de Livros
CREATE TABLE livros (
    id_livro INT AUTO_INCREMENT PRIMARY KEY,
    isbn VARCHAR(20) UNIQUE,
    titulo VARCHAR(200) NOT NULL,
    id_autor INT NOT NULL,
    id_editora INT NOT NULL,
    id_categoria INT NOT NULL,
    ano_publicacao YEAR,
    edicao VARCHAR(10),
    numero_paginas INT,
    sinopse TEXT,
    idioma VARCHAR(30) DEFAULT 'Português',
    quantidade_total INT DEFAULT 1,
    quantidade_disponivel INT DEFAULT 1,
    localizacao_prateleira VARCHAR(20),
    data_aquisicao DATE,
    valor_aquisicao DECIMAL(10,2),
    status ENUM('disponivel', 'emprestado', 'manutencao', 'descartado') DEFAULT 'disponivel',
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor),
    FOREIGN KEY (id_editora) REFERENCES editoras(id_editora),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    
    INDEX idx_titulo (titulo),
    INDEX idx_autor (id_autor),
    INDEX idx_categoria (id_categoria),
    INDEX idx_status (status)
);

-- Tabela de Usuários da Biblioteca
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    data_nascimento DATE,
    endereco TEXT,
    tipo_usuario ENUM('estudante', 'professor', 'comunidade', 'funcionario') DEFAULT 'comunidade',
    status ENUM('ativo', 'inativo', 'suspenso') DEFAULT 'ativo',
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_validade DATE,
    
    INDEX idx_cpf (cpf),
    INDEX idx_status (status)
);

-- Tabela de Empréstimos
CREATE TABLE emprestimos (
    id_emprestimo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_livro INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    data_devolucao_prevista DATE NOT NULL,
    data_devolucao_real DATE,
    status ENUM('ativo', 'devolvido', 'atrasado', 'renovado') DEFAULT 'ativo',
    multa DECIMAL(8,2) DEFAULT 0.00,
    observacoes TEXT,
    funcionario_responsavel VARCHAR(100),
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_livro) REFERENCES livros(id_livro),
    
    INDEX idx_usuario (id_usuario),
    INDEX idx_data_emprestimo (data_emprestimo),
    INDEX idx_status (status)
);

-- Tabela de Reservas
CREATE TABLE reservas (
    id_reserva INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_livro INT NOT NULL,
    data_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_prevista_disponibilidade DATE,
    status ENUM('ativa', 'cancelada', 'concluida') DEFAULT 'ativa',
    prioridade INT DEFAULT 1,
    
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_livro) REFERENCES livros(id_livro),
    
    UNIQUE KEY unique_reserva_ativa (id_usuario, id_livro, status),
    INDEX idx_data_reserva (data_reserva)
);

-- Tabela de Histórico de Ações
CREATE TABLE historico_acoes (
    id_historico INT AUTO_INCREMENT PRIMARY KEY,
    tabela_afetada VARCHAR(50) NOT NULL,
    id_registro INT NOT NULL,
    acao ENUM('INSERT', 'UPDATE', 'DELETE') NOT NULL,
    dados_anteriores JSON,
    dados_novos JSON,
    usuario_responsavel VARCHAR(100),
    data_acao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    INDEX idx_tabela_afetada (tabela_afetada),
    INDEX idx_data_acao (data_acao)
);

-- Tabela de Configurações do Sistema
CREATE TABLE configuracoes (
    id_config INT AUTO_INCREMENT PRIMARY KEY,
    chave VARCHAR(50) UNIQUE NOT NULL,
    valor TEXT NOT NULL,
    descricao TEXT,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Inserção de configurações padrão
INSERT INTO configuracoes (chave, valor, descricao) VALUES
('dias_emprestimo_padrao', '15', 'Duração padrão do empréstimo em dias'),
('limite_renovacoes', '2', 'Número máximo de renovações permitidas'),
('valor_multa_dia', '1.00', 'Valor da multa por dia de atraso'),
('limite_emprestimos_usuario', '5', 'Número máximo de livros por usuário'),
('email_notificacoes', 'biblioteca@municipio.gov.br', 'E-mail para notificações');

-- Views para relatórios
CREATE VIEW view_estoque_livros AS
SELECT 
    l.id_livro,
    l.titulo,
    a.nome as autor,
    c.nome as categoria,
    l.quantidade_total,
    l.quantidade_disponivel,
    (l.quantidade_total - l.quantidade_disponivel) as quantidade_emprestada,
    ROUND((l.quantidade_disponivel / l.quantidade_total) * 100, 2) as percentual_disponivel
FROM livros l
JOIN autores a ON l.id_autor = a.id_autor
JOIN categorias c ON l.id_categoria = c.id_categoria;

CREATE VIEW view_emprestimos_ativos AS
SELECT 
    e.id_emprestimo,
    u.nome as usuario,
    l.titulo as livro,
    e.data_emprestimo,
    e.data_devolucao_prevista,
    DATEDIFF(CURDATE(), e.data_devolucao_prevista) as dias_atraso,
    e.multa
FROM emprestimos e
JOIN usuarios u ON e.id_usuario = u.id_usuario
JOIN livros l ON e.id_livro = l.id_livro
WHERE e.status = 'ativo';

-- Stored Procedures
DELIMITER //

CREATE PROCEDURE sp_realizar_emprestimo(
    IN p_id_usuario INT,
    IN p_id_livro INT,
    IN p_funcionario VARCHAR(100)
)
BEGIN
    DECLARE v_quantidade_disponivel INT;
    DECLARE v_limite_emprestimos INT;
    DECLARE v_emprestimos_ativos INT;
    
    -- Verifica se há exemplares disponíveis
    SELECT quantidade_disponivel INTO v_quantidade_disponivel
    FROM livros WHERE id_livro = p_id_livro;
    
    -- Verifica limite de empréstimos do usuário
    SELECT valor INTO v_limite_emprestimos
    FROM configuracoes WHERE chave = 'limite_emprestimos_usuario';
    
    SELECT COUNT(*) INTO v_emprestimos_ativos
    FROM emprestimos 
    WHERE id_usuario = p_id_usuario AND status = 'ativo';
    
    IF v_quantidade_disponivel > 0 AND v_emprestimos_ativos < v_limite_emprestimos THEN
        -- Realiza o empréstimo
        INSERT INTO emprestimos (id_usuario, id_livro, data_emprestimo, data_devolucao_prevista, funcionario_responsavel)
        VALUES (p_id_usuario, p_id_livro, CURDATE(), 
                DATE_ADD(CURDATE(), INTERVAL (SELECT valor FROM configuracoes WHERE chave = 'dias_emprestimo_padrao') DAY),
                p_funcionario);
        
        -- Atualiza quantidade disponível
        UPDATE livros 
        SET quantidade_disponivel = quantidade_disponivel - 1
        WHERE id_livro = p_id_livro;
        
        SELECT 'SUCESSO' as resultado, 'Empréstimo realizado com sucesso' as mensagem;
    ELSE
        SELECT 'ERRO' as resultado, 
               CASE 
                   WHEN v_quantidade_disponivel = 0 THEN 'Livro não disponível'
                   ELSE 'Usuário atingiu limite de empréstimos'
               END as mensagem;
    END IF;
END //

DELIMITER ;
```