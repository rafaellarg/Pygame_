import pygame
from configuracoes import GAME, INSTRUCOES, QUIT, largura, altura
from jogo import tela_jogo
from assets import fundo_tela_fosca, instrucoes

def tela_instrucoes(tela):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                running = False
                state = tela_jogo(tela)

        tela.blit(fundo_tela_fosca, (0,0))

        tela.blit(instrucoes, (210, 50))
        

        pygame.display.flip()

    return state