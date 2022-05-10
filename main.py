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
pygame.display.set_caption("A link's Sokoban")
screen = pygame.display.set_mode(size)

#0
grass = pygame.image.load("assets/grass.png")
grass = pygame.transform.scale(grass, (40, 40))
#1
rock = pygame.image.load("assets/rock.png")
rock = pygame.transform.scale(rock, (40, 40))
#2
chicken = pygame.image.load("assets/Chicken.gif")
chicken = pygame.transform.scale(chicken, (40, 40))
#3
link_walking = pygame.image.load("assets/link_walking.gif")
link_walking = pygame.transform.scale(link_walking, (40, 40))
#4
tree = pygame.image.load("assets/tree.png")
tree = pygame.transform.scale(tree, (40, 40))
#5
mushroom = pygame.image.load("assets/mushroom.png")
mushroom = pygame.transform.scale(mushroom, (40, 40))
#6
water = pygame.image.load("assets/water.png")
water = pygame.transform.scale(water, (40, 40))
#7
rupee = pygame.image.load("assets/rupee.png")
rupee = pygame.transform.scale(rupee, (40, 40))



#instance du player

game = Game()
myMap = game.map.generateMap()
print(myMap[0])
# print(len(myMap))
# print(myMap[1][0])
# print(myMap[2][0])

i = 0
while i < len(myMap):
    # print(i,"index")
    a = 0
    while a < len(myMap[i]):
        if myMap[i][a] == 0:
            screen.blit(grass, (grass.get_height() * i, grass.get_width() * a))
        elif myMap[i][a] == 1:
            screen.blit(rock, (rock.get_height() * i,rock.get_width() * a))
        elif myMap[i][a] == 2:
            screen.blit(chicken, (chicken.get_height() * i,chicken.get_width() * a))
        elif myMap[i][a] == 3:
            screen.blit(link_walking, (link_walking.get_height() * i,link_walking.get_width() * a))
        elif myMap[i][a] == 4:
            screen.blit(tree, (tree.get_height() * i,tree.get_width() * a))
        elif myMap[i][a] == 5:
            screen.blit(mushroom, (mushroom.get_height() * i,mushroom.get_width() * a))
        elif myMap[i][a] == 6:
            screen.blit(water, (water.get_height() * i,water.get_width() * a))
        elif myMap[i][a] == 7:
            screen.blit(rupee, (rupee.get_height() * i,rupee.get_width() * a))
        a += 1
    i += 1


# a = 0
# b = 0
# for i in myMap:
#     print(i[0])
#     if i[a] == 0:
#         screen.blit(grass, (0,grass.get_height()*a))
#     elif i[a] == 1:
#         screen.blit(rock, (0,rock.get_height()*a))    
#     a = a + 1

while 1:

    #injection de l'image du personnage 
    screen.blit(game.player.image, game.player.rect)
    

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.moveRight()
    
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.moveLeft()

    elif game.pressed.get(pygame.K_UP):
        game.player.moveTop()

    elif game.pressed.get(pygame.K_DOWN):
        game.player.moveBottom()

    # print(game.player.rect.x)
    # print(game.player.rect.y)
    # print(game.map.generateMap())

    

    #mettre a jour mon ecran 
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == pygame.QUIT: 
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
  