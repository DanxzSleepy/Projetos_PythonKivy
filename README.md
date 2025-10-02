# Projeto Kivy - Desenvolvimento de Aplicações Multiplataforma

Este repositório contém uma coleção abrangente de aplicações desenvolvidas com o framework Kivy em Python, demonstrando desde conceitos básicos até técnicas avançadas de programação GUI multiplataforma. O projeto foi estruturado como um currículo educacional completo para o aprendizado de desenvolvimento com Kivy.

## 📋 Visão Geral do Projeto

O projeto é organizado em várias unidades curriculares (UCs) que cobrem diferentes aspectos do desenvolvimento com Kivy, desde aplicações simples até sistemas complexos com integração de banco de dados. O repositório também inclui documentação completa em formato Obsidian e exemplos práticos de jogos.

### Estrutura Principal

```
├── Documentacao_Obsidian/      # Documentação completa em formato Obsidian
├── Jogos Py_Kv_html/           # Jogos desenvolvidos com Python/Kivy
├── Propriedades do Kivy/       # Exemplos e atividades sobre propriedades do Kivy
├── Reaprendendo kivy - UC 08 - Atividades/  # Atividades da Unidade Curricular 8
└── LICENSE                     # Licença do projeto
```

## 🎯 Destaques do Projeto

### 1. CRUD de Filmes com Banco de Dados SQLite

**Localização**: `Reaprendendo kivy - UC 08 - Atividades/UC 08 - Atividade DBkivy/UC8_CRUD_Filmes/`

Aplicação profissional de gerenciamento de filmes com todas as operações CRUD:
- **Create**: Cadastro de novos filmes com título, gênero, ano e imagem
- **Read**: Listagem completa dos filmes cadastrados
- **Update**: Edição de informações de filmes existentes
- **Delete**: Remoção de filmes do banco de dados

#### Arquivos Principais:

