import pygame
import random
import os


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



image_dir = "img/img_frutas"


class Frutas(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        image_file = [f for f in os.listdir(image_dir) if f.endswith(('.png'))]
        image_file = random.choice(image_file)
        caminho_imagem = os.path.join(image_dir, image_file)
        self.image = pygame.image.load(caminho_imagem).convert()
        self.image = pygame.transform.scale(self.image, (80,60)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000 - self.rect.width)  
        self.rect.y = random.randint(-self.rect.height, -10)  
        self.speed = random.randint(2, 5)  
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = random.randint(-self.rect.height, -10)
            self.rect.x = random.randint(0, 1000 - self.rect.width)

