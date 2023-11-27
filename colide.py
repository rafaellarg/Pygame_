import pygame
lista_frutas = [
    pygame.image.load("img/abacaxi.png").convert_alpha(),
    pygame.image.load("img/amora.png").convert_alpha(),
    pygame.image.load("img/banana.png").convert_alpha(),
    pygame.image.load("img/cereja.png").convert_alpha(),
    pygame.image.load("img/laranja.png").convert_alpha(),
    pygame.image.load("img/maca.png").convert_alpha(),
    pygame.image.load("img/melancia.png").convert_alpha(),
    pygame.image.load("img/morango.png").convert_alpha(),
    pygame.image.load("img/pera.png").convert_alpha(),
    pygame.image.load("img/uva.png").convert_alpha()
]

lista_bombas = [
    pygame.image.load("img/bomba 2.png").convert_alpha(),
    pygame.image.load("img/bomba 3.png").convert_alpha(),
    pygame.image.load("img/bomba 4.png").convert_alpha(),
    pygame.image.load("img/bomba.png").convert_alpha()

]
score = 0

for fruit in lista_frutas[:]:
        if fruit.colliderect(Pessoa):
            lista_frutas.remove(fruit)
            score += 1

for bomb in lista_bombas[:]:
    if bomb.colliderect(Pessoa):
        lista_bombas.remove(bomb)
        # Encerra o jogo
        pygame.quit()
        running = False

