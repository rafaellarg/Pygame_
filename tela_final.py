import pygame
from configuracoes import GAME, INIT, largura, altura


def tela_final(tela): 

    tela_final = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Catch the Fruits")

    fundo_tela = pygame.image.load('assets/img/tela_fundo_fosca.png')
    fundo_tela = pygame.transform.scale(fundo_tela, (largura, altura))
    quit_claro = pygame.image.load('assets/img/quit_claro.png').convert_alpha()
    quit_claro = pygame.image.load('assets/img/quit_claro.png').convert_alpha()

    quit_escuro = pygame.image.load('assets/img/quit_escuro.png').convert_alpha()
    reset_escuro = pygame.image.load('assets/img/reset_escuro.png').convert_alpha()
    reset_claro = pygame.image.load('assets/img/reset_claro.png').convert_alpha()

    titulo = pygame.image.load('assets/img/titulo.png').convert_alpha()
    titulo = pygame.transform.scale(titulo, (650, 400))


    class Botao(pygame.sprite.Sprite):
        def __init__(self, x, y, imagem, escala):
            pygame.sprite.Sprite.__init__(self)
            largura = imagem.get_width()
            altura = imagem.get_height()
            nova_largura = int(largura * escala)
            nova_altura = int(altura * escala)
            self.image = pygame.transform.scale(imagem, (nova_largura, nova_altura))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)

    botao_quit = Botao(320, 689, quit_claro, 6)
    botao_reset = Botao(900, 710, reset_claro, 6)

    relogio = pygame.time.Clock()

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


        tela.blit(fundo_tela, (0, 0))
        tela.blit(titulo, (350, 50))
        grupo_botoes = pygame.sprite.Group()
        grupo_botoes.add(botao_quit)
        grupo_botoes.add(botao_reset)
        grupo_botoes.draw(tela)

        relogio.tick(30)
        pygame.display.update()

    return state
