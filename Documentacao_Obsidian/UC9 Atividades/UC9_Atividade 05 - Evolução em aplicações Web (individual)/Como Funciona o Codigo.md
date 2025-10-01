# Como Funciona o Código - AvoidNess

## Visão Geral

O projeto AvoidNess é uma evolução de um formulário de cadastro simples para uma versão mais robusta e estilizada. O código foi dividido em duas partes principais:

1. **Código Antes**: Versão inicial do formulário com funcionalidades básicas
2. **Código Depois**: Versão aprimorada com validações avançadas, design moderno e funcionalidades adicionais

## Estrutura de Arquivos

```
Projeto/
├── Codigo Antes/
│   └── indexantes.html          # Versão básica do formulário
├── Codigo Depois/
│   ├── indexdepois.html         # Versão aprimorada do formulário
│   └── AvoidNess.css            # Estilos personalizados
```

## Código Antes - indexantes.html

### Estrutura HTML

```html
<!DOCTYPE html>
<html lang="pt-br">
```

- `<!DOCTYPE html>`: Declara que este é um documento HTML5
- `<html lang="pt-br">`: Define o idioma do documento como português do Brasil

### Cabeçalho (Head)

```html
<head>
    <meta charset="UTF-8">
    <title>Formulário de Cadastro</title>
```

- `<meta charset="UTF-8">`: Define a codificação de caracteres como UTF-8 para suportar caracteres especiais
- `<title>Formulário de Cadastro</title>`: Define o título da página que aparece na aba do navegador

### Estilos CSS Embutidos

```css
<style>
    body {
        font-family: Arial, sans-serif background-color: #ffffff;
        display: flex;
        justify-content: center;
        align-items: center height: 100vh;
    }
```

- `font-family: Arial, sans-serif`: Define a fonte padrão do documento
- `background-color: #ffffff`: Define a cor de fundo como branco
- `display: flex`: Transforma o body em um container flexível
- `justify-content: center`: Centraliza horizontalmente os elementos filhos
- `align-items: center`: Centraliza verticalmente os elementos filhos
- `height: 100vh`: Define a altura como 100% da viewport (altura da tela)

```css
    .card {
        border: 2px solid #000;
        padding: 12px;
        width: 320px;
        box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.2);
    }
```

- `.card`: Classe CSS para estilizar o contêiner do formulário
- `border: 2px solid #000`: Adiciona uma borda preta de 2px
- `padding: 12px`: Adiciona espaçamento interno de 12px
- `width: 320px`: Define a largura fixa de 320px
- `box-shadow`: Adiciona uma sombra ao elemento

### Corpo (Body) e Formulário

```html
<body>
    <div class="card">
        <h2>Cadastro</h2>
        <form id="formCadastro" onsubmit="return validar Formulario()">
```

- `<div class="card">`: Contêiner principal do formulário usando a classe card
- `<h2>Cadastro</h2>`: Título do formulário
- `<form id="formCadastro" onsubmit="return validar Formulario()">`: Formulário com ID e função de validação ao submeter

### Campos do Formulário

```html
<label for="nome">Nome</label>
<input type="text" id="nome" name="nome">
<label for="email">E-mail</label>
<input type="text" id="email" name="email">
<label for="senha">Senha</label>
<input type="password" id="senha" name="senha">
<label for="telefone">Telefone</label>
<input type="email" id="telefone" name="telefone">
<label for="idade">Idade</label>
<input type="email" id="idade" name="idade">
```

- `<label>`: Rótulo para cada campo do formulário
- `<input>`: Campos de entrada de dados
- `type="text"`: Campo para texto genérico
- `type="password"`: Campo para senha (oculta os caracteres)
- `type="email"`: Campo específico para emails (com validação automática)
- `id` e `name`: Identificadores únicos para cada campo

### Botões de Ação

```html
<div class="actions">
    <input type="button" value="Cadastrar" onclick="enviarFormular
io()">
    <button type="button" onclick="clearFields()">Limpar</button>
</div>
```

- `<div class="actions">`: Contêiner para os botões
- `<input type="button">`: Botão de cadastro com evento onclick
- `<button type="button">`: Botão de limpar com evento onclick

### JavaScript

```javascript
<script>
    function validar Formulario() {
        let nome = document.getElementById("nome").value;
        let email = document.getElementById("email").value;
        let senha = document.getElementById("senha").value;
        let telefone = document.getElementById("telefone").value;
        let idade = document.getElementById("idade").value;
        if (nome === || emai
111#
            ===
            "
            || senha === "") {
            alert("Por favor, preencha todos os campos!");
            return false;
        }
        return true;
    }
```

- `function validar Formulario()`: Função para validar o formulário (com erro de digitação no nome)
- `document.getElementById().value`: Obtém o valor dos campos do formulário
- Validação simples: verifica se nome, email ou senha estão vazios
- `alert()`: Exibe mensagem de erro
- `return false`: Impede o envio do formulário se houver erro

```javascript
    function limparFormulario() {
    }
    document.getElementById("formCadastro").reset();
```

- `function limparFormulario()`: Função para limpar o formulário
- `document.getElementById("formCadastro").reset()`: Reseta todos os campos do formulário

```javascript
    function enviar Formulario() {
        if (validar Formulario()) {
            alert("Formulário enviado (simulação).");
            // aqui poderia ter código para enviar via fetch/XHR
        }
    }
</script>
```

