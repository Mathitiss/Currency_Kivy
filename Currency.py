import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

kivy.require('1.9.0')

Builder.load_string("""
<Start>:
    canvas:
        Color:
            rgba: 2, 5, 207, 1
        Rectangle:
            size: self.size
""")

screen_manager = ScreenManager()

class Start(Screen):
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)

screen_manager.add_widget(Start(name="Start"))

class Currency(App):
    def build(self):
        Window.size = (375, 645)
        screen_manager.current = 'Start'
        return screen_manager

Currency().run()