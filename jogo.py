import pygame
from pygame.locals import *
import random
from classes import Pessoa, Frutas, Bombas
from assets import load_assets

largura = 1000
altura = 600

aceleracao = 30

pygame.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Catch the fruits")

fundo_tela = pygame.image.load('img/tela_fundo.jpg')
fundo_tela = pygame.transform.scale(fundo_tela, (largura,altura))
bomba_img = pygame.image.load('img/bomba.png')
bomba_img = pygame.transform.scale(bomba_img, (60,60))

grupo_Sprites = pygame.sprite.Group()
pessoa = Pessoa()
grupo_Sprites.add(pessoa)

grupo_frutas = pygame.sprite.Group()


grupo_bombas = pygame.sprite.Group()

lista_frutas = load_assets()

for i in range(10):
    contador = random.randint(0,100)
    if contador < 80:
        frutas = Frutas(random.choice(lista_frutas))
        grupo_frutas.add(frutas)
        grupo_Sprites.add(frutas)

    else:
        bomba = Bombas(bomba_img)
        grupo_bombas.add(bomba)
        grupo_Sprites.add(bomba)






relogio = pygame.time.Clock()

# Criando o loop principal do jogo
while True:
    # Caso o evento seja do tipo QUIT a janela fecha
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                pessoa.rect.x += aceleracao
            if event.key == pygame.K_LEFT:
                pessoa.rect.x -= aceleracao

    # Adicionando a imagem no fundo
    tela.blit(fundo_tela, (0,0))

    grupo_Sprites.update()
    grupo_Sprites.draw(tela)

    relogio.tick(30)

    pygame.display.update()





