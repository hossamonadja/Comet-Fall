import pygame
from comet import comet

# creer une classe pour gerer cet evenement
class cometFALLEvent:

    # lors du chargement on va creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        # definir un groupe de sprite pour stocker les cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        for i in range(1, 10):
            # apparaitre 1 premiere boule de feu
            self.all_comets.add(comet(self))
    def attempt_fall(self):
        # la jauge d'evenement totalement charger
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de cometes !!")
            self.meteor_fall()
            self.fall_mode = True # activer l'evenement

    def update_bar(self, surface):

        # ajouter du pourcentage a la barre
        self.add_percent()

        # barre noir en arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # axe des x
            surface.get_height() -20, # axe des y
            surface.get_width(), # longueur de la fenetre
            10 # epaisseur de la barre
        ])
        # barre rouge qui s'affifche pendant l'evenement
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # axe des x
            surface.get_height() -20, # axe des y
            (surface.get_width() / 100) * self.percent, # longueur de la fenetre
            10 # epaisseur de la barre
        ])