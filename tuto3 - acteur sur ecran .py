import pygame

pygame.init() # initialiser

fenetre = pygame.display.set_mode((800, 600))

execution = True



class Acteur(pygame.sprite.Sprite):
    def __init__(self):
        super(Acteur, self).__init__()
        self.surf = pygame.Surface((75,75)) # taille du rectangle de acteur
        self.surf.fill((236, 165, 22)) # coleur en rgb
        self.rect = self.surf.get_rect()


# Cree une instance de acteur
sidi = Acteur()



while execution:
    for evenement in pygame.event.get():
        if evenement.type == pygame.KEYDOWN:

            if evenement.key == pygame.K_b:
                execution = False

        elif evenement.type == pygame.QUIT:
            execution = False

    # dessiner l'acteur dans la fenetre
    fenetre.blit(sidi.surf, (300, 300))

    pygame.display.flip()