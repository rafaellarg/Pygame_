# importa bibliotecas e arquivos necessários
import pygame
from pygame.locals import *
import random
from classes import Pessoa, Frutas, Bombas
from assets import load_assets
from configuracoes import GAME, largura, altura, aceleracao, min_frutas
from tela_final import tela_final
import time
from assets import audio, fundo_tela, bomba_img, audiofrutas

# Função que irá criar a tela principal de jogo
def tela_jogo(tela):
    #Iniciando o pygame
    pygame.init()

    # Definindo o tamanho da tela e seu nome
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Catch the Fruits")

    # Criando um grupo de Sprites principal
    grupo_Sprites = pygame.sprite.Group()

    # Criando grupo de Sprites para cada uma das imagens que serão desenhadas na tela
    grupo_frutas = pygame.sprite.Group()
    grupo_bombas = pygame.sprite.Group()
    # Criando uma variável da classe Pessoa
    pessoa = Pessoa()
    # Adicionado a variável no grupo de Sprites principal
    grupo_Sprites.add(pessoa)


    # Carregando a lista que contém as imagens das frutas
    lista_frutas = load_assets()

    # Iniciando a variável que mostrará a pontuação
    pontuacao = 0

    # Declarndo a fonte que será usada no texto da pontuação 
    fonte = pygame.font.Font(None, 36)

    # Criando um for que sorteia um número aleatório e o relacionado com o aparecimento de frutas ou bombas na tela
    for i in range(10):
        contador = random.randint(0, 100)
        # Caso o número for menor que 40, sorteia uma fruta
        if contador < 40:
            # Escolhendo uma imagem de fruta aleatória
            fruta = Frutas(random.choice(lista_frutas))
            # Adicionado au grupo de Sprites específico
            grupo_frutas.add(fruta)
            # Adicionando ao grupo de Sprites principal
            grupo_Sprites.add(fruta)
        # Caso o número for maior que 40, aparece uma bomba
        else:
            # Inspeciona a classe Bomba 
            bomba = Bombas(bomba_img)
            # Adiciona ao grupo de Sprites específico
            grupo_bombas.add(bomba)
            # Adiciona ao grupo de Sprites principal
            grupo_Sprites.add(bomba)

    # Define o relogio do jogo
    relogio = pygame.time.Clock()

    #Inicializa o loop principal da tela
    rodando = True
    while rodando:
        # Loop que certifica que sempre serão desenhadas novas frutas na tela
        while len(grupo_frutas) < min_frutas:
            fruta = Frutas(random.choice(lista_frutas))
            grupo_frutas.add(fruta)
            grupo_Sprites.add(fruta)

        # Define os eventos do pygame
        for event in pygame.event.get():
            # Se o evento for do tipo saiir do jogo, a tela fecha
            if event.type == QUIT:
                pygame.quit()
            # Se o evento for do tipo apertar uma tecla e essa for a tecla lateral direita, o personagem andará para a direita
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pessoa.rect.x += aceleracao
                # Se o evento for do tipo apertar uma tecla e essa for a tecla lateral esquerda, o personagem andará para a esquerda
                if event.key == pygame.K_LEFT:
                    pessoa.rect.x -= aceleracao

        # Verifica se houve colisão do personagem com bombas
        colisao_bomba = pygame.sprite.spritecollide(pessoa, grupo_bombas, True, pygame.sprite.collide_mask)
        if colisao_bomba:
            # Audio toca
            audio.play()
            som_length = audio.get_length()
            pygame.time.wait(int(som_length * 1000))
            # Jogo acaba e direciona para a tela final
            state = tela_final(tela)
            return state

        # Verifica se houve colisão com alguma fruta
        colisao_fruta = pygame.sprite.spritecollide(pessoa, grupo_frutas, True, pygame.sprite.collide_mask)
        if colisao_fruta:
            # Toca aúdio
            audiofrutas.play()
            # Pontuação aumenta um ponto
            pontuacao += 1

        # Defina a imagem como fundo da tela do jogo
        tela.blit(fundo_tela, (0, 0))

        # Atualiza os Sprites a cada tela
        grupo_Sprites.update()

        # Desenha os Sprites a cada tela
        grupo_Sprites.draw(tela)

        # Coloca a pontuação na tela
        texto_pontuacao = fonte.render(f'Pontuação: {pontuacao}', True, (255, 255,255, 255))
        tela.blit(texto_pontuacao, (10, 10))

        relogio.tick(40)

        pygame.display.update()

            
