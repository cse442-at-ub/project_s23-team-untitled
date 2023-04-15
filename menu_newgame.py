from easy import *
from level_2 import *
from level_3 import *

#global initialization
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
saved = None
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number*cell_size))
clock = pygame.time.Clock()
game_font = pygame.font.Font('Font/bahnschrift.ttf',25)
icon = pygame.image.load('Graphics/snake.png')

def background_grass(screen):
    grass_color = (201, 223, 201)
    for row in range(cell_number):
        if row % 2 == 0:
            for col in range(cell_number):
                if col % 2 == 0:
                    grass_rec = pygame.Rect(
                        col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rec)
        else:
            for col in range(cell_number):
                if col % 2 != 0:
                    grass_rec = pygame.Rect(
                        col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rec)

def new_game():

    button_easy = pygame.image.load('Buttons/button_easy.png').convert_alpha()
    button_medium = pygame.image.load('Buttons/button_medium.png').convert_alpha()
    button_hard = pygame.image.load('Buttons/button_hard.png').convert_alpha()

    button_easy_highlight = pygame.image.load('Buttons/button_easy_highlight.png').convert_alpha()
    button_medium_highlight = pygame.image.load('Buttons/button_medium_highlight.png').convert_alpha()
    button_hard_highlight = pygame.image.load('Buttons/button_hard_highlight.png').convert_alpha()

    newgame_title = pygame.image.load('Buttons/title_newgame.png').convert_alpha()
    return_button = pygame.image.load('Buttons/button_return.png').convert_alpha()
    
    easybutton_visible = False
    medbutton_visible = False
    hardbutton_visible = False

    while True:
        screen.fill((179, 207, 178))
        background_grass(screen)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Snaking')

        newgame_rect = newgame_title.get_rect(center=(screen.get_rect().centerx, 70))
        screen.blit(newgame_title,newgame_rect)

        return_button_rect = return_button.get_rect(topleft=(20, 20))
        screen.blit(return_button, return_button_rect)


        level1_rect = button_easy.get_rect(center=(screen.get_rect().centerx, 250))
        level2_rect = button_medium.get_rect(center=(level1_rect.centerx, 400))
        level3_rect = button_hard.get_rect(center=(level2_rect.centerx, 550))

        level1_rect_highlight = button_easy_highlight.get_rect(center=level1_rect.center)
        level2_rect_highlight = button_medium_highlight.get_rect(center=level2_rect.center)
        level3_rect_highlight = button_hard_highlight.get_rect(center=level3_rect.center)
        
        mouse_pos = pygame.mouse.get_pos()

        if level1_rect.collidepoint(mouse_pos):
            easybutton_visible = True   
        else:
            easybutton_visible = False
            # screen.blit(button_easy_highlight, level1_rect)
        if level2_rect.collidepoint(mouse_pos):
            medbutton_visible = True
        else:
            medbutton_visible = False
            # screen.blit(button_medium_highlight, level2_rect)
        if level3_rect.collidepoint(mouse_pos):
            hardbutton_visible = True
        else:
            hardbutton_visible = False
            # screen.blit(button_hard_highlight, level3_rect)

        if easybutton_visible:
            screen.blit(button_easy_highlight, level1_rect_highlight)
        else:
            screen.blit(button_easy, level1_rect)
        
        if medbutton_visible:
            screen.blit(button_medium_highlight, level2_rect_highlight)
        else:
            screen.blit(button_medium, level2_rect)

        if hardbutton_visible:
            screen.blit(button_hard_highlight, level3_rect_highlight)
        else:
            screen.blit(button_hard, level3_rect)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.MOUSEBUTTONDOWN and level1_rect.collidepoint(mouse_pos):
                main_game = EASY_MAIN()
                main_game.game()

            if event.type == pygame.MOUSEBUTTONDOWN and level2_rect.collidepoint(mouse_pos):
                main_game = MED_MAIN()
                main_game.game()
            
            if event.type == pygame.MOUSEBUTTONDOWN and level3_rect.collidepoint(mouse_pos):
                main_game = HARD_MAIN()
                main_game.game()

        pygame.display.update()
        clock.tick(60)