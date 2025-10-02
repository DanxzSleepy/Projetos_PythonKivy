# UC 09 - 🧠 Atividade de Programação Web - Mini CRUD com JSON e localStorage

## 🔍 Pesquisa Inicial

### O que é JSON?

JSON (JavaScript Object Notation) é um formato de texto leve e independente de linguagem para armazenamento e troca de dados. É fácil de ler e escrever para humanos e fácil de analisar e gerar para máquinas.

### Para que ele é utilizado no desenvolvimento de sistemas?

- **Troca de dados**: Comunicação entre cliente e servidor em aplicações web
- **Configuração**: Armazenamento de configurações de aplicativos
- **Armazenamento de dados**: Persistência de informações em formato estruturado
- **APIs**: Formato padrão para resposta de APIs REST
- **Serialização**: Converter objetos em strings para transmissão ou armazenamento

### Qual a diferença entre JSON e um array/objeto do JavaScript?

| Característica | JSON | Objeto JavaScript |
|----------------|------|-------------------|
| Tipo | String (formato de texto) | Estrutura de dados em memória |
| Função | Intercâmbio de dados | Manipulação de dados em tempo de execução |
| Métodos | Requer parsing (`JSON.parse`) | Acesso direto às propriedades |
| Tipos suportados | String, número, boolean, array, objeto, null | Todos os tipos + funções, undefined, símbolos |
| Sintaxe | Aspas duplas obrigatórias | Aspas simples ou duplas |

### Cite um exemplo simples de dado em formato JSON

```json
{
  "nome": "João Silva",
  "idade": 30,
  "casado": true,
  "habilidades": ["JavaScript", "HTML", "CSS"],
  "endereco": {
    "rua": "Av. Paulista",
    "numero": 1000,
    "cidade": "São Paulo"
  }
}
```

## 🎯 Objetivos da Atividade

1. Desenvolver lógica de cadastro, listagem e exclusão de itens
2. Reforçar a manipulação do DOM e do localStorage
3. Entender como o JSON auxilia na persistência de dados no navegador

## 📝 Atividade Prática: Mini CRUD de Tarefas

### ✅ Funcionalidades Implementadas

- **Adicionar item**: Campo de texto com botão "Adicionar" que insere novas tarefas na lista
- **Listar itens**: Exibição dinâmica das tarefas cadastradas
- **Editar item**: Permite modificar o texto de uma tarefa existente
- **Excluir item**: Botão para remover tarefas da lista e do localStorage
- **Salvar no localStorage**: Persistência dos dados utilizando JSON.stringify e JSON.parse
- **Validações**: 
  - Impedir cadastro de itens vazios
  - Impedir cadastro de itens duplicados
- **Feedback visual**: Mensagens temporárias de sucesso e erro

### 🧩 Funcionalidades Adicionais

- Edição inline de tarefas
- Validação de dados (vazio e duplicados)
- Feedback visual com mensagens temporárias
- Design responsivo
- Tecla Enter para adicionar tarefas

## 💡 Estrutura do Código

### Funções principais:

- `adicionarItem()`: Adiciona nova tarefa à lista
- `listarItens()`: Renderiza as tarefas na interface
- `removerItem(index)`: Remove uma tarefa específica
- `editarItem(index)`: Permite editar uma tarefa existente
- `salvarLocalStorage()`: Salva os dados no localStorage usando JSON
- `carregarLocalStorage()`: Carrega os dados do localStorage usando JSON

### Uso de JSON e localStorage:

- `JSON.stringify()`: Converte array de tarefas em string para salvar no localStorage
- `JSON.parse()`: Converte string do localStorage de volta para array de tarefas

## 📤 Entrega da Atividade

✅ Pesquisa inicial respondida (este documento)
✅ Código fonte disponível no repositório
✅ Funcionalidades implementadas conforme solicitado