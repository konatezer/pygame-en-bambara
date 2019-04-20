import pygame

pygame.init() # initialiser

fenetre = pygame.display.set_mode((800, 600))

execution = True

while execution:
    for evenement in pygame.event.get():
        if evenement.type == pygame.KEYDOWN:

            if evenement.key == pygame.K_b:
                execution = False

        elif evenement.type == pygame.QUIT:
            execution = False

    pygame.display.flip()