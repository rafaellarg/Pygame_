import pygame
from pygame.locals import *
import random
from classes import Pessoa, Frutas, Bombas
from assets import load_assets
from configuracoes import GAME, largura, altura, aceleracao
from tela_final import tela_final
import time
from assets import audio, fundo_tela, bomba_img

def tela_jogo(tela):

    pygame.init()

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Catch the Fruits")

    fundo_tela = pygame.image.load('assets/img/tela_fundo.png')
    fundo_tela = pygame.transform.scale(fundo_tela, (largura, altura))
    bomba_img = pygame.image.load('assets/img/bomba.png')
    bomba_img = pygame.transform.scale(bomba_img, (60, 60))

    grupo_Sprites = pygame.sprite.Group()
    pessoa = Pessoa()
    grupo_Sprites.add(pessoa)

    grupo_frutas = pygame.sprite.Group()
    grupo_bombas = pygame.sprite.Group()

    lista_frutas = load_assets()

   
    pontuacao = 0

    fonte = pygame.font.Font(None, 36)

    for i in range(10):
        contador = random.randint(0, 100)
        if contador < 70:
            fruta = Frutas(random.choice(lista_frutas))
            grupo_frutas.add(fruta)
            grupo_Sprites.add(fruta)
        else:
            bomba = Bombas(bomba_img)
            grupo_bombas.add(bomba)
            grupo_Sprites.add(bomba)

    relogio = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pessoa.rect.x += aceleracao
                if event.key == pygame.K_LEFT:
                    pessoa.rect.x -= aceleracao


        colisao_bomba = pygame.sprite.spritecollide(pessoa, grupo_bombas, True, pygame.sprite.collide_mask)
        if colisao_bomba:
            audio.play()
            som_length = audio.get_length()
            pygame.time.wait(int(som_length * 1000))
            state = tela_final(tela)
            return state


        colisao_fruta = pygame.sprite.spritecollide(pessoa, grupo_frutas, True, pygame.sprite.collide_mask)
        if colisao_fruta:
            pontuacao += 1

        tela.blit(fundo_tela, (0, 0))

        grupo_Sprites.update()
        grupo_Sprites.draw(tela)

        texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, (255, 255,255, 255))
        tela.blit(texto_pontuacao, (10, 10))

        relogio.tick(30)

        pygame.display.update()

            
