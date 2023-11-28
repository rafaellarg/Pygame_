import pygame
from configuracoes import GAME, INSTRUCOES, QUIT, largura, altura

def tela_instrucoes(screen):
    clock = pygame.time.Clock()

    GREEN = (0, 153, 51)
    
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(60)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYDOWN:
                state = GAME
                running = False

            

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(GREEN)
        

        pygame.display.flip()

    return state
