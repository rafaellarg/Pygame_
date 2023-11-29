import pygame
from configuracoes import GAME, INIT, INSTRUCOES, largura, altura
from tela_instrucoes import tela_instrucoes
from jogo import tela_jogo
from classes import Botao
from assets import fundo_tela_fosca, jogar_claro, regras_claro, titulo

def tela_inicio(tela):
    state = INIT

    tela_inicio = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Catch the Fruits")

    botao_jogar = Botao(450, 430, jogar_claro, 6)
    botao_regras = Botao(900, 430, regras_claro, 6)

    relogio = pygame.time.Clock()

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_regras.rect.collidepoint(event.pos):
                    rodando = False
                    state = tela_instrucoes(tela)
                if botao_jogar.rect.collidepoint(event.pos):
                    rodando = False
                    state = tela_jogo(tela)


        tela.blit(fundo_tela_fosca, (0, 0))
        tela.blit(titulo, (350, 50))

        grupo_botoes = pygame.sprite.Group()
        grupo_botoes.add(botao_jogar)
        grupo_botoes.add(botao_regras)
        grupo_botoes.draw(tela)

        relogio.tick(40)
        pygame.display.update()

    return state
