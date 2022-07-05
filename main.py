from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '700')
from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.lang import Builder
from kivy.config import Config
import random, time, os

class Dibujar(Widget):

    def __init__(self, **kwargs):
        super(Dibujar, self).__init__(**kwargs)
        Clock.schedule_once(self.appear_target, 1)
        #self.ids.animal.reload()

    def appear_target(self, *args):
        target = Target()
        self.add_widget(target)

class Target(Widget):

    def on_touch_move(self, touch):
        self.parent.remove_widget(self)
        return Dibujar()


class AnimalesApp(App):

    def build(self):
        return Dibujar()

if __name__ == '__main__':
    AnimalesApp().run()