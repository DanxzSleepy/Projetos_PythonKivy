```python
<RegistrationScreen>:
    title_input: title_input
    genre_input: genre_input
    year_input: year_input
    image_input: image_input
    
    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        Label:
            text: "Cadastro de Filmes"
            font_size: 24
            bold: True
            size_hint_y: 0.1

        TextInput:
            id: title_input
            hint_text: "Título do Filme"
            size_hint_y: 0.1

        TextInput:
            id: genre_input
            hint_text: "Gênero"
            size_hint_y: 0.1

        TextInput:
            id: year_input
            hint_text: "Ano de Lançamento"
            input_filter: "int"
            size_hint_y: 0.1

        TextInput:
            id: image_input
            hint_text: "Caminho da Imagem (opcional)"
            size_hint_y: 0.1

        BoxLayout:
            orientation: "horizontal"
            spacing: 10
            size_hint_y: 0.2

            Button:
                text: "Salvar Filme"
                on_release: root.save_movie()

            Button:
                text: "Ver Lista"
                on_release: app.root.current = "list"

<ListScreen>:
    movie_list: movie_list
    
    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        Label:
            text: "Lista de Filmes"
            font_size: 24
            bold: True
            size_hint_y: 0.1

        ScrollView:
            GridLayout:
                id: movie_list
                cols: 1
                spacing: 10
                size_hint_y: None
                height: self.minimum_height

        Button:
            text: "Voltar ao Cadastro"
            size_hint_y: 0.1
            on_release: app.root.current = "register"

<EditScreen>:
    title_input: title_input
    genre_input: genre_input
    year_input: year_input
    image_input: image_input
    
    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        Label:
            text: "Editar Filme"
            font_size: 24
            bold: True
            size_hint_y: 0.1

        TextInput:
            id: title_input
            hint_text: "Título do Filme"
            size_hint_y: 0.1

        TextInput:
            id: genre_input
            hint_text: "Gênero"
            size_hint_y: 0.1

        TextInput:
            id: year_input
            hint_text: "Ano de Lançamento"
            input_filter: "int"
            size_hint_y: 0.1

        TextInput:
            id: image_input
            hint_text: "Caminho da Imagem (opcional)"
            size_hint_y: 0.1

        BoxLayout:
            orientation: "horizontal"
            spacing: 10
            size_hint_y: 0.2

            Button:
                text: "Salvar Alterações"
                on_release: root.save_edits()

            Button:
                text: "Cancelar"
                on_release: app.root.current = "list"

<MovieItem>:
    canvas.before:
        Color:
            rgba: 0.9, 0.9, 0.9, 1
        Rectangle:
            pos: self.pos
            size: self.size
```