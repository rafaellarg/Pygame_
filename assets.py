import pygame 
from os import path
import os

def load_assets():
    nomes = [
        'melancia', 'abacaxi', 'amora', 'banana',
        'cereja', 'morango', 'maca', 'pera', 'uva'
    ]
    lista = []
    for nome in nomes:
        fruta  =  pygame.image.load(f"assets/img/img_frutas/{nome}.png").convert_alpha()
        fruta = pygame.transform.scale(fruta,(70,70))
        lista.append(fruta)
    return lista

pygame.mixer.init()

SND_DIR = path.join(path.dirname(__file__), 'assets', 'audios')
audio = pygame.mixer.Sound(os.path.join(SND_DIR, 'audio2.mp3'))

