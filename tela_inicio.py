# Importa bibliotecas e arquivos necessários
import pygame
from configuracoes import GAME, INIT, INSTRUCOES, largura, altura
from tela_instrucoes import tela_instrucoes
from jogo import tela_jogo
from classes import Botao
from assets import fundo_tela_fosca, jogar_claro, regras_claro, titulo

# Função que irá criar a tela inicial
def tela_inicio(tela):
    # Definindo o estado da tela
    state = INIT

    # Criando a jeanela da tela, e definindo seu tamanho e nome
    tela_inicio = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Catch the Fruits")

    # Criando botões de jogar e regras, inspecionando a classe Botao
    botao_jogar = Botao(450, 430, jogar_claro, 6)
    botao_regras = Botao(900, 430, regras_claro, 6)

    # Definindo o relógio do jogo
    relogio = pygame.time.Clock()

    # Criando o loop principal da tela
    rodando = True
    while rodando:
        # Definindo os eventos do pygame
        for event in pygame.event.get():
            # Verificase o evento é sair da tela, caso seja ela fecha
            if event.type == pygame.QUIT:
                pygame.quit()
            # Caso clique no botão regras, é direcionado para a tela de instruções
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_regras.rect.collidepoint(event.pos):
                    rodando = False
                    state = tela_instrucoes(tela)
                # Caso clique no botão jogar, o jogo começa
                if botao_jogar.rect.collidepoint(event.pos):
                    rodando = False
                    state = tela_jogo(tela)

        # Definindo a imagem fosca como fundo de tela
        tela.blit(fundo_tela_fosca, (0, 0))
        tela.blit(titulo, (350, 50))

        # Criando grupo de Sprites
        grupo_botoes = pygame.sprite.Group()
        #Adicionado os botões ao grupo de Sprites
        grupo_botoes.add(botao_jogar)
        grupo_botoes.add(botao_regras)
        # Desenhando os Sprites na tela
        grupo_botoes.draw(tela)

        relogio.tick(40)
        pygame.display.update()

    return state
