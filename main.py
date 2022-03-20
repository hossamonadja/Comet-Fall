import pygame
import math
from game import Game
pygame.init()

# definir une clock
clock = pygame.time.Clock()
FPS = 60

#generer la fenetre du jeu
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080, 720))

#importer l'arriere plan du jeu
background = pygame.image.load('assets/bg.jpg')

# charger la baniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# charger le bouton play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y =math.ceil(screen.get_height() / 2)

# charger notre jeu
game = Game()

#Creation d'une variable pour l'execution de la fenetre
running = True

#Creation de la boucle qui s'execute tant que running=vrai
while running:

    # appliquer l'arriere plan du jeu
    screen.blit(background, (0, -200))

    # verifier si le jeu a commencé  :
    if game.is_playing:
        # declencher les instruction de la partie
        game.update(screen)
    # verifier si le jeu n'a pas commencé  :
    else:
        # ajouter mon ecran de bienvenu
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #mettre a jour l'ecran
    pygame.display.flip()

    #si le joueur ferme la fenetre

    for event in pygame.event.get():
        #fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Au revoir")
        # detecter action clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenché
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    #lancer le jeu
                    game.start()
                    # jouer le son
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si la souris le bouton play est enclencher
            if play_button_rect.collidepoint(event.pos):
                #lancer le jeu
                game.start()
                # jouer le son
                #game.sound_manager.play('click')
    # fixer le nombre de fps sur ma clock
    clock.tick(FPS)