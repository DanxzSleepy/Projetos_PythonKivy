from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, AliasProperty
from kivy.lang import Builder

Builder.load_file("alias_prop.kv")

class CalculatorWidget(BoxLayout):
    num1 = NumericProperty(10)
    num2 = NumericProperty(5)

    def get_sum(self):
        return self.num1 + self.num2

    sum_result = AliasProperty(get_sum, None, bind=('num1', 'num2'))

class AliasPropApp(App):
    def build(self):
        return CalculatorWidget()

if __name__ == '__main__':
    AliasPropApp().run()
