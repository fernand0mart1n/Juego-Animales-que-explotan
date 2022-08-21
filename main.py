from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty
from kivy.lang import Builder
from kivy.config import Config
import HoverBehavior
import random
import os

ANIMALES = os.listdir("video")

class Dibujar(Widget):

    sound = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(Dibujar, self).__init__(**kwargs)

        self.play_song('snd/musica.mp3')

        Clock.schedule_interval(self.appear_target, 3)

    def appear_target(self, *args):

        nombre_animal = random.choice(ANIMALES).split('.')[0]
        animal = Animal()
        animal.fuente = 'video/' + nombre_animal + '.zip'
        self.add_widget(animal)
        animal.sound = SoundLoader.load('snd/' + nombre_animal + '.wav')
        animal.sound.play()

    def play_song(self, path_cancion):
        song_path = path_cancion
        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(song_path)
        if self.sound:
            self.sound.loop = True
            self.sound.play()

class Animal(Widget):

    fuente = StringProperty()
    sound = ObjectProperty(None, allownone=True)

    def callback(self):
        self.parent.remove_widget(self)
        self.sound.stop()

class AnimalesApp(App):

    TAMANO_IMAGENES = Window.width * 0.1
    VELOCIDAD_ANIMACION = 1/17
    MARGEN_ANCHO = Window.width - TAMANO_IMAGENES
    MARGEN_ALTO = Window.height - TAMANO_IMAGENES

    def build(self):
        
        return Dibujar()

if __name__ == '__main__':
    Config.set('graphics', 'fullscreen', '2')
    Config.set('graphics', 'window_state', 'maximized')
    Config.write()
    AnimalesApp().run()