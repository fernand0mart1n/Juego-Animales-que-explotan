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
import random

class Dibujar(Widget):

    def __init__(self, **kwargs):
        super(Dibujar, self).__init__(**kwargs)
        Clock.schedule_once(self.appear_target, 1)
        #self.ids.animal.reload()

    def appear_target(self, *args):
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        target = random.choice(animales)
        self.add_widget(target)

class Elefante(Widget):

    def on_touch_down(self, touch):
        self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return Dibujar.appear_target(random.choice(animales))

class Gallina(Widget):

    def on_touch_down(self, touch):
        self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return Dibujar.appear_target(random.choice(animales))

class Gato(Widget):

    def on_touch_down(self, touch):
        self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return Dibujar.appear_target(random.choice(animales))

class Leon(Widget):

    def on_touch_down(self, touch):
        self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return Dibujar.appear_target(random.choice(animales))      

class Oveja(Widget):

    def on_touch_down(self, touch):
        self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return Dibujar.appear_target(random.choice(animales))  

class Perro(Widget):

    def on_touch_down(self, touch):
        self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return Dibujar.appear_target(random.choice(animales))

class AnimalesApp(App):

    def build(self):
        return Dibujar()

if __name__ == '__main__':
    AnimalesApp().run()