import sys, pygame

from database import Database
# from tkinter.tix import DisplayStyle


class Map:

    def __init__(self) -> None:
        self.grass = pygame.image.load("assets/grass.png")
        self.rock = pygame.image.load("assets/rock.png")
        self.chicken = pygame.image.load("assets/Chicken.gif")
        self.link_walking = pygame.image.load("assets/link_walking.gif")
        self.tree = pygame.image.load("assets/tree.png")
        self.mushroom = pygame.image.load("assets/mushroom.png")
        self.water = pygame.image.load("assets/water.png")
        self.rupee = pygame.image.load("assets/rupee.png")
        self.img_victory = pygame.image.load("assets/victory.png").convert_alpha()
        self.background = pygame.image.load("assets/bg-back.png")
        self.victory = False
        self.map = self.generateMap()
        self.databse = Database()


    def generateMap(self):
        return [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #12x16
            [1,0,0,0,0,0,0,0,0,0,0,1,6,6,6,1],
            [1,0,0,0,2,0,0,0,2,0,0,1,6,6,6,1],
            [1,1,1,0,7,0,0,0,0,0,0,1,1,1,1,1],
            [6,6,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [6,6,1,0,0,0,0,0,0,0,0,7,0,0,0,1],
            [1,1,1,0,0,0,3,0,0,0,0,0,0,0,0,1],
            [1,0,0,2,0,0,0,0,0,0,0,0,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,0,1,5,5,1],
            [1,0,7,0,0,0,0,0,0,2,0,0,1,5,5,1],
            [1,0,0,0,0,0,7,0,0,0,0,0,1,5,5,1],
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        ]


    def loopMap(self,screen:pygame.Surface, start_ticks):

        grass = pygame.transform.scale(self.grass, (40, 40))
        rock = pygame.transform.scale(self.rock, (40, 40))
        chicken = pygame.transform.scale(self.chicken, (40, 40))
        link_walking = pygame.transform.scale(self.link_walking, (40, 40))
        tree = pygame.transform.scale(self.tree, (40, 40))
        mushroom = pygame.transform.scale(self.mushroom, (40, 40))
        water = pygame.transform.scale(self.water, (40, 40))
        rupee = pygame.transform.scale(self.rupee, (40, 40))

        i = 0

        while i < len(self.map):
            
            # print(i,"index")
            a = 0
            while a < len(self.map[i]):
                if self.map[i][a] == 0:
                    screen.blit(grass, (grass.get_width() * a, grass.get_height() * i))
                elif self.map[i][a] == 1:
                    screen.blit(rock, (rock.get_width() * a, rock.get_height() * i))
                elif self.map[i][a] == 2:
                    screen.blit(chicken, (chicken.get_width() * a, chicken.get_height() * i))
                elif self.map[i][a] == 3:
                    screen.blit(link_walking, (link_walking.get_width() * a, link_walking.get_height() * i))
                    index_character_y = i
                    index_character_x = a
                elif self.map[i][a] == 4:
                    screen.blit(tree, (tree.get_width() * a, tree.get_height() * i))
                elif self.map[i][a] == 5:
                    screen.blit(mushroom, (mushroom.get_width() * a, mushroom.get_height() * i))
                elif self.map[i][a] == 6:
                    screen.blit(water, (water.get_width() * a, water.get_height() * i))
                elif self.map[i][a] == 7:
                    screen.blit(rupee, (rupee.get_width() * a, rupee.get_height() * i))
                a += 1
            i += 1
        i = 0
        
        
        
        
        if self.map[3][4] == 2 and self.map[5][11] == 2 and self.map[9][2] == 2 and self.map[10][6] == 2:
            screen.blit(self.img_victory, (0, 0))
            self.victory = True
        else:
            self.victory = False
            global seconds 
            seconds = (pygame.time.get_ticks()-start_ticks)/1000

        print("seconds", seconds)
        #permet de laisser les rubis en place 
        if self.map[3][4] == 0:
            self.map[3][4] = 7
        if self.map[5][11] == 0:
            self.map[5][11] = 7
        if self.map[9][2] == 0:
            self.map[9][2] = 7
        if self.map[10][6] == 0:
            self.map[10][6] = 7






        for event in pygame.event.get():

            if event.type == pygame.QUIT: 
                sys.exit()

          
               

            if event.type == pygame.KEYDOWN:
                    if self.victory == False:

                        if event.key == pygame.K_UP:
                            if self.map[index_character_y-1][index_character_x] == 1: #collision rock 
                                self.map[index_character_y][index_character_x] = 3
                            elif self.map[index_character_y-1][index_character_x] == 2: #collision poule 
                                if self.map[index_character_y-2][index_character_x] == 1 or self.map[index_character_y-2][index_character_x] == 2:
                                    pass
                                else:
                                    self.map[index_character_y-1][index_character_x] = 3
                                    self.map[index_character_y-2][index_character_x] = 2
                                    self.map[index_character_y][index_character_x] = 0
                            else:
                                self.map[index_character_y-1][index_character_x] = 3
                                self.map[index_character_y][index_character_x] = 0

                        if event.key == pygame.K_DOWN:
                            if self.map[index_character_y+1][index_character_x] == 1:
                                self.map[index_character_y][index_character_x] = 3
                            elif self.map[index_character_y+1][index_character_x] == 2:
                                if self.map[index_character_y+2][index_character_x] == 1 or self.map[index_character_y+2][index_character_x] == 2:
                                    pass
                                else:
                                    self.map[index_character_y+1][index_character_x] = 3
                                    self.map[index_character_y+2][index_character_x] = 2
                                    self.map[index_character_y][index_character_x] = 0
                            else:    
                                self.map[index_character_y+1][index_character_x] = 3
                                self.map[index_character_y][index_character_x] = 0

                        if event.key == pygame.K_RIGHT:
                            if self.map[index_character_y][index_character_x+1] == 1:
                                self.map[index_character_y][index_character_x] = 3
                            elif self.map[index_character_y][index_character_x+1] == 2:
                                if self.map[index_character_y][index_character_x + 2] == 1 or self.map[index_character_y][index_character_x+2] == 2:
                                    pass
                                else:
                                    self.map[index_character_y][index_character_x+1] = 3
                                    self.map[index_character_y][index_character_x+2] = 2
                                    self.map[index_character_y][index_character_x] = 0
                            else:
                                self.map[index_character_y][index_character_x + 1] = 3
                                self.map[index_character_y][index_character_x] = 0

                        if event.key == pygame.K_LEFT:
                            if self.map[index_character_y][index_character_x-1] == 1:
                                self.map[index_character_y][index_character_x] = 3
                            elif self.map[index_character_y][index_character_x-1] == 2:
                                if self.map[index_character_y][index_character_x-2] == 1 or self.map[index_character_y][index_character_x-2] == 2:
                                    pass
                                else:
                                    self.map[index_character_y][index_character_x-1] = 3
                                    self.map[index_character_y][index_character_x-2] = 2
                                    self.map[index_character_y][index_character_x] = 0                                                                                                                                                                                                                      
                            else:
                                self.map[index_character_y][index_character_x - 1] = 3
                                self.map[index_character_y][index_character_x] = 0

                    if event.key == pygame.K_r:
                        self.map = self.generateMap()
                        screen.blit(self.background, (0, 0))
                        