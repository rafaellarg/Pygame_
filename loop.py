# Importa bibliotecas e arquivos necessários
import pygame   
import random
from tela_inicio import tela_inicio
from jogo import tela_jogo
from tela_final import tela_final
from tela_instrucoes import tela_instrucoes
from configuracoes import INIT, GAME, QUIT, GAME_OVER, INSTRUCOES

# Inicializa o pygame
pygame.init()

# Cria a janela, seu tamanho e nome
janela = pygame.display.set_mode((600, 1000))
pygame.display.set_caption('Catch the Fruits')

# Define os estados de jogo e mudança de tela
state = INIT
while state != QUIT:
    if state == INIT:
        state = tela_inicio(janela)
    elif state == INSTRUCOES:
        state = tela_instrucoes(janela) 
    elif state == GAME:
        state = tela_jogo(janela)
    elif state == GAME_OVER:
        state = tela_final(janela)