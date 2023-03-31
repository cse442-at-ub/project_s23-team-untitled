import pygame,sys,random
from pygame.math import Vector2
#global initialization
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()

cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number*cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.Font('Font/bahnschrift.ttf',25)

class MAIN:
    def __init__(self):
        self.screen_parameter= 230


        

    def draw_elements(self):
        self.draw_grass()




    def draw_grass(self):
        grass_color = (201,223,201)
        grass = [[grass_color if (row+col)%2==0 else (179,207,179) for col in range(cell_number)] for row in range(cell_number)]
        grass_surface = pygame.Surface((cell_number*cell_size, cell_number*cell_size))
        for row, cols in enumerate(grass):
            for col, color in enumerate(cols):
                grass_rec = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(grass_surface, color, grass_rec)
        screen.blit(grass_surface, (0, 0))



main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        
    screen.fill((179,207,178))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) #auto reset after 60s
 