- `function enviar Formulario()`: Função para enviar o formulário após validação
- `alert()`: Mensagem de confirmação (simulação)

## Código Depois - indexdepois.html

### Melhorias na Estrutura HTML

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AvoidNess - Cadastro</title>
```

- `<meta name="viewport">`: Torna o site responsivo para dispositivos móveis
- Título atualizado para refletir a marca AvoidNess

### Integração com Fontes Externas

```html
<link
    href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Rajdhani:wght@500;700&display=swap"
    rel="stylesheet">
<link rel="stylesheet" href="AvoidNess.css">
```

- Importação de fontes personalizadas do Google Fonts
- Link para o arquivo CSS externo AvoidNess.css

### Estilos CSS Aprimorados

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(to bottom, #2d1b4e, #0d0521);
    font-family: 'Space Grotesk', sans-serif;
}
```

- Gradiente de fundo roxo escuro
- Fonte personalizada 'Space Grotesk'
- `min-height: 100vh`: Garante que o body tenha pelo menos a altura da tela

```css
.login-card {
    background: rgba(15, 10, 30, 0.9);
    border-radius: 16px;
    padding: 2.5rem;
    max-width: 400px;
    width: 100%;
    box-shadow: 0 0 25px rgba(138, 43, 226, 0.3);
    backdrop-filter: blur(12px);
    animation: fadeInUp 0.8s ease forwards;
}
```

- Design de card moderno com bordas arredondadas
- Efeito de desfoque de fundo (`backdrop-filter`)
- Animação de entrada suave

### Inputs com Efeitos Avançados

```html
<div class="input-group">
    <input type="text" id="nome" name="nome" placeholder=" " required>
    <label for="nome">Nome</label>
</div>
```

- Estrutura de grupo para inputs com labels flutuantes
- `placeholder=" "`: Espaço em branco necessário para o efeito de animação
- `required`: Torna o campo obrigatório

```css
.input-group input:focus+label,
.input-group input:not(:placeholder-shown)+label {
    top: -12px;
    font-size: 0.75rem;
    color: #8a2be2;
}
```

- Efeito de label flutuante quando o input está focado ou preenchido
- Transição suave de posição e tamanho da fonte

### Validações JavaScript Aprimoradas

```javascript
function validarFormulario() {
    let nome = document.getElementById("nome").value.trim();
    let email = document.getElementById("email").value.trim();
    let senha = document.getElementById("senha").value;
    let telefone = document.getElementById("telefone").value.trim();
    let idade = document.getElementById("idade").value;

    // Nome
    let regexNome = /^[A-Za-zÀ-ÖØ-öø-ÿ\s]{3,}$/;
    if (!regexNome.test(nome)) {
        alert("O nome deve ter pelo menos 3 letras e não conter números.");
        return false;
    }
```

- `.trim()`: Remove espaços em branco no início e fim
- Expressões regulares para validações específicas
- `regexNome`: Permite letras, acentos e espaços, mínimo de 3 caracteres

```javascript
    // Email
    let regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!regexEmail.test(email)) {
        alert("Digite um e-mail válido.");
        return false;
    }
```

- Validação de formato de email com expressão regular

```javascript
    // Senha
    let regexSenha = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
    if (!regexSenha.test(senha)) {
        alert("A senha deve ter no mínimo 8 caracteres, incluindo letra maiúscula, minúscula, número e símbolo.");
        return false;
    }
```

- Validação de senha forte:
  - `(?=.*[a-z])`: Pelo menos uma letra minúscula
  - `(?=.*[A-Z])`: Pelo menos uma letra maiúscula
  - `(?=.*\d)`: Pelo menos um número
  - `(?=.*[\W_])`: Pelo menos um caractere especial
  - `.{8,}`: Mínimo de 8 caracteres

```javascript
    // Telefone
    if (telefone !== "" && !/^\d{11}$/.test(telefone)) {
        alert("Digite um telefone válido com 11 números (DDD + número).");
        return false;
    }

    // Idade
    if (idade !== "" && (idade < 12 || idade > 120)) {
        alert("A idade deve estar entre 12 e 120 anos.");
        return false;
    }
```

- Validação condicional para telefone (somente se preenchido)
- Restrição de idade entre 12 e 120 anos

### Botões de Login Social

```html
<button class="btn-alt">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" alt="Google">
    Continuar com Google
</button>
```

- Botões para login com redes sociais
- Ícones carregados de CDNs externos

## AvoidNess.css

### Classes Utilitárias e Efeitos

```css
.gradient-text {
    background: linear-gradient(to right, #8a2be2, #4a0080);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}
```

- Texto com gradiente de cores
- `-webkit-background-clip: text`: Recorte do fundo apenas no texto

```css
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
}
```

- Efeito hover nos cards com elevação e sombra aumentada

### Animações

```css
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}
```

- Animação de fade-in com movimento ascendente
- Usada para dar entrada suave aos elementos

```css
.floating {
    animation: floating 3s ease-in-out infinite;
}
```

- Elementos com animação flutuante contínua

## Conclusão

A evolução do código e para demonstrar melhorias significativas em:

1. **Design**: Interface moderna com gradientes, sombras e animações
2. **Validações**: Regras mais robustas para garantir qualidade dos dados
3. **Responsividade**: Compatibilidade com dispositivos móveis
4. **Experiência do Usuário**: Feedback visual e interações aprimoradas
5. **Organização**: Separação de estilos em arquivo CSS externo