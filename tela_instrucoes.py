import pygame
from configuracoes import GAME, INSTRUCOES, largura, altura

def tela_instrucoes(tela):
    state = INSTRUCOES

    fundo_tela = pygame.image.load('img/tela_fundo_fosca.png')
    fundo_tela = pygame.transform.scale(fundo_tela, (largura, altura))
    jogar_claro = pygame.image.load('img/jogar_claro.png').convert_alpha()

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
    grupo_botoes = pygame.sprite.Group()
    grupo_botoes.add(botao_jogar)

    rodando = True
    while rodando:
        tela.blit(fundo_tela, (0, 0))
        grupo_botoes.draw(tela)
        pygame.display.update()
    
    return state

pygame.quit()