# Importa bibliotecas e arquivos necessários
import pygame
from configuracoes import GAME, INIT, largura, altura
from assets import fundo_tela_fosca, quit_claro, quit_escuro, reset_escuro, reset_claro, titulo
from classes import Botao

# Função que irá criar a tela final
def tela_final(tela): 

    tela_final = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Catch the Fruits")

    # Cria dois botões, de quit e reset inspecionando a classe Botao
    botao_quit = Botao(320, 689, quit_claro, 6)
    botao_reset = Botao(900, 710, reset_claro, 6)

    # Define o relógio do jogo
    relogio = pygame.time.Clock()

    #Inicializa o loop principal da tela
    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_quit.rect.collidepoint(event.pos):
                    botao_quit.imagem = quit_escuro
                    state = pygame.quit()
                    rodando = False
                if botao_reset.rect.collidepoint(event.pos):
                    botao_reset.imagem = reset_escuro
                    rodando = False
                    state = GAME

        # Define a imagem fosca como fundo de tela
        tela.blit(fundo_tela_fosca, (0, 0))
        # Coloca a iamgem do título na tela
        tela.blit(titulo, (350, 50))
        # Adiciona os botões ao grupo de Sprites
        grupo_botoes = pygame.sprite.Group()
        grupo_botoes.add(botao_quit)
        grupo_botoes.add(botao_reset)
        # Desenha os botões na tela
        grupo_botoes.draw(tela)

        relogio.tick(40)
        pygame.display.update()

    return state
