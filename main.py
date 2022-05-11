import sys, pygame
import random
from game import Game

pygame.init()

size = width, height = 640, 480
pygame.display.set_caption("A Link's Sokoban")
screen = pygame.display.set_mode(size)


game = Game()
myMap = game.map.generateMap()


while 1:

    #injection de l'image du personnage 
    # screen.blit(game.player.image, game.player.rect)

    game.map.loopMap(screen)
    
    #mettre a jour mon ecran 
    pygame.display.flip()



  