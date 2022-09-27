# para compiliar .exe lo anoto ya que encontre como hacia:
# pip install pyinstaller
# pyinstaller --onefile <your_script_name>.py
# ojo que no copia las carpetas con otros archivos, mover manualmente a "dist"

import pygame
from config import * # FER: SACAR LO QUE HAY AHI Y PONERLO EN ESTE MOODULO MAIN PORQUE LO QUE QUEDO ES UN CHISTE
import random

pygame.init()


# FER: QUIZA QUEDE MEJOR PASAR ESTA CLASE A OTRO ARCHIVO (MODULO)
class Sprite_animado:

    def __init__(self,archivoIMG, archivoSND,anchoFrame,cantFrames): 
        # archivoIMG = ruta del sprite o tira de frames
        # archivoSND = ruta del archivo de audio
        #a nchoFrame = ancho de un frame
        # cantFrame = cuantos frames tiene la tira
        self.imagen = pygame.image.load(archivoIMG).convert_alpha()
        self.ancho, self.alto = self.imagen.get_size()
        self.anchoFrame = anchoFrame
        self.cantFrames = cantFrames
        self.sonido = pygame.mixer.Sound(archivoSND)
        self.posX , self.posY = (300,300)
    
    def mostrar(self,x,y,frame): 
        gameDisplay.blit(self.imagen, (x,y),(self.anchoFrame*frame,0,self.anchoFrame,self.alto))   #el ultimo parentisis es el recorte x_inicial,y_inicial,ancho,alto
	
    def playSND (self,reproducir):
        if not pygame.mixer.get_busy() and reproducir:
            self.sonido.play()
        elif pygame.mixer.get_busy() and not reproducir:
            self.sonido.fadeout(300)

# FER: AL FINAL PASA TODO DENTRO DE ESTA CLASE, ME PARECE QUE ES AL PEDO QUE ESTÉ, HACE QUE TODAS LAS VARIABLES TENGAN "self."
#       Y ES MUY FEO LEERLO, QUIZA LO MEJOR EN ESTE CASO SACAR TODO FUERA Y USAR VARIABLES GLOBALES O PASAR PARAMETROS A LAS FUNCIONES
#       SI USAS GLOBALES ACORDATE QUE PYTHON LEE LAS GLOBALES DENTRO DE UNA FUNCIÓN PERO PARA ESCRIBIRLAS HAY QUE DECLARLAS DENTRO COMO "Global nombreVariable"
class Juego:
    def __init__(self):
        self.corriendo = True
        self.perro=Sprite_animado("img/perro_sprite.png","snd/perro.wav",400,9)
        self.oveja=Sprite_animado("img/oveja_sprite.png","snd/oveja.wav",400,9)
        self.leon=Sprite_animado("img/leon_sprite.png","snd/leon.wav",400,9)
        self.gato=Sprite_animado("img/gato_sprite.png","snd/gato.wav",400,9)
        self.gallina=Sprite_animado("img/gallina_sprite.png","snd/gallo.wav",400,9)
        self.elefante=Sprite_animado("img/elefante_sprite.png","snd/elefante.wav",400,9)
        self.explosion=Sprite_animado("img/explosion_sprite.png","snd/explosion.wav",400,10)
        self.animales = (self.perro,self.oveja,self.leon,self.gallina,self.elefante)
        self.indexAnimal = 0
        self.spriteActual = self.animales[self.indexAnimal]
        self.frameActual=0
        self.boundingBox = pygame.Rect(0,0, self.spriteActual.anchoFrame, self.spriteActual.alto)
        self.boundingBox.topleft = (self.spriteActual.posX,self.spriteActual.posY)
        self.explotando = False
        fuenteArial = pygame.font.SysFont('Arial', 15)
        self.txtEscape = fuenteArial.render('presionar ESCAPE para salir', True, (150, 150, 150))

    def eventos_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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
        if self.indexAnimal < len(self.animales)-1:
            self.indexAnimal += 1
        else: 
            self.indexAnimal = 0
        self.spriteActual = self.animales[self.indexAnimal]
        self.spriteActual.posX = random.randint(0,infoPantalla.current_w-self.spriteActual.anchoFrame)
        self.spriteActual.posY = random.randint(0,infoPantalla.current_h-self.spriteActual.alto)
        self.explosion.posY = self.spriteActual.posY
        self.explosion.posX = self.spriteActual.posX
        self.boundingBox.topleft = (self.spriteActual.posX,self.spriteActual.posY)
        
    
    def logica_loop(self):      
        colision = self.boundingBox.collidepoint(pygame.mouse.get_pos())
        if colision and not self.explotando: 
            self.spriteActual.playSND(False)                  # para sonido animal
            self.explotando= True
            self.spriteActual = self.explosion
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
        gameDisplay.blit (self.txtEscape,(infoPantalla.current_w/2-self.txtEscape.get_size()[0]/2,infoPantalla.current_h-30))  # muestra texto Esc
        pygame.display.update()

    def ejecutar(self):
        while self.corriendo:
            self.eventos_loop()
            self.logica_loop()
            self.render_loop()  
            clock.tick(10)

# TAMPOCO ME PARECE QUE SE JUSTIFICA ESTO PARA LO QUE QUEDO ACÁ, ME PARECE QUE TODO EL PROGRAMA QUEDARIA MAS CLARO COMO UN EN ESTE CASO SCRIPT

if __name__ == "__main__" :
    clock = pygame.time.Clock()
    infoPantalla = pygame.display.Info()
    print (infoPantalla)
    gameDisplay = pygame.display.set_mode((infoPantalla.current_w,infoPantalla.current_h),pygame.FULLSCREEN)    #,pygame.RESIZABLE ,pygame.FULLSCREEN
    pygame.display.set_caption(TITULO)
    miJuego = Juego()
    miJuego.ejecutar()
    pygame.quit()
    quit()