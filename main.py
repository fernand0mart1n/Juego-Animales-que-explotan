from time import time
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.lang import Builder
from kivy.config import Config
from time import sleep
import HoverBehavior
import random
import os

# Window.clearcolor = '#394352'                                     # lo meti en __main__

# ANIMALES = os.listdir("videoAnimales")                            # no hace falta que sea global la meti en la clase Dibujar, func __init__

class Dibujar(Widget):

    sound = ObjectProperty(None, allownone=True)

    def __init__(self, **kwargs):
        super(Dibujar, self).__init__(**kwargs)
        self.play_song('snd/musica.mp3')
        #Clock.schedule_interval(self.appear_target, 3)            # lo saqué de aca para que aprezca de una
        ANIMALES = os.listdir("videoAnimales")
        nombre_animal = random.choice(ANIMALES).split('.')[0]      
        posAnimalx,posAnimaly = (random.randint(100, int(AnimalesApp.MARGEN_ANCHO)),random.randint(100, int(AnimalesApp.MARGEN_ALTO)))
        self.appear_target(nombre_animal, posAnimalx, posAnimaly)   # mando como argumento el nombre y pos, no dejo que se calcule en la funcion


    def appear_target(self, nombre_animal, posAnimalx, posAnimaly, *args):
        animal = Animal()
        animal.fuente = 'videoAnimales/' + nombre_animal + '.zip'
        animal.posX = posAnimalx
        animal.posY = posAnimaly
        self.add_widget(animal)
        animal.sound = SoundLoader.load('snd/' + nombre_animal + '.wav')
        animal.sound.play()
    
    def appear_explosion(self, posAnimalx, posAnimaly, *args):
        animal = Animal()
        animal.fuente = 'videoExplosion/explosion.zip'
        animal.posX = posAnimalx
        animal.posY = posAnimaly
        self.add_widget(animal)
        #animal.sound = SoundLoader.load('snd/' + nombre_animal + '.wav')
        #animal.sound.play()

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
    posX = NumericProperty()
    posY = NumericProperty()
    sound = ObjectProperty(None, allownone=True)

    def callback(self,pos):
        #self.sound.stop()
        Dibujar.appear_explosion(self,pos[0],pos[1])
        #self.parent.remove_widget(self)
        

class AnimalesApp(App):

    TAMANO_IMAGENES = Window.width * 0.1
    VELOCIDAD_ANIMACION = 1/17
    MARGEN_ANCHO = Window.width - Window.width*0.15
    MARGEN_ALTO = Window.height - Window.height*0.15

    def build(self):    
        return Dibujar()

if __name__ == '__main__':
    Window.clearcolor = '#394352'
    Config.set('graphics', 'fullscreen', '2')
    Config.set('graphics', 'window_state', 'maximized')
    Config.write()
    AnimalesApp().run()