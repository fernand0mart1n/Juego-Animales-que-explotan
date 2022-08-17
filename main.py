from kivy.app import App
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior
from kivy.graphics import Rectangle
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.config import Config
import HoverBehavior
import random
import os

class Dibujar(Widget):

    def __init__(self, **kwargs):
        super(Dibujar, self).__init__(**kwargs)

        Clock.schedule_interval(self.appear_target, 3)
        sound = SoundLoader.load('snd/musica.mp3')
        sound.loop = True
        sound.play()
        #Clock.schedule_once(self.appear_target, 3)

    def appear_target(self, *args):
        
        animal = Animal()
        self.add_widget(animal)
        #nombre_animal = animal.audio.split('.')[0]
        #sonido = SoundLoader.load('snd/' + nombre_animal + '.wav')
        #sonido.play()

class Animal(Widget):

    def callback(self):
        self.parent.remove_widget(self)
    
class AnimalesApp(App):

    def build(self):
        
        return Dibujar()

if __name__ == '__main__':
    Config.set('graphics', 'fullscreen', '2')
    Config.set('graphics', 'window_state', 'maximized')
    Config.write()
    AnimalesApp().run()