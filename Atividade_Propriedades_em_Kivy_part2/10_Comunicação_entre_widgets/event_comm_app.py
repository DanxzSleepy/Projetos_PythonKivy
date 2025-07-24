from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivy.event import EventDispatcher

class GlobalState(EventDispatcher):
    current_status = StringProperty("Inicial")

class StatusDisplayWidget(BoxLayout):
    global_state_obj = ObjectProperty()

class StatusChangerWidget(BoxLayout):
    global_state_obj = ObjectProperty()

    def change_status(self, new_status):
        self.global_state_obj.current_status = new_status

class EventCommApp(App):
    def build(self):
        self.shared_state = GlobalState()

        root = BoxLayout(orientation='vertical')
        root.add_widget(StatusDisplayWidget(global_state_obj=self.shared_state))
        root.add_widget(StatusChangerWidget(global_state_obj=self.shared_state))
        return root

if __name__ == '__main__':
    EventCommApp().run()
