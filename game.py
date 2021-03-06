from player import player
from monster import Monster
from sounds import SoundManager
from monster import Mummy
from monster import Alien
from comet_event import cometFALLEvent
import pygame


#creer une seconde classe qui va representer notre jeu
from sounds import SoundManager


class Game:

    def __init__(self):
        #definir si le jeu a commence ou non :
        self.is_playing = False
        #generer notre joeur en debut de partie
        self.all_players = pygame.sprite.Group()
        self.player = player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = cometFALLEvent(self)
        # groupe de montre
        self.all_monsters = pygame.sprite.Group()
        # gerer le son
        self.sound_manager = SoundManager()
        # mettre le score a 0
        self.font = font = pygame.font.Font("assets/my_font.ttf", 25)
        self.score = 0
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spwan_monster(Mummy)
        self.spwan_monster(Mummy)
        self.spwan_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        #remetre le jeu a zero
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):

        # afficher le score sur l'ecran

        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # actualiser l'animation du joueur
        self.player.update_animation()

        # recuperer les projectiles
        for projectile in self.player.all_projectile:
            projectile.move()

        # recuperer les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recuperer les comets de notre jeu
        for comte in self.comet_event.all_comets:
            comte.fall()

        # aplliquer l'ensemble des images du groupe projectile
        self.player.all_projectile.draw(screen)

        # aplliquer l'ensemble des images du groupe de monstre
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images de mon groupe de comettes
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur va a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spwan_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))