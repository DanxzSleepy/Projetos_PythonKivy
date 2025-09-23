```sql
-- Arquivo: sistema_biblioteca_caotico.sql
-- DESASTRE TOTAL - Sistema anterior usando uma única tabela gigante

CREATE DATABASE IF NOT EXISTS biblioteca_desorganizada;
USE biblioteca_desorganizada;

-- TABELA MONSTRUOSA - TUDO JUNTO E MISTURADO 
CREATE TABLE tudo_junto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Dados do Livro (mas repetidos várias vezes)
    titulo_livro VARCHAR(200),
    autor_livro VARCHAR(100),
    editora_livro VARCHAR(100),
    ano_livro VARCHAR(10), -- VARCHAR porque às vezes vem "2001-2002"
    categoria_livro VARCHAR(50),
    
    -- Dados do Usuário (repetidos pra cada livro)
    nome_usuario VARCHAR(100),
    cpf_usuario VARCHAR(20), -- Formatos variados: 123.456.789-00, 12345678900, etc.
    telefone_usuario VARCHAR(30),
    email_usuario VARCHAR(100),
    
    -- Dados de Empréstimo (mas sem controle)
    data_emprestimo VARCHAR(20), -- "15/03/2023", "2023-03-15", "15-mar-2023"
    data_devolucao VARCHAR(20),
    situacao VARCHAR(50), -- "emprestado", "devolvido", "atrasado", "perdido"
    
    -- Campos "genéricos" que eram usados para tudo
    observacoes_gerais TEXT, -- Aqui ia TUDO: "livro rasgado", "usuário suspenso", etc.
    campo_extra1 VARCHAR(100), -- Usado pra coisas aleatórias
    campo_extra2 VARCHAR(100),
    campo_extra3 VARCHAR(100),
    
    -- Sem datas de controle
    data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--  INSERÇÕES DESORGANIZADAS - CADA UM FAZIA DE UM JEITO 

-- Livro 1 - Emprestado
INSERT INTO tudo_junto (titulo_livro, autor_livro, editora_livro, ano_livro, categoria_livro, 
                       nome_usuario, cpf_usuario, data_emprestimo, data_devolucao, situacao) 
VALUES ('Dom Casmurro', 'Machado de Assis', 'Editora A', '1899', 'Romance',
        'João Silva', '123.456.789-00', '15/03/2023', '30/03/2023', 'emprestado');

-- Mesmo livro, mesmo usuário, EMPRÉSTIMO DIFERENTE (duplicado)
INSERT INTO tudo_junto (titulo_livro, autor_livro, editora_livro, ano_livro, categoria_livro, 
                       nome_usuario, cpf_usuario, data_emprestimo, data_devolucao, situacao) 
VALUES ('Dom Casmurro', 'Machado de Assis', 'Editora A', '1899', 'Romance',
        'João Silva', '123.456.789-00', '10/04/2023', '25/04/2023', 'devolvido');

-- Livro 2 - Dados inconsistentes
INSERT INTO tudo_junto (titulo_livro, autor_livro, editora_livro, ano_livro, categoria_livro,
                       nome_usuario, cpf_usuario, data_emprestimo, data_devolucao, situacao,
                       observacoes_gerais) 
VALUES ('O Cortiço', 'Aluísio Azevedo', 'Editora B', '1890', 'Romance, Naturalismo', -- Categoria múltipla
        'Maria Santos', '98765432100', '2023-03-20', '2023-04-04', 'atrasado',
        'usuário deve multa de R$ 5,00');

--  CONSULTAS PAIA - EXTREMAMENTE COMPLEXAS 

-- Tentativa de saber quantos livros temos (IMPRECISO)
SELECT COUNT(DISTINCT titulo_livro) as total_livros FROM tudo_junto;
-- Resultado: INCORRETO porque livros com títulos ligeiramente diferentes contam separado

-- Tentativa de encontrar livros emprestados (COMPLEXA)
SELECT titulo_livro, nome_usuario, data_emprestimo, data_devolucao 
FROM tudo_junto 
WHERE situacao = 'emprestado' 
   OR situacao = 'atrasado'
   OR (data_devolucao IS NULL AND data_emprestimo IS NOT NULL)
   OR observacoes_gerais LIKE '%emprestado%';
--  Resultado: INCONSISTENTE

-- Tentativa de encontrar usuários com empréstimos ativos
SELECT DISTINCT nome_usuario, cpf_usuario 
FROM tudo_junto 
WHERE situacao IN ('emprestado', 'atrasado')
GROUP BY nome_usuario, cpf_usuario;
--  Problema: CPFs formatados diferente agrupam errado

--  ATUALIZAÇÕES PERIGOSAS 

-- "Devolver" um livro (mas qual registro??)
UPDATE tudo_junto 
SET situacao = 'devolvido', 
    data_devolucao = CURDATE(),
    observacoes_gerais = CONCAT(observacoes_gerais, ' - Devolvido em ', CURDATE())
WHERE titulo_livro = 'Dom Casmurro' 
  AND nome_usuario = 'João Silva'
  AND situacao = 'emprestado';
--  ATUALIZA VÁRIOS REGISTROS! Pode devolver empréstimos antigos também!

--  SEM CONTROLE DE ESTOQUE 
-- Não há como saber quantos exemplares existem realmente
-- Não há como controlar quantos estão disponíveis

--  "RELATÓRIOS" HORRÍVEIS 

-- Relatório de livros mais populares (INCONFIAVÉL)
SELECT titulo_livro, COUNT(*) as total_emprestimos
FROM tudo_junto 
WHERE situacao IN ('devolvido', 'emprestado', 'atrasado')
   OR data_emprestimo IS NOT NULL
GROUP BY titulo_livro
ORDER BY total_emprestimos DESC;
-- 🤡 Resultado: Totalmente distorcido devido a duplicações

-- Tentativa de calcular multas (CAÓTICO)
SELECT nome_usuario, cpf_usuario,
       SUM(
           CASE 
               WHEN situacao = 'atrasado' THEN 5.00
               WHEN observacoes_gerais LIKE '%multa%' THEN 
                   CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(observacoes_gerais, 'R$ ', -1), ',', 1) AS DECIMAL)
               ELSE 0 
           END
       ) as multa_total
FROM tudo_junto
GROUP BY nome_usuario, cpf_usuario;
--  Resultado: Completamente errado

--  PROCEDURES INEXISTENTES - TUDO MANUAL 

-- Empréstimo manual (cada funcionário faz de um jeito)
-- 1. Procurar se o livro existe (consulta complexa)
-- 2. Verificar se está disponível (mais consultas complexas)
-- 3. Inserir novo registro (com todos os dados repetidos)
-- 4. "Torcer" para não duplicar nada

--  TRIGGERS? CONSTRAINTS? ÍNDICES? NADA DISSO KKK

-- Não há chaves estrangeiras
-- Não há unique constraints
-- Não há validação de dados
-- Índices básicos apenas no ID

--  BACKUP PRECÁRIO 
-- Backup manual via phpMyAdmin
-- Sem versionamento
-- Sem teste de restore

--  MIGRAÇÃO DE Dados EXISTENTES (DESASTRE) 

-- Dados vindos de 3 planilhas Excel diferentes:
-- 1. "Acervo Biblioteca.xlsx" - 1.200 registros
-- 2. "Controle Emprestimos 2023.xlsx" - 800 registros  
-- 3. "Usuarios Cadastrados.csv" - 350 registros

-- Script de migração bagunçado:
INSERT INTO tudo_junto (titulo_livro, autor_livro, editora_livro, ano_livro, categoria_livro)
SELECT titulo, autor, editora, ano, categoria FROM acervo_excel;

INSERT INTO tudo_junto (nome_usuario, cpf_usuario, telefone_usuario, email_usuario)
SELECT nome, cpf, telefone, email FROM usuarios_excel;

-- Resultado: 2.350 registros de livros + 350 registros de usuários = CAOS TOTAL
```