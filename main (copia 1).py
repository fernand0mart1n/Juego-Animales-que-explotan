import os
import random

from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.app import App
from kivymd.app import MDApp

# traemos los nombres de los archivos de imagen de animales animados y los guardamos en una lista
animales = os.listdir("video")

Window.size = (1200, 700)

kv = f'''

#:import hex kivy.utils.get_color_from_hex
MDScreen:
    MDGridLayout:
        cols: 1
        Image:
            id: display_image
            source: 'video/{random.choice(animales)}'
            anim_delay: 1/20
            anim_reset: True
            size_hint_y:None
            height: 200
'''
# en esta línea de arriba seteamos como se van a ver los animales y seleccionamos uno de la lista aleatoriamente

class Animales(MDApp):
    def build(self):
        root = Builder.load_string(kv)
        self.delay = root.ids.display_image.anim_delay
        Clock.schedule_once(self.stop_anim, 45*self.delay)  # stop after 45 frames
        return root

    def stop_anim(self, dt):
        print('stopping animation')
        self.root.ids.display_image.anim_delay = -1
        Clock.schedule_once(self.restart_anim, 5)

    def restart_anim(self, dt):
        print('restarting animation')
        self.root.ids.display_image.anim_delay = self.delay

if __name__== '__main__':
    Animales().run()