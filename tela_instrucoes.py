import pygame
from configuracoes import GAME, INSTRUCOES, QUIT, largura, altura
from jogo import tela_jogo

def tela_instrucoes(tela):

    fundo_tela = pygame.image.load('img/tela_fundo_fosca.png')
    fundo_tela = pygame.transform.scale(fundo_tela, (largura, altura))

    instrucoes = pygame.image.load('img/tela_instrucoes.png')
    instrucoes = pygame.transform.scale(instrucoes, (600, 500))


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                running = False
                state = tela_jogo(tela)

        tela.blit(fundo_tela, (0,0))

        tela.blit(instrucoes, (210, 50))
        

        pygame.display.flip()

    return state