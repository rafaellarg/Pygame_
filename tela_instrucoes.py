# Importando bibliotecas e arquivos necessários
import pygame
from configuracoes import GAME, INSTRUCOES, QUIT, largura, altura
from jogo import tela_jogo
from assets import fundo_tela_fosca, instrucoes

# Função que irá criar a tela de instruções
def tela_instrucoes(tela):
    # Iniciando a loop principal da tela
    running = True
    while running:
        # Verifica se o evento é sair da tela, caso seja ela fecha
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Verifica se o tipo de evento é apertar uma tecla
            if event.type == pygame.KEYDOWN:
                # Caso a tecla apertada seja espaço, o jogo começa
                if event.key == pygame.K_SPACE:
                    running = False
                    state = tela_jogo(tela)
        # Define a imagem fosca como fundo de tela
        tela.blit(fundo_tela_fosca, (0,0))
        # Coloca a imagem de intruções na tela
        tela.blit(instrucoes, (210, 50))
        

        pygame.display.flip()

    return state