import pygame
pygame.init()
infoPantalla = pygame.display.Info()
print (infoPantalla)
gameDisplay = pygame.display.set_mode((infoPantalla.current_w,infoPantalla.current_h),pygame.FULLSCREEN)    #,pygame.RESIZABLE ,pygame.FULLSCREEN
pygame.display.set_caption('ANIMALES QUE DESAPARECEN')