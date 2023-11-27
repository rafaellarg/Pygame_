import pygame
import random


largura_pessoa = 225
altura_pessoa = 245

aceleracao = 10

class Pessoa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/pessoa.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (largura_pessoa, altura_pessoa))
        self.rect = self.image.get_rect()
        self.rect.x = 380
        self.rect.y = 290
        print(self.rect)

    def update(self):
        if self.rect.x > 830:
            self.rect.x = 830

        elif self.rect.x < -52:
            self.rect.x = -52




class Frutas(pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000 - self.rect.width)  
        self.rect.y = random.randint(-self.rect.height, -10)  
        self.speed = random.randint(3, 6)  
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = random.randint(-self.rect.height, -10)
            self.rect.x = random.randint(0, 1000 - self.rect.width)


class Bombas(pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000 - self.rect.width)  
        self.rect.y = random.randint(-self.rect.height, -10)  
        self.speed = random.randint(3, 6)  
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = random.randint(-self.rect.height, -10)
            self.rect.x = random.randint(0, 1000 - self.rect.width)
