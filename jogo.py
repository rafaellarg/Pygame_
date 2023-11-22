import pygame
from pygame.locals import *

largura = 800
altura = 600

pygame.init()

tela = pygame.display.set_mode((largura, altura))

fundo_tela = pygame.image.load('img/tela_fundo.jpeg')
fundo_tela = pygame.transform.scale(fundo_tela, (largura,altura))
pessoa = pygame.image.load('img/pessoa.jpg').convert_alpha()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    tela.blit(fundo_tela, (0,0))

    pygame.display.update()