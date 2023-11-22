import pygame


class Pessoa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


        self.image = pygame.image.load("img/pessoa.jpg").convert_alpha()
        self.rect = self.image.get_rect()
        print(self.rect)

    def update():
        pass
