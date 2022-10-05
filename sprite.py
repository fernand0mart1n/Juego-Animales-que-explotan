import pygame
from globales import infoPantalla, gameDisplay
pygame.init()

class Sprite:
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
        global gameDisplay
        #infoPantalla = pygame.display.Info()  
        #gameDisplay = pygame.display.set_mode((infoPantalla.current_w,infoPantalla.current_h),pygame.FULLSCREEN) 
        gameDisplay.blit(self.imagen, (x,y),(self.anchoFrame*frame,0,self.anchoFrame,self.alto))   #el ultimo parentisis es el recorte x_inicial,y_inicial,ancho,alto
	
    def playSND (self,reproducir):
        if not pygame.mixer.get_busy() and reproducir:
            self.sonido.play()
        elif pygame.mixer.get_busy() and not reproducir:
            self.sonido.fadeout(300)

