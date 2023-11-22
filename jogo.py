import pygame
from pygame.locals import *
from classes import Pessoa

largura = 1000
altura = 600

aceleracao = 30

pygame.init()

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Catch the fruits")

fundo_tela = pygame.image.load('img/tela_fundo.jpg')
fundo_tela = pygame.transform.scale(fundo_tela, (largura,altura))


grupo_pessoa = pygame.sprite.Group()
pessoa = Pessoa()
grupo_pessoa.add(pessoa)

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

    grupo_pessoa.update()
    grupo_pessoa.draw(tela)

    relogio.tick(30)

    pygame.display.update()