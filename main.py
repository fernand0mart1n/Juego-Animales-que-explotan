from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '700')

from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Rectangle
from kivy.lang import Builder
from kivy.config import Config
import random

class Dibujar(Widget):

    def __init__(self, **kwargs):
        super(Dibujar, self).__init__(**kwargs)
        #Clock.schedule_interval(self.appear_target, random.randint(2, 4))
        Clock.schedule_once(self.appear_target, random.randint(2, 4))
        #self.ids.animal.reload()

    def appear_target(self, *args):
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        target = random.choice(animales)
        self.add_widget(target)

class Elefante(Widget):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return super().on_touch_down(touch)

class Gallina(Widget):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return super().on_touch_down(touch)

class Gato(Widget):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return super().on_touch_down(touch)

class Leon(Widget):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return super().on_touch_down(touch)      

class Oveja(Widget):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return super().on_touch_down(touch)  

class Perro(Widget):

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.remove_widget(self)
        animales = [Elefante(), Gallina(), Gato(), Leon(), Oveja(), Perro()]
        return super().on_touch_down(touch)

class AnimalesApp(App):

    def build(self):
        return Dibujar()

if __name__ == '__main__':
    AnimalesApp().run()