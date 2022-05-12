import sys, pygame
import random
from database import Database
from game import Game
import mysql.connector


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("gerudo_valley.wav")
pygame.mixer.music.play(-1)



size = width, height = 640, 480
pygame.display.set_caption("A Link's Sokoban")
screen = pygame.display.set_mode(size)


game = Game()
myMap = game.map.generateMap()

database = Database()
database.insertScoreDatabase("test" , 15.6)
start_ticks = pygame.time.get_ticks()


while 1:
    seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
    game.map.loopMap(screen , seconds)
    
    #mettre a jour mon ecran 
    pygame.display.flip()






  