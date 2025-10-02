# Mini CRUD com JSON e localStorage

Este projeto é uma aplicação web simples de lista de tarefas (CRUD) que utiliza JSON e localStorage para persistência de dados no navegador.

## 📋 Funcionalidades

- Adicionar novas tarefas
- Listar tarefas existentes
- Editar tarefas
- Excluir tarefas
- Persistência de dados com localStorage
- Validação de dados (itens vazios e duplicados)
- Feedback visual para o usuário

## 🛠️ Tecnologias Utilizadas

- HTML5
- CSS3
- JavaScript (ES6+)
- JSON
- localStorage

## 🚀 Como Executar

1. Clone este repositório:
   ```
   git clone https://github.com/DanxzSleepy/Projetos_PythonKivy ou <url-do-repositorio>
   ```

2. Navegue até o diretório do projeto

3. Abra o arquivo `index.html` no seu navegador ou inicie um servidor local:
   ```
   python -m http.server 8000
   ```

4. Acesse `http://localhost:8000` no seu navegador

## 📁 Estrutura do Projeto

```
.
├── index.html          # Estrutura principal da aplicação
├── style.css           # Estilos da aplicação
├── script.js           # Lógica da aplicação (CRUD)
└── documentacao.md     # Documentação da atividade
```

## 🎯 Detalhes da Implementação

### Classes e Funções Principais

- `TaskManager`: Classe principal que gerencia todas as operações do CRUD
- `addTask()`: Adiciona uma nova tarefa
- `deleteTask()`: Remove uma tarefa pelo ID
- `editTask()`: Permite editar uma tarefa existente
- `renderTaskList()`: Atualiza a interface com a lista de tarefas
- `saveToLocalStorage()`: Salva os dados no localStorage usando JSON
- `loadFromLocalStorage()`: Carrega os dados do localStorage usando JSON

### Uso de JSON e localStorage

- `JSON.stringify()`: Converte o array de tarefas em uma string para armazenar no localStorage
- `JSON.parse()`: Converte a string do localStorage de volta para um array de tarefas
- `localStorage.setItem()`: Armazena os dados no navegador
- `localStorage.getItem()`: Recupera os dados do navegador

## 📝 Documentação

A documentação completa da atividade está disponível no arquivo [UC09-Atividade_de_Programação_Web_Documentacao-Mini_CRUD_com_JSON_e_localStorage.md](UC09-Atividade_de_Programação_Web_Documentacao-Mini_CRUD_com_JSON_e_localStorage.md).

