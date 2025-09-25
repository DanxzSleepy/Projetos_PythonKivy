### 1. Registro de Problemas

- Todos os problemas serão registrados em uma **ferramenta de tickets** (Jira, Trello ou Redmine).
    
- Fontes: cliente (e-mail, portal de suporte, telefone) ou equipe interna (QA/testes).
    
- Cada ticket deve conter:
    
    - **Título:** resumo do problema.
        
    - **Descrição:** explicação clara do erro ou solicitação.
        
    - **Prioridade:** Crítica, Alta, Média, Baixa.
        
    - **Gravidade:** Bloqueador, Alto, Médio, Baixo.
        
    - **Módulo afetado** (ex: Login, Relatórios, Financeiro).
        
    - **Anexos:** prints, vídeos, logs de erro.
        

### 2. Análise e Responsáveis

- O **analista de suporte** ou **gerente de projetos** fará a triagem inicial.
    
- Etapas da análise:
    
    - Validar se o problema é legítimo.
        
    - Classificar como: **Bug/Correção, Melhoria ou Nova Funcionalidade**.
        
    - Definir prioridade/gravidade.
        
    - Atribuir a um **desenvolvedor especializado** (frontend, backend, banco de dados etc.).
        

### 3. Acompanhamento e Prazos

- O status do ticket será atualizado na própria plataforma:
    
    - **Aberto → Em Análise → Em Desenvolvimento → Em Teste → Concluído.**
        
- O prazo dependerá da prioridade:
    
    - **Crítico:** até 4h.
        
    - **Alto:** até 24h.
        
    - **Médio:** até 1 semana.
        
    - **Baixo:** backlog ou sprint futuro.
        
- O gerente de projetos fará **reuniões semanais de acompanhamento**.
    
- Após entrega, a equipe de QA fará **validação** e o cliente será informado.
    

---

## Simulações de Protocolos

**1. Bug Crítico – Login**

- **Problema:** usuários não conseguem acessar o sistema, tela recarrega sem mensagem de erro.
    
- **Registro:** ticket aberto pelo suporte, prioridade Crítica, gravidade Bloqueador.
    
- **Análise:** atribuído a desenvolvedor backend.
    
- **Acompanhamento:** erro 500 na API de autenticação corrigido em 2h. Testado e validado.
    

**2. Erro de Relatório Financeiro**

- **Problema:** soma de vendas diárias incorreta.
    
- **Registro:** ticket aberto pelo setor financeiro, prioridade Alta.
    
- **Análise:** atribuído a desenvolvedor SQL.
    
- **Acompanhamento:** regra de imposto estava errada. Corrigido em 1 dia e validado.
    

**3. Melhoria de Usabilidade – Botão Salvar**

- **Problema:** botão escondido causa confusão.
    
- **Registro:** ticket aberto pelo cliente, prioridade Média.
    
- **Análise:** classificado como Melhoria, agendado para próximo sprint.
    
- **Acompanhamento:** botão movido para local visível. Implementado na nova versão.
    

**4. Erro de Permissão – Acesso Negado**

- **Problema:** gerente não acessa módulo de Análise, mesmo com permissão.
    
- **Registro:** prioridade Alta, ticket do suporte.
    
- **Análise:** erro na lógica de verificação de permissões.
    
- **Acompanhamento:** corrigido em algumas horas, validado e liberado.
    

**5. Nova Funcionalidade – Exportação CSV**

- **Problema:** cliente pede exportação de relatórios em CSV.
    
- **Registro:** ticket aberto pelo gerente de projetos, prioridade Baixa.
    
- **Análise:** classificado como Nova Funcionalidade.
    
- **Acompanhamento:** incluído no backlog, planejado para o próximo trimestre.