import pygame 

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

