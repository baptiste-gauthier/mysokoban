import sys, pygame
import random
from game import Game

pygame.init()

# création de la classe repr'sentant le terrain 

# class Ground:

#     def __init__(self, width , height) -> None:
#         self.width = width
#         self.height = height

#     def buildGround(self):
#         myArray = []

#         for i in range(self.width):
#             myArray.append(random.randint(0, 4))
#         return myArray

size = width, height = 1080, 520

pygame.display.set_caption("Zelda Sokoban")
screen = pygame.display.set_mode(size)

# link_walking = pygame.image.load("assets/link_walking.gif")
chicken = pygame.image.load("assets/chicken.gif")
rock = pygame.image.load("assets/rock.png")
tree = pygame.image.load("assets/tree.png")
grass = pygame.image.load("assets/grass.png")

#instance du player

game = Game()

# myGround = Ground(20,12)
# print(myGround.buildGround())

while 1:

    #injection de l'mage du personnage 
    screen.blit(game.player.image, game.player.rect)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.moveRight()
    
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.moveLeft()

    elif game.pressed.get(pygame.K_UP):
        game.player.moveTop()

    elif game.pressed.get(pygame.K_DOWN):
        game.player.moveBottom()

    print(game.player.rect.x)
    print(game.player.rect.y)

    

    #mettre a jour mon ecran 
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
  