import pygame
from configuracoes import GAME, INIT, INSTRUCOES, largura, altura
from tela_instrucoes import tela_instrucoes
from jogo import tela_jogo

def tela_inicio(tela):
    state = INIT

    tela_inicio = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Catch the Fruits")

    fundo_tela = pygame.image.load('assets/img/tela_fundo_fosca.png')
    fundo_tela = pygame.transform.scale(fundo_tela, (largura, altura))
    jogar_claro = pygame.image.load('assets/img/jogar_claro.png').convert_alpha()
    regras_claro = pygame.image.load('assets/img/regras_claro.png').convert_alpha()
    titulo = pygame.image.load('assets/img/titulo.png').convert_alpha()

    jogar_escuro = pygame.image.load('assets/img/jogar_escuro.png').convert_alpha()
    regras_escuro = pygame.image.load('assets/img/regras_escuro.png').convert_alpha()

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


        tela.blit(fundo_tela, (0, 0))
        tela.blit(titulo, (300, 500))

        grupo_botoes = pygame.sprite.Group()
        grupo_botoes.add(botao_jogar)
        grupo_botoes.add(botao_regras)
        grupo_botoes.draw(tela)

        relogio.tick(30)
        pygame.display.update()

    return state
