import pygame
from configuracoes import GAME, INSTRUCOES

def tela_final(screen):
    largura = 1000
    altura = 600

    tela_inicio = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Catch the Fruits")

    fundo_tela = pygame.image.load('img/tela_fundo_fosca.png')
    fundo_tela = pygame.transform.scale(fundo_tela, (largura, altura))
    jogar_claro = pygame.image.load('img/jogar_claro.png').convert_alpha()
    regras_claro = pygame.image.load('img/regras_claro.png').convert_alpha()

    jogar_escuro = pygame.image.load('img/jogar_escuro.png').convert_alpha()
    regras_escuro = pygame.image.load('img/regras_escuro.png').convert_alpha()


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

        def desenha(self):
            tela_inicio.blit(self.image, self.rect.topleft)


    botao_jogar = Botao(450, 430, jogar_claro, 6)
    botao_regras = Botao(900, 430, regras_claro, 6)

    grupo_botoes = pygame.sprite.Group()
    grupo_botoes.add(botao_jogar)
    grupo_botoes.add(botao_regras)

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_jogar.rect.collidepoint(event.pos):
                    rodando = False
                    state = GAME
                elif botao_regras.rect.collidepoint(event.pos):
                    # state = INSTRUCOES
                    rodando = False

        tela_inicio.blit(fundo_tela, (0, 0))

        grupo_botoes.draw(tela_inicio)

        pygame.display.update()

    pygame.quit()

    return state