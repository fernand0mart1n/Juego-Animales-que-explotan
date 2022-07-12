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
        Clock.schedule_interval(self.appear_target, 1.5)
        #Clock.schedule_once(self.appear_target, random.randint(2, 4))

    def appear_target(self, *args):
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        target = random.choice(animales)
        self.add_widget(target)

class Elefante(Widget):
    
    def callback(self):
        self.ids.animal1.opacity = 0
    
class Gallina(Widget):

    def callback(self):
        self.ids.animal2.opacity = 0
    
class Gato(Widget):

    def callback(self):
        self.ids.animal3.opacity = 0
    
class Leon(Widget):

    def callback(self):
        self.ids.animal4.opacity = 0
    
class Oveja(Widget):

    def callback(self):
        self.ids.animal5.opacity = 0
    
class Perro(Widget):

    def callback(self):
        self.ids.animal6.opacity = 0
    
class AnimalesApp(App):

    def build(self):
        return Dibujar()

if __name__ == '__main__':
    AnimalesApp().run()