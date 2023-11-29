# Importando bibliotecas e arquivos necessários
import pygame
import random
from configuracoes import largura_pessoa, altura_pessoa, aceleracao

# Classe que irá definir os atributos de movimento e aparencia do personagem na tela
class Pessoa(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/img/pessoa.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (largura_pessoa, altura_pessoa))
        self.rect = self.image.get_rect()
        self.rect.x = 380
        self.rect.y = 290
# Atualiza as caracteristicas a cada tela
    def update(self):
        if self.rect.x > 830:
            self.rect.x = 830

        elif self.rect.x < -52:
            self.rect.x = -52



# Classe que irá definir os atributos de movimento e aparencia das frutas na tela
class Frutas(pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000 - self.rect.width)  
        self.rect.y = random.randint(-self.rect.height, -10)  
        self.speed = random.randint(3, 6)  
# Atulaiza as posicoes das frutas a cada tela
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = random.randint(-self.rect.height, -10)
            self.rect.x = random.randint(0, 1000 - self.rect.width)

# Classe que irá definir os atributos de movimento e aparência das bombas na tela
class Bombas(pygame.sprite.Sprite):
    def __init__(self, imagem):
        pygame.sprite.Sprite.__init__(self)
        self.image = imagem
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1000 - self.rect.width)  
        self.rect.y = random.randint(-self.rect.height, -10)  
        self.speed = random.randint(3, 6)  
# Atulaiza as posicoes e velocidade das bombas a cada tela
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = random.randint(-self.rect.height, -10)
            self.rect.x = random.randint(0, 1000 - self.rect.width)

# Classe que define as caracteristicas de aparência dos botões na tela
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



