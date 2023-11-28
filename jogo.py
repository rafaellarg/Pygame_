import pygame
from pygame.locals import *
import random
from classes import Pessoa, Frutas, Bombas
from assets import load_assets
from configuracoes import GAME, largura, altura
from tela_final import tela_final

pygame.mixer.init()

caminho_do_arquivo = 'Audio.mp3'
som = pygame.mixer.Sound(caminho_do_arquivo)

def tela_jogo(tela):


    aceleracao = 30

    pygame.init()

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Catch the Fruits")

    fundo_tela = pygame.image.load('img/tela_fundo.png')
    fundo_tela = pygame.transform.scale(fundo_tela, (largura, altura))
    bomba_img = pygame.image.load('img/bomba.png')
    bomba_img = pygame.transform.scale(bomba_img, (60, 60))

    grupo_Sprites = pygame.sprite.Group()
    pessoa = Pessoa()
    grupo_Sprites.add(pessoa)

    grupo_frutas = pygame.sprite.Group()
    grupo_bombas = pygame.sprite.Group()

    lista_frutas = load_assets()

    # Pontuação inicial
    pontuacao = 0

    # Fonte para exibir a pontuação
    fonte = pygame.font.Font(None, 36)

    for i in range(10):
        contador = random.randint(0, 100)
        if contador < 80:
            fruta = Frutas(random.choice(lista_frutas))
            grupo_frutas.add(fruta)
            grupo_Sprites.add(fruta)
        else:
            bomba = Bombas(bomba_img)
            grupo_bombas.add(bomba)
            grupo_Sprites.add(bomba)

    relogio = pygame.time.Clock()

    # Criando o loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pessoa.rect.x += aceleracao
                if event.key == pygame.K_LEFT:
                    pessoa.rect.x -= aceleracao

        # Verificando colisão com bombas
        colisao_bomba = pygame.sprite.spritecollide(pessoa, grupo_bombas, True, pygame.sprite.collide_mask)
        if colisao_bomba:
            som.play()
            pygame.quit()
            state = tela_final(tela)
            return state

        # Verificando colisão com frutas
        colisao_fruta = pygame.sprite.spritecollide(pessoa, grupo_frutas, True, pygame.sprite.collide_mask)
        if colisao_fruta:
            pontuacao += 1

        # Adicionando a imagem no fundo
        tela.blit(fundo_tela, (0, 0))

        # Atualizando e desenhando sprites na tela
        grupo_Sprites.update()
        grupo_Sprites.draw(tela)

        # Exibindo pontuação na tela
        texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, (255, 255,255, 255))
        tela.blit(texto_pontuacao, (10, 10))

        relogio.tick(30)

        pygame.display.update()

            
