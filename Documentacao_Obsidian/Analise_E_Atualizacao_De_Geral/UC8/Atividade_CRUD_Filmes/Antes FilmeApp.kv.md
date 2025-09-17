```kv
<CadastroScreen>:

    titulo: titulo

    genero: genero

    ano: ano

    imagem: imagem

    BoxLayout:

        orientation: "vertical"

        padding: 20

        spacing: 10

  

        Label:

            text: "Cadastro de Filmes"

            font_size: 24

  

        TextInput:

            id: titulo

            hint_text: "Título"

        TextInput:

            id: genero

            hint_text: "Gênero"

        TextInput:

            id: ano

            hint_text: "Ano de Lançamento"

            input_filter: "int"

        TextInput:

            id: imagem

            hint_text: "Caminho da Imagem (opcional)"

  

        Button:

            text: "Salvar"

            on_release: root.salvar_filme()

        Button:

            text: "Ir para Listagem"

            on_release: app.root.current = "listagem"

  
  
  

<ListagemScreen>:

    lista: lista

    BoxLayout:

        orientation: "vertical"

        padding: 20

        spacing: 10

  

        Label:

            text: "Lista de Filmes"

            font_size: 24

  

        ScrollView:

            GridLayout:

                id: lista

                cols: 1

                spacing: 5

                size_hint_y: None

                height: self.minimum_height

  

        Button:

            text: "Voltar ao Cadastro"

            on_release: app.root.current = "cadastro"

  
  

<EdicaoScreen>:

    titulo: titulo

    genero: genero

    ano: ano

    imagem: imagem  # <-- referencia aqui

  

    BoxLayout:

        orientation: "vertical"

        padding: 20

        spacing: 10

  

        TextInput:

            id: titulo

            hint_text: "Título"

  

        TextInput:

            id: genero

            hint_text: "Gênero"

  

        TextInput:

            id: ano

            hint_text: "Ano"

  

        TextInput:

            id: imagem

            hint_text: "Caminho da Imagem (opcional)"

  

        Button:

            text: "Salvar Alterações"

            on_release: root.salvar_edicao()
```