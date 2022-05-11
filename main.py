import sys, pygame
import random
from game import Game

pygame.init()

size = width, height = 480, 400
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

    # for event in pygame.event.get():
    
    #     if event.type == pygame.QUIT: 
    #         sys.exit()

    #     elif event.type == pygame.KEYDOWN:
    #         print('tata')

  