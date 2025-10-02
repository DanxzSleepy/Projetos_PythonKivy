

---

# 📝 Documentação do Formulário "AvoidNess"

## 🌑 Antes (Código Original)

O projeto inicial era um **formulário básico de cadastro** em HTML, CSS e JS, mas tinha erros que afetavam tanto a usabilidade quanto a aparência.

### Organização do Código

- Estrutura simples com `<div class="card">` centralizando o formulário.
    
- Campos: Nome, Email, Senha, Telefone e Idade.
    
- Dois botões em `<div class="actions">`: **Cadastrar** e **Limpar**.
    
- CSS e JS **embutidos** no HTML.
    

### Pontos Fortes

- Estrutura clara e didática.
    
- Uso de `<label>` associado ao campo → acessibilidade.
    
- Botões bem definidos.
    
- Simulação de envio com `alert`.
    

### Erros e Inconsistências

**HTML**

- `telefone` e `idade` definidos como `type="email"` (errado).
    
- O botão **Limpar** chama `clearFields()`, mas essa função não existe.
    
- Encoding quebrado no título e labels (ex: `<h2Cadastro</h2`).
    

**CSS**

- Linha `font-family: Arial, sans-serif background-color: #ffffff;` com **erro de sintaxe** (faltou ponto e vírgula).
    
- Chave extra `}` no bloco `.actions`.
    
- Estilo sem identidade AvoidNess (muito neutro).
    

**JavaScript**

- Função `validar Formulario()` escrita com espaço → **erro de sintaxe**.
    
- Variável `emai` ao invés de `email`.
    
- Validação inconsistente: `if (nome === || emai...` → código quebrado.
    
- Função `limparFormulario()` vazia, mas com `reset()` solto fora dela.
    
- Conflito: `onsubmit="validarFormulario()"` e botão "Cadastrar" chamando `enviarFormulario()`.
    

---

## 🌘 Depois (Código Corrigido + Estilo AvoidNess)

O novo código foi refeito com:

- **Visual AvoidNess**: dark com neon roxo, blur e animação suave.
    
- **Inputs flutuantes** (UX moderna).
    
- **Validações profissionais** (Regex, limites e mensagens claras).
    
- **Botões sociais** (Google, Microsoft, Apple).
    
- Código organizado e sem erros de sintaxe.
    

---

### Estrutura HTML

- Mantida a base, mas modernizada.
    
- Campos corrigidos:
    
    - Telefone → `type="tel"`, `pattern="[0-9]{11}"`, `maxlength="11"`.
        
    - Idade → `type="number"`, `min="12"`, `max="120"`.
        
- Labels flutuantes para experiência melhor.
    
- Separador com **"Ou"** antes dos botões sociais.
    

---

### Estilo CSS (AvoidNess)

- Fundo dark gradiente: `#2d1b4e → #0d0521`.
    
- Card translúcido com `backdrop-filter: blur(12px)`.
    
- Inputs minimalistas com labels animadas.
    
- Botão principal (`Cadastrar`) com efeito neon roxo.
    
- Botões sociais com hover roxo sutil.
    

Exemplo:

```css
.input-group input:focus {
  border-color: #8a2be2;
}

.input-group input:focus+label {
  top: -12px;
  font-size: 0.75rem;
  color: #8a2be2;
}
```

---

### Validações JavaScript

Foram aplicadas regras **mais realistas e seguras**:

- **Nome**: mínimo 3 letras, apenas letras e espaços.
    
- **Email**: formato válido (`usuario@dominio.com`).
    
- **Senha**: mínimo 8 caracteres, contendo:
    
    - 1 maiúscula
        
    - 1 minúscula
        
    - 1 número
        
    - 1 símbolo
        
- **Telefone**: exatamente 11 dígitos.
    
- **Idade**: entre 12 e 120 anos.
    

Exemplo:

```javascript
let regexSenha = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$/;
if (!regexSenha.test(senha)) {
  alert("A senha deve ter no mínimo 8 caracteres, incluindo letra maiúscula, minúscula, número e símbolo.");
  return false;
}
```

---

## ✅ Resultado Final

- **Antes**: formulário funcional, mas cheio de erros e sem estilo.
    
- **Depois**: formulário **"profissional"**, coerente com o projeto AvoidNess, validado corretamente e com uma UI moderna.
    

---

## ⚡ Melhorias Futuras

- Mostrar mensagens de erro **embaixo do input** (UX melhor que `alert` "foi uma ideia da ia mas eu Nao quero).
    
- Adicionar campo de **confirmar senha**. (normalmente tem)
    
- Validação em tempo real (`oninput`). (esqueci o que e isso)
    
- Integração com backend (Django/Node "depende isso aqui pq eu ja to fazendo k).
    

---

