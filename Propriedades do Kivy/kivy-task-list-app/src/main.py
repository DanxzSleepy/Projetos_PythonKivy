from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from task_manager import TaskManager

class TaskListApp(App):
    def build(self):
        self.task_manager = TaskManager()
        return Builder.load_file('ui.kv')

    def add_task(self, task):
        if task:
            self.task_manager.add_task(task)
            self.update_task_list()

    def update_task_list(self):
        task_list = self.root.ids.task_list
        task_list.clear_widgets()
        for task in self.task_manager.get_tasks():
            task_list.add_widget(Label(text=task))
            
    def clear_tasks(self):
        self.task_manager.clear_tasks()
        self.update_task_list()        

if __name__ == '__main__':
    TaskListApp().run()
    