1. **CRUD-filmesWBD.py** (Depois) - Versão final profissional:
   - Implementa o padrão Repository com classe [DatabaseManager](file:///c:/Users/Danilo54279466/Coder/dev/projetoskivy/Reaprendendo%20kivy%20-%20UC%2008%20-%20Atividades/UC%2008%20-%20Atividade%20DBkivy/UC8_CRUD_Filmes/Depois/CRUD-filmesWBD.py#L37-L154) para acesso a dados
   - Utiliza ScreenManager para navegação entre telas
   - Implementa widgets personalizados como [MovieItem](file:///c:/Users/Danilo54279466/Coder/dev/projetoskivy/Reaprendendo%20kivy%20-%20UC%2008%20-%20Atividades/UC%2008%20-%20Atividade%20DBkivy/UC8_CRUD_Filmes/Depois/CRUD-filmesWBD.py#L157-L225)
   - Segue boas práticas de programação com documentação extensiva
   - Utiliza context managers para gerenciamento de conexões com banco de dados
   - Implementa validação de entrada de dados e tratamento de erros

2. **CRUD-filmesWBD.py** (Antes) - Versão inicial:
   - Implementação mais direta das funções de banco de dados
   - Estrutura básica de telas sem separação clara de responsabilidades
   - Funções globais para operações CRUD

3. **MovieApp.kv** (Depois) - Interface declarativa:
   - Define layouts para [RegistrationScreen](file:///c:/Users/Danilo54279466/Coder/dev/projetoskivy/Reaprendendo%20kivy%20-%20UC%2008%20-%20Atividades/UC%2008%20-%20Atividade%20DBkivy/UC8_CRUD_Filmes/Depois/MovieApp.kv#L2-L42), [ListScreen](file:///c:/Users/Danilo54279466/Coder/dev/projetoskivy/Reaprendendo%20kivy%20-%20UC%2008%20-%20Atividades/UC%2008%20-%20Atividade%20DBkivy/UC8_CRUD_Filmes/Depois/MovieApp.kv#L44-L69) e [EditScreen](file:///c:/Users/Danilo54279466/Coder/dev/projetoskivy/Reaprendendo%20kivy%20-%20UC%2008%20-%20Atividades/UC%2008%20-%20Atividade%20DBkivy/UC8_CRUD_Filmes/Depois/MovieApp.kv#L71-L105)
   - Utiliza propriedades do tipo ObjectProperty para vinculação
   - Define estilos visuais com Canvas instructions

4. **FilmeApp.kv** (Antes) - Interface básica:
   - Estrutura mais simples sem estilização avançada
   - Layouts básicos para as funcionalidades essenciais

#### Características Técnicas:
- Arquitetura profissional usando padrão Repository
- Interface responsiva com Kivy Language (.kv files)
- Validação de entrada de dados
- Prevenção de injeção SQL com consultas parametrizadas
- Gerenciamento adequado de conexões com banco de dados
- Tratamento de erros e feedback ao usuário
- Widgets personalizados para exibição de itens
- Navegação entre telas com ScreenManager

### 2. Jogos Desenvolvidos com Kivy

**Localização**: `Jogos Py_Kv_html/`

Coleção de jogos clássicos implementados com Kivy:

#### Paint Completo (`Paint/PaintCompleto.py`):
- Aplicação de desenho com múltiplas ferramentas (linha, retângulo, elipse)
- Sistema de cores aleatórias
- Controles deslizantes para ajuste de espessura
- Manipulação direta do Canvas do Kivy
- Tratamento de eventos de toque (touch events)
- Interface com FloatLayout para posicionamento preciso

#### Pong Game (`PongGame/main.py` e `PongGame/pong.kv`):
- Implementação do clássico jogo Pong
- Física de colisão com a biblioteca Vector do Kivy
- Controles por teclado e toque
- Pontuação e reinício automático
- Gráficos vetoriais com Canvas instructions
- Uso de ReferenceListProperty para vetores de velocidade

#### Pong Ball IA (`pongball_IA/index.html`):
- Versão web com inteligência artificial
- Implementada em HTML/JavaScript

### 3. Exploração de Propriedades do Kivy

**Localização**: `Propriedades do Kivy/`

Estudo detalhado das propriedades do Kivy com exemplos práticos:

#### Atividade_Propriedades_em_Kivy:
1. **StringProperty Básica** (`01_StringProperty Básica/string_prop_app.py`):
   - Demonstração fundamental de StringProperty
   - Vinculação automática entre propriedade e interface
   - Integração com arquivos KV

2. **NumericProperty e Interação** (`02_NumericProperty e Interação/numeric_prop_app.py`):
   - Propriedades numéricas reativas
   - Integração com sliders e inputs numéricos

3. **Vinculando StringProperty em Python** (`03_Vinculando StringProperty em Python/bind_string_app.py`):
   - Vinculação programática de propriedades
   - Uso do método bind() para callbacks

4. **BooleanProperty e ToggleButton** (`04_BooleanProperty e ToggleButton/bool_prop_app.py`):
   - Propriedades booleanas para estados
   - Integração com ToggleButton

5. **Vinculando em KV com on_property** (`05_Vinculando em KV com on_property/kv_bind_app.py`):
   - Vinculação declarativa no arquivo KV
   - Uso de eventos on_property

#### Atividade_Propriedades_em_Kivy_part2:
- Exploração avançada de propriedades como DictProperty, ReferenceListProperty, AliasProperty
- Implementação de propriedades aninhadas e eventos personalizados
- Persistência simulada e comunicação entre widgets

### 4. Fundamentos do Kivy - Progressão Didática

**Localização**: `Reaprendendo kivy - UC 08 - Atividades/`

Progressão didática do aprendizado com Kivy:

#### UC 08 - Atividade 01 (`A_AppHelloWorld.py`):
- Aplicação "Hello World" mais simples
- Introdução à classe App e ao widget Label
- Conceitos básicos de propriedades de widgets

#### UC 08 - Atividade 02 (`A_AppBoasVindas.py`):
- Introdução à interação com usuário
- Uso de TextInput e Button
- Event handling com callbacks
- Layout com BoxLayout

#### UC 08 - Atividade 03 (`A_AppIdadeAcesso.py`):
- Validação de entrada de dados
- Controle condicional de fluxo
- Feedback visual ao usuário

#### UC 08 - Atividade 04 (`A_AppSugestaoFilme.py`):
- Interface avançada com múltiplos widgets
- Widgets personalizados (Card)
- ToggleButton groups
- ScrollView para histórico
- Manipulação de imagens
- Validação complexa com regras de negócio

#### UC 08 - Atividade 05 (`A_AppSugestaoFilmeGenero.py`):
- Refinamento da aplicação de sugestão
- Melhorias na interface e experiência do usuário

#### UC 08 - Atividade 06 (`A_AppConsumAPI-kv.py`):
- Integração com APIs externas
- Processamento de dados JSON
- Tratamento de requisições assíncronas

#### UC 08 - Atividade 07 (`A_AppMulti-Telas_BoasVindas.py`):
- Introdução ao ScreenManager
- Navegação entre múltiplas telas
- Passagem de dados entre telas
- Aplicação completa integrando funcionalidades anteriores

#### UC 08 - Atividade DBkivy (`UC8_CRUD_Filmes/`):
- Projeto final integrador com banco de dados
- Implementação completa de CRUD
- Arquitetura profissional com separação de camadas

## 🧰 Tecnologias Utilizadas

- **Python 3.x**: Linguagem principal de desenvolvimento
- **Kivy**: Framework para aplicações GUI multiplataforma
- **SQLite**: Banco de dados embutido para persistência de dados
- **KV Language**: Linguagem declarativa para design de interfaces
- **Obsidian**: Para documentação e organização de conhecimento
- **HTML/CSS/JavaScript**: Para versões web de alguns jogos

## 📁 Estrutura Detalhada

### Documentacao_Obsidian/
Documentação completa do projeto em formato compatível com Obsidian, incluindo:

#### 1 - Criando README – Web, Desktop e Mobile:
- Comparação detalhada entre desenvolvimento Web, Desktop e Mobile
- Vantagens e limitações de cada ambiente
- Tecnologias e ferramentas utilizadas
- Exemplos práticos de cada tipo de aplicação

#### Analise_E_Atualizacao_De_Geral/Banco_De_Dados:
- Documentação de situações-problema e soluções implementadas
- Sistema de gerenciamento de biblioteca com MySQL
- Scripts SQL completos com tabelas, views e stored procedures
- Modelagem de dados avançada

#### Analise_E_Atualizacao_De_Geral/PaintCompleto:
- Análise antes e depois da implementação
- Documentação do código e suas funcionalidades

#### Analise_E_Atualizacao_De_Geral/PongGame:
- Comparação entre versões do jogo Pong
- Explicação das melhorias implementadas

#### Manutenção de Software:
- Introdução à manutenção de software
- Tipos de manutenção (corretiva, adaptativa, perfectiva, preventiva)
- Processos e fluxos de manutenção
- Métricas e planejamento estratégico

#### UC9 Atividades:
- Atividades de programação web com CRUD e localStorage
- Tipos de manutenção de software
- Protocolos de manutenção
- Erros, falhas e defeitos
- Métricas de manutenção
- Evolução em aplicações Web

### Jogos Py_Kv_html/
Implementações práticas de jogos:

#### Paint:
- Aplicação completa de desenho com múltiplas ferramentas
- Manipulação direta do Canvas
- Interface intuitiva com controles deslizantes

#### PongGame:
- Implementação completa do jogo Pong
- Física de colisão realista
- Controles por teclado e toque
- Sistema de pontuação

#### pongball_IA:
- Versão web com inteligência artificial
- Implementada em HTML/JavaScript

### Propriedades do Kivy/
Exploração técnica das funcionalidades do Kivy:

#### Atividade_Propriedades_em_Kivy:
- 10 exemplos progressivos de propriedades do Kivy
- Desde StringProperty básica até propriedades personalizadas
- Integração entre Python e KV files
- Vinculação de eventos e callbacks

#### Atividade_Propriedades_em_Kivy_part2:
- Propriedades avançadas como DictProperty, ReferenceListProperty
- AliasProperty e propriedades aninhadas
- Eventos personalizados
- Persistência simulada

#### Código_Kivy_Painel_de_Controle_da_IA:
- Interface de painel de controle
- Integração com sistemas de inteligência artificial

#### Estrutura de App Mobile com Kivy:
- Estrutura base para aplicações mobile
- Organização em telas e navegação
- Componentes reutilizáveis

#### Regras de Linguagem KV:
- Exemplos de uso avançado da linguagem KV
- Vinculação de propriedades
- Estilização de widgets

#### kivy-task-list-app:
- Aplicação completa de lista de tarefas
- CRUD local com persistência
- Interface moderna e responsiva

#### melhorando_a_tela_de_login_da_UI_UX:
- Exemplos de melhorias de interface
- Princípios de UI/UX aplicados
- Design responsivo

### Reaprendendo kivy - UC 08 - Atividades/
Progressão didática do aprendizado:

#### UC 08 - Atividades 01-07:
- Sequência de aplicações que introduzem conceitos progressivamente
- Da aplicação mais simples até sistemas complexos
- Integração de múltiplos conceitos em cada atividade

#### UC 08 - Atividade DBkivy:
- Projeto final integrador com banco de dados SQLite
- Implementação profissional de CRUD
- Arquitetura em camadas
- Interface completa com múltiplas telas

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- Kivy framework

### Instalação
```bash
pip install kivy
```

### Executando a Aplicação Principal (CRUD de Filmes)
```bash
cd "Reaprendendo kivy - UC 08 - Atividades/UC 08 - Atividade DBkivy/UC8_CRUD_Filmes/Depois"
python CRUD-filmesWBD.py
```

### Executando outros exemplos
```bash
# Hello World
python "Reaprendendo kivy - UC 08 - Atividades/UC 08 - Atividade 01/A_AppHelloWorld.py"

# Paint Application
python "Jogos Py_Kv_html/Paint/PaintCompleto.py"

# Pong Game
python "Jogos Py_Kv_html/PongGame/main.py"
```

## 📖 Documentação

A documentação completa está disponível na pasta `Documentacao_Obsidian/`, organizada por temas e unidades curriculares. Os principais tópicos incluem:

1. **Desenvolvimento Multiplataforma**: Comparação entre Web, Desktop e Mobile
2. **Soluções de Banco de Dados**: Implementação com MySQL
3. **Manutenção de Software**: Tipos, processos e métricas
4. **Programação Web**: Mini CRUDs com JSON e localStorage
5. **Análise de Código**: Antes e depois das implementações

## 🏗️ Arquitetura do CRUD de Filmes

### Componentes Principais

1. **DatabaseManager**: Camada de acesso a dados seguindo o padrão Repository
   - Criação e inicialização do banco de dados
   - Operações CRUD completas com segurança
   - Gerenciamento automático de conexões
   - Prevenção de injeção SQL com consultas parametrizadas

2. **Telas da Aplicação**:
   - **RegistrationScreen**: Cadastro de novos filmes
     - Validação de entrada de dados
     - Feedback visual com popups
     - Limpeza automática de campos após cadastro
   - **ListScreen**: Listagem e visualização de filmes
     - Atualização automática ao entrar na tela
     - Widgets personalizados para cada item
     - Scroll infinito para muitos registros
   - **EditScreen**: Edição de filmes existentes
     - Carregamento de dados existentes
     - Validação antes de salvar
     - Navegação de volta à lista

3. **Componentes Personalizados**:
   - **MovieItem**: Widget para exibição individual de filmes
     - Exibição de imagem (se disponível)
     - Informações do filme formatadas
     - Botões de edição e exclusão
     - Navegação entre telas
   - Popups para feedback ao usuário
   - Tratamento de erros e validações

### Padrões de Projeto Implementados

- **Repository Pattern**: Separação da lógica de negócio e acesso a dados
  - Classe DatabaseManager encapsula todas as operações de banco
  - Facilita testes e manutenção
  - Permite troca de tecnologia de banco de dados

- **MVC Pattern**: Separação clara entre modelo, visão e controlador
  - Modelos: Classes de dados e acesso a banco
  - Visão: Arquivos KV e widgets
  - Controlador: Classes de tela e lógica de interface

- **Factory Pattern**: Criação e gerenciamento de telas
  - ScreenManager cria e gerencia instâncias de telas
  - Facilita a navegação entre diferentes partes da aplicação

- **Observer Pattern**: Vinculação de propriedades e tratamento de eventos
  - Propriedades reativas que atualizam a interface automaticamente
  - Eventos de clique e interação do usuário

## 🔒 Segurança

- Consultas parametrizadas para prevenção de injeção SQL
- Validação de entrada de dados
- Tratamento adequado de exceções
- Gerenciamento seguro de conexões com banco de dados

## 📱 Plataformas Suportadas

As aplicações podem ser executadas em:
- Windows
- macOS
- Linux
- Android (com buildozer)
- iOS (com kivy-ios)

## 📝 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👥 Contribuição

Contribuições são bem-vindas! Para mudanças importantes, por favor abra uma issue primeiro para discutir o que você gostaria de modificar.

## 🙏 Agradecimentos

Projeto desenvolvido como parte do currículo educacional com foco em desenvolvimento de aplicações multiplataforma utilizando Python e Kivy. A documentação extensa demonstra o compromisso com o aprendizado profundo e a qualidade do código.