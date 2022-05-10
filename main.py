import sys, pygame
import random
from game import Game

pygame.init()

size = width, height = 600, 500
pygame.display.set_caption("A link's Sokoban")
screen = pygame.display.set_mode(size)


game = Game()
myMap = game.map.generateMap()


while 1:

    #injection de l'image du personnage 
    screen.blit(game.player.image, game.player.rect)

    game.map.loopMap(screen)
    

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.moveRight()
    
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.moveLeft()

    elif game.pressed.get(pygame.K_UP):
        game.player.moveTop()

    elif game.pressed.get(pygame.K_DOWN):
        game.player.moveBottom()

    #mettre a jour mon ecran 
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
  