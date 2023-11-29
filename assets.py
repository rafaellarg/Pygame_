# Importando bibliotecas e arquivos necessários
import pygame 
from os import path
import os
from configuracoes import largura, altura

# Funcao que carrega as imagens de frutas
def load_assets():
    nomes = [
        'melancia', 'abacaxi', 'amora', 'banana',
        'cereja', 'morango', 'maca', 'pera', 'uva'
    ]
    lista = []
    for nome in nomes:
        fruta  =  pygame.image.load(f"assets/img/img_frutas/{nome}.png")
        fruta = pygame.transform.scale(fruta,(70,70))
        lista.append(fruta)
    return lista

pygame.mixer.init()

# Carregando as imagens que serão utilizadas no jogo ao longo das telas
fundo_tela = pygame.image.load('assets/img/tela_fundo.png')
fundo_tela = pygame.transform.scale(fundo_tela, (largura, altura))
bomba_img = pygame.image.load('assets/img/bomba.png')
bomba_img = pygame.transform.scale(bomba_img, (60, 60))


fundo_tela_fosca = pygame.image.load('assets/img/tela_fundo_fosca.png')
fundo_tela_fosca = pygame.transform.scale(fundo_tela_fosca, (largura, altura))

quit_claro = pygame.image.load('assets/img/quit_claro.png')
quit_claro = pygame.image.load('assets/img/quit_claro.png')
quit_escuro = pygame.image.load('assets/img/quit_escuro.png')

jogar_claro = pygame.image.load('assets/img/jogar_claro.png')
jogar_escuro = pygame.image.load('assets/img/jogar_escuro.png')


regras_claro = pygame.image.load('assets/img/regras_claro.png')
regras_escuro = pygame.image.load('assets/img/regras_escuro.png')


reset_escuro = pygame.image.load('assets/img/reset_escuro.png')
reset_claro = pygame.image.load('assets/img/reset_claro.png')

titulo = pygame.image.load('assets/img/titulo.png')
titulo = pygame.transform.scale(titulo, (650, 400))

instrucoes = pygame.image.load('assets/img/tela_instrucoes.png')
instrucoes = pygame.transform.scale(instrucoes, (600, 500))




SND_DIR = path.join(path.dirname(__file__), 'assets', 'audios')
audio = pygame.mixer.Sound(os.path.join(SND_DIR, 'audio2.mp3'))

