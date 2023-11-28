import pygame
from configuracoes import GAME, INSTRUCOES, QUIT, largura, altura
from jogo import tela_jogo

def tela_instrucoes(tela):
    clock = pygame.time.Clock()

    GREEN = (0, 153, 51)
    
    running = True
    while running:
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                running = False
                state = QUIT

            if event.type == pygame.KEYDOWN:
                running = False
                state = tela_jogo(tela)

        tela.fill(GREEN)
        

        pygame.display.flip()

    return state
