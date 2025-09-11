from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class Tela4(Screen):
    title = StringProperty('Tela 4')
    description = StringProperty('Esta é a Tela 4 do aplicativo.')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Título
        title_label = Label(text=self.title, font_size=30, size_hint_y=0.2)
        
        # Botão voltar
        back_btn = Button(text='Voltar', size_hint_y=0.1)
        back_btn.bind(on_press=self.go_back)
        
        # Descrição
        desc_label = Label(text=self.description, font_size=18)
        
        layout.add_widget(title_label)
        layout.add_widget(back_btn)
        layout.add_widget(desc_label)
        
        self.add_widget(layout)
    
    def go_back(self, instance):
        self.manager.current = 'home'