# 📘 UC08 - Atividade 06

## Consumindo uma API em um App com Kivy

### 🎯 Objetivo

* Compreender o conceito de API e sua importância no desenvolvimento de software.
* Utilizar o Kivy para criar uma interface gráfica em Python.
* Consumir dados de uma API externa e exibi-los em um aplicativo.

---

## 🔎 Parte 1 – Pesquisa e Conceitos

### 1. O que é uma API?

API significa **Application Programming Interface**.
É uma “ponte” que permite que diferentes programas e sistemas se comuniquem, trocando dados e funcionalidades.

---

### 2. Para que serve uma API pública? Cite dois exemplos.

Uma API pública serve para disponibilizar dados/serviços abertamente na internet, para que desenvolvedores possam utilizá-los em seus aplicativos.

**Exemplos:**

* **OpenWeather API** → fornece informações sobre clima e previsão do tempo.
* **PokéAPI** → fornece dados sobre Pokémon (nomes, tipos, evoluções etc).

---

### 3. O que significa uma requisição HTTP GET?

É um tipo de requisição que o cliente (nosso app) envia ao servidor para **obter dados**.
Na prática, é o método usado para buscar informações em uma API.

---

### 4. Por que usamos o módulo `requests` em Python?

Porque ele simplifica a comunicação com servidores HTTP, permitindo enviar requisições (GET, POST etc.) e receber respostas de maneira prática.

---

### 5. Quais são os principais componentes básicos de uma interface em Kivy?

* **BoxLayout** → organiza os widgets em linhas ou colunas.
* **Label** → exibe textos.
* **Button** → cria botões interativos.
* (Outros comuns: **TextInput**, **Image**, **FloatLayout** etc.)

---

## 🖥️ Parte 2 – Desenvolvimento do App

### API utilizada

👉 [Official Joke API](https://official-joke-api.appspot.com/random_joke)

Exemplo de resposta:

```json
{
  "id": 123,
  "type": "general",
  "setup": "Por que o computador foi ao médico?",
  "punchline": "Porque pegou um vírus!"
}
```

---

### Código do Aplicativo (main.py)

```python
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class JokeApp(App):
    def build(self):
        # Layout principal
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Label para mostrar a piada
        self.joke_label = Label(
            text="Clique no botão para ver uma piada!",
            halign="center",
            valign="middle",
            font_size=20
        )
        self.joke_label.bind(size=self.joke_label.setter('text_size'))

        # Botão para carregar nova piada
        self.button = Button(
            text="Nova piada 😂",
            size_hint=(1, 0.2),
            font_size=18
        )
        self.button.bind(on_press=self.get_joke)

        # Adiciona ao layout
        self.layout.add_widget(self.joke_label)
        self.layout.add_widget(self.button)

        return self.layout

    def get_joke(self, instance):
        try:
            url = "https://official-joke-api.appspot.com/random_joke"
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                joke = response.json()
                setup = joke.get("setup", "")
                punchline = joke.get("punchline", "")
                self.joke_label.text = f"{setup}\n\n{punchline}"
            else:
                self.joke_label.text = "Erro ao carregar piada 😢"
        except Exception as e:
            self.joke_label.text = f"Erro: {e}"

if __name__ == "__main__":
    JokeApp().run()
```

---

## 🧪 Como testar

1. Instalar dependências:

   ```bash
   pip install kivy requests
   ```
2. Rodar o app:

   ```bash
   python main.py
   ```
3. Clicar no botão → aparecerá uma piada carregada da API.

---

## 💡 Desafio Extra (opcional)

* Usar outra API pública (ex: frases motivacionais, clima, curiosidades).
* Adicionar cores, título ou layout diferente para personalizar a interface.

---

## 📌 Entrega

* Arquivo `.py` com o código no GitHub.
* Documento `.pdf` ou `.docx` com:

  * Respostas da parte teórica.
  * Prints do app funcionando.
* Vídeo curto mostrando:

  1. App rodando.
  2. Botão sendo clicado e piada aparecendo.
  3. Código do app no final.

---
