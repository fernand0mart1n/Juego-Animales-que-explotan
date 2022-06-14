import os
import random

from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image
from kivy.app import App
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.lang import Builder

animales = os.listdir("video")

a = Builder.load_string('''
<BattleField>
    BoxLayout:
        orientation: 'vertical'

<Target>
    canvas:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'video/'+random.choice(animales)   

''')

class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)
        self.root = RelativeLayout()
        Window.size = (1200, 700)

        def appear_target(self, *args):
            random_pos = tuple([random.randint(200, 800) for i in range(2)])
            target = Target()
            target.pos = random_pos
            self.add_widget(target)

        animales = os.listdir("video")

        #animated_icon = Image(source='video/'+random.choice(animales))
        #animated_icon.bind(texture=self.update_texture)
        
        #Clock.schedule_interval(animated_icon.on_touch_down, 0.01)

        posicion = [(200, 150), (800, 150), (200, 350), (800, 350)]
        
        #self.r = Rectangle(texture=animated_icon.texture, size=(250, 250), pos=appear_target(self))
        #Clock.schedule_interval(self.r.appear_target, 1)
        #self.root.canvas.add(self.r)

    #def update_texture(self, instance, value):
    #    self.r.texture = value

    def build(self):
        return self.root

    class Target(Widget):

        def on_touch_down(self, touch):
            if self.collide_point(*touch.pos):
                self.parent.remove_widget(self)


if __name__ == '__main__':
    MainApp().run()