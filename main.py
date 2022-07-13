from kivy.config import Config

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '700')

from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Rectangle
from kivy.lang import Builder
from kivy.config import Config
import random

class Dibujar(Widget):

    def __init__(self, **kwargs):
        super(Dibujar, self).__init__(**kwargs)
        Clock.schedule_interval(self.appear_target, random.randint(2, 4))
        #Clock.schedule_once(self.appear_target, random.randint(2, 4))

    def appear_target(self, *args):
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        target = random.choice(animales)
        self.add_widget(target)

class Elefante(Widget):
    
    def callback(self):
        self.parent.remove_widget(self)
    
class Gallina(Widget):

    def callback(self):
        self.parent.remove_widget(self)
    
class Gato(Widget):

    def callback(self):
        self.parent.remove_widget(self)
    
class Leon(Widget):

    def callback(self):
        self.parent.remove_widget(self)
    
class Oveja(Widget):

    def callback(self):
        self.parent.remove_widget(self)
    
class Perro(Widget):

    def callback(self):
        self.parent.remove_widget(self)
    
class AnimalesApp(App):

    def build(self):
        return Dibujar()

if __name__ == '__main__':
    AnimalesApp().run()