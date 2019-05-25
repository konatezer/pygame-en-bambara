import pygame, random

pygame.init() # initialiser

fenetre = pygame.display.set_mode((800, 600))

fond_ecran = pygame.image.load("img/bg1.jpg")

execution = True

clock = pygame.time.Clock()


class Acteur(pygame.sprite.Sprite):
    def __init__(self):
        super(Acteur, self).__init__()
        self.surf = pygame.Surface((75,75)) # taille du rectangle de acteur
        self.surf.fill((255, 255, 255)) # coleur en rgb
        self.rect = self.surf.get_rect()

    def update(self, boutton_appyer):
        if boutton_appyer[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if boutton_appyer[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if boutton_appyer[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
        if boutton_appyer[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)


        # maintenir acteur dans ecran
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right >800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >600:
            self.rect.bottom = 600

class Bandit(pygame.sprite.Sprite):
    def __init__(self):
        super(Bandit, self).__init__()
        self.surf = pygame.Surface((30,15)) # taille du rectangle de acteur
        self.surf.fill((255, 0, 0)) # coleur en rgb
        self.rect = self.surf.get_rect(center=(820, random.randint(0, 600)))
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0: #si le cote droite du retangle de bandit est hors de ecran
            self.kill()


# Cree une instance de acteur
sidi = Acteur()

#cree une instance de bandit
bandit_sidi = Bandit()



while execution:
    for evenement in pygame.event.get():
        if evenement.type == pygame.KEYDOWN:

            if evenement.key == pygame.K_b:
                execution = False

        elif evenement.type == pygame.QUIT:
            execution = False

    boutton_appuyer = pygame.key.get_pressed() # determiner quelle bouton a ete appuyer
    sidi.update(boutton_appuyer)

    bandit_sidi.update()

    fenetre.blit(fond_ecran, (0, 0))

    # dessiner l'acteur dans la fenetre
    fenetre.blit(bandit_sidi.surf, bandit_sidi.rect)
    fenetre.blit(sidi.surf, sidi.rect) # acteur sidi



    pygame.display.flip()
    clock.tick(60)