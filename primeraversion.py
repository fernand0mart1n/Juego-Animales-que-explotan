import os
import random

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.app import App
from kivy.properties import (
    ReferenceListProperty, ObjectProperty, BooleanProperty
)
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.graphics import Color, Rectangle

# traemos los nombres de los archivos de imagen de animales animados y los guardamos en una lista
animales = os.listdir("video")

Window.size = (1200, 700)
 

class Animacion(Widget):
    pass
    """
    desaparece = BooleanProperty(True)
    anim_delay: 1/20
    delay: 1/20

    def animar(self, touch):
        if self.collide_widget(touch) and self.desaparece:
            self.desaparece = False
        elif not self.collide_widget(touch) and not self.desaparece:
            self.desaparece = True
    """
class AnimalesApp(App):
    def build(self):
        main = Animacion()
        #Clock.schedule_once(self.stop_anim, 45*main.delay)  # stop after 45 frames
        return main

    def stop_anim(self, dt):
        print('stopping animation')
        self.root.ids.display_image.anim_delay = -1
        Clock.schedule_once(self.restart_anim, 5)

    def restart_anim(self, dt):
        print('restarting animation')
        self.root.ids.display_image.anim_delay = self.delay

if __name__== '__main__':
    AnimalesApp().run()