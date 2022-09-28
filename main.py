# para compiliar .exe lo anoto ya que encontre como hacia:
# pip install pyinstaller
# pyinstaller --onefile <your_script_name>.py
# ojo que no copia las carpetas con otros archivos, mover manualmente a "dist"

import pygame
import random
from pygame import mixer
from sprite import Sprite

pygame.init()

infoPantalla = pygame.display.Info()
gameDisplay = pygame.display.set_mode((infoPantalla.current_w,infoPantalla.current_h),pygame.FULLSCREEN)    
#,pygame.RESIZABLE ,pygame.FULLSCREEN

mixer.init()
mixer.music.load('snd/musica.mp3')
mixer.music.play()

TITULO = 'ANIMALES QUE DESAPARECEN'
corriendo = True
perro=Sprite("img/perro_sprite.png","snd/perro.wav",400,9)
oveja=Sprite("img/oveja_sprite.png","snd/oveja.wav",400,9)
leon=Sprite("img/leon_sprite.png","snd/leon.wav",400,9)
gato=Sprite("img/gato_sprite.png","snd/gato.wav",400,9)
gallina=Sprite("img/gallina_sprite.png","snd/gallo.wav",400,9)
elefante=Sprite("img/elefante_sprite.png","snd/elefante.wav",400,9)
explosion=Sprite("img/explosion_sprite.png","snd/explosion.wav",400,10)
animales = (perro,oveja,leon,gallina,gato,elefante)

# FER: AL FINAL PASA TODO DENTRO DE ESTA CLASE, ME PARECE QUE ES AL PEDO QUE ESTÉ, HACE QUE TODAS LAS VARIABLES TENGAN "self."
# Y ES MUY FEO LEERLO, QUIZA LO MEJOR EN ESTE CASO SACAR TODO FUERA Y USAR VARIABLES GLOBALES O PASAR PARAMETROS A LAS 
# FUNCIONES
#       SI USAS GLOBALES ACORDATE QUE PYTHON LEE LAS GLOBALES DENTRO DE UNA FUNCIÓN PERO PARA ESCRIBIRLAS HAY QUE 
# DECLARLAS DENTRO COMO "Global nombreVariable"
class Juego:
    def __init__(self):
        self.indexAnimal = 0
        self.spriteActual = animales[self.indexAnimal]
        self.frameActual=0
        self.boundingBox = pygame.Rect(0,0, self.spriteActual.anchoFrame, self.spriteActual.alto)
        self.boundingBox.topleft = (self.spriteActual.posX,self.spriteActual.posY)
        self.explotando = False
        fuenteArial = pygame.font.SysFont('Arial', 15)
        self.txtEscape = fuenteArial.render('presionar ESCAPE para salir', True, (150, 150, 150))

    def eventos_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global corriendo 
                corriendo = False
                break
            if event.type == pygame.KEYDOWN:
                if  pygame.key.name(event.key) == "escape":
                    corriendo = False
                    pygame.quit()
                    quit()
                    break

    def huvoColision(self):
        pygame.mouse.set_pos(0,0)
        self.spriteActual.playSND(False)                    # para sonido explosion si no termino
        if self.indexAnimal < len(animales)-1:
            self.indexAnimal += 1
        else: 
            self.indexAnimal = 0
        self.spriteActual = animales[self.indexAnimal]
        self.spriteActual.posX = random.randint(0,infoPantalla.current_w-self.spriteActual.anchoFrame)
        self.spriteActual.posY = random.randint(0,infoPantalla.current_h-self.spriteActual.alto)
        explosion.posY = self.spriteActual.posY
        explosion.posX = self.spriteActual.posX
        self.boundingBox.topleft = (self.spriteActual.posX,self.spriteActual.posY)
        
    
    def logica_loop(self):      
        colision = self.boundingBox.collidepoint(pygame.mouse.get_pos())
        if colision and not self.explotando: 
            self.spriteActual.playSND(False)                  # para sonido animal
            self.explotando= True
            self.spriteActual = explosion
            self.frameActual = 0

    def render_loop(self):
        gameDisplay.fill((57,67,82))
        if self.frameActual < self.spriteActual.cantFrames-1:
            self.frameActual +=1
        else:
            self.frameActual = 0
            if self.explotando:                                            # si terminó de reproducir el sprite de explosion..
                self.explotando= False
                self.huvoColision()
        self.spriteActual.mostrar(self.spriteActual.posX, self.spriteActual.posY, self.frameActual)
        self.spriteActual.playSND(True)
        pygame.draw.rect(gameDisplay, (200,200,200,50), self.boundingBox,1)  #si necesitamos ver el boundigbox
        gameDisplay.blit (self.txtEscape,(infoPantalla.current_w/2-self.txtEscape.get_size()[0]/2,infoPantalla.current_h-30))  
        # muestra texto Esc
        pygame.display.update()

    def ejecutar(self):
        while corriendo:
            self.eventos_loop()
            self.logica_loop()
            self.render_loop()  
            clock.tick(10)

# TAMPOCO ME PARECE QUE SE JUSTIFICA ESTO PARA LO QUE QUEDO ACÁ, ME PARECE QUE TODO EL PROGRAMA QUEDARIA MAS CLARO COMO 
# UN EN ESTE CASO SCRIPT

if __name__ == "__main__" :
    clock = pygame.time.Clock()
    print (infoPantalla)
    pygame.display.set_caption(TITULO)
    miJuego = Juego()
    miJuego.ejecutar()
    pygame.quit()
    quit()