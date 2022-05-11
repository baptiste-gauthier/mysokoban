import sys, pygame

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
        self.map = self.generateMap()


    def generateMap(self):
        return [
            [1,1,1,1,1,1,1,1,1,1,1,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,0,0,0,2,0,0,0,2,0,0,1],
            [1,1,1,0,0,0,0,0,0,0,0,1],
            [6,6,1,0,0,0,0,0,0,0,0,1],
            [6,6,1,0,0,0,0,0,0,0,0,1],
            [1,1,1,0,0,0,3,0,0,0,0,1],
            [1,0,0,2,0,0,0,0,0,0,0,1],
            [1,0,0,0,0,0,0,0,0,0,0,1],
            [1,1,1,1,1,1,1,1,1,1,1,1],
        ]


    def loopMap(self,screen:pygame.Surface):

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

        for event in pygame.event.get():

            if event.type == pygame.QUIT: 
                sys.exit()

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.map[index_character_y-1][index_character_x] == 1:
                            self.map[index_character_y][index_character_x] = 3
                        elif self.map[index_character_y-1][index_character_x] == 2:
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
                            self.map[index_character_y][index_character_x-1] = 3
                            self.map[index_character_y][index_character_x-2] = 2
                            self.map[index_character_y][index_character_x] = 0
                        else:
                            self.map[index_character_y][index_character_x - 1] = 3
                            self.map[index_character_y][index_character_x] = 0



            

        
       


        
    