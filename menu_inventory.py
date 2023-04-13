import pygame,sys,random
from pygame.math import Vector2
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

class InventoryMenu:
    def __init__(self):
        # Load images for buttons
        self.save_button = pygame.image.load('Buttons/button_save.png').convert_alpha()
        self.save_button_highlight = pygame.image.load('Buttons/button_save_highlight.png').convert_alpha()
        self.undo_button = pygame.image.load('Buttons/button_undo.png').convert_alpha()
        self.return_button = pygame.image.load('Buttons/button_return.png').convert_alpha()
        self.inventory_title = pygame.image.load('Buttons/title_inventory.png').convert_alpha()


        # Load images for skins
        self.sn_skin1_image = pygame.image.load('Skins/sn_skin1.png').convert_alpha()
        self.sn_skin2_image = pygame.image.load('Skins/sn_skin2.png').convert_alpha()
        self.sn_skin3_image = pygame.image.load('Skins/sn_skin3.png').convert_alpha()
        self.sn_skin4_image = pygame.image.load('Skins/sn_skin4.png').convert_alpha()
        self.sn_skin5_image = pygame.image.load('Skins/sn_skin5.png').convert_alpha()

        self.fr_skin1_image = pygame.image.load('Skins/fr_skin1.png').convert_alpha()
        self.fr_skin2_image = pygame.image.load('Skins/fr_skin2.png').convert_alpha()
        self.fr_skin3_image = pygame.image.load('Skins/fr_skin3.png').convert_alpha()
        self.fr_skin4_image = pygame.image.load('Skins/fr_skin4.png').convert_alpha()
        self.fr_skin5_image = pygame.image.load('Skins/fr_skin5.png').convert_alpha()
        self.fr_skin6_image = pygame.image.load('Skins/fr_skin6.png').convert_alpha()
        self.fr_skin7_image = pygame.image.load('Skins/fr_skin7.png').convert_alpha()
        self.fr_skin8_image = pygame.image.load('Skins/fr_skin8.png').convert_alpha()
        self.fr_skin9_image = pygame.image.load('Skins/fr_skin9.png').convert_alpha()

        # Create checkboxes for skin selection
        self.sn_skin1_checkbox = pygame.Rect(50, 200, 30, 30)
        self.sn_skin2_checkbox = pygame.Rect(120, 150, 30, 30)
        self.sn_skin3_checkbox = pygame.Rect(190, 150, 30, 30)
        self.sn_skin4_checkbox = pygame.Rect(260, 150, 30, 30)
        self.sn_skin5_checkbox = pygame.Rect(330, 150, 30, 30)

        self.fr_skin1_checkbox = pygame.Rect(50, 400, 30, 30)
        self.fr_skin2_checkbox = pygame.Rect(120, 400, 30, 30)
        self.fr_skin3_checkbox = pygame.Rect(190, 400, 30, 30)
        self.fr_skin4_checkbox = pygame.Rect(260, 400, 30, 30)
        self.fr_skin5_checkbox = pygame.Rect(330, 400, 30, 30)
        self.fr_skin6_checkbox = pygame.Rect(400, 400, 30, 30)
        self.fr_skin7_checkbox = pygame.Rect(470, 400, 30, 30)
        self.fr_skin8_checkbox = pygame.Rect(540, 400, 30, 30)
        self.fr_skin9_checkbox = pygame.Rect(610, 400, 30, 30)
        

        # Set initial selection
        self.sn_skin_selection = 1
        self.fr_skin_selection = 1
        self.load_skin_selections()

        # Set initial button state
        self.buttons_visible = False
        self.saved_selections = False
        


    def load_skin_selections(self):
        try:
            with open('skin_selections.txt', 'r') as f:
                lines = f.readlines()
                if len(lines) == 2:
                    self.sn_skin_selection = int(lines[0])
                    self.fr_skin_selection = int(lines[1])
            global saved
            saved = (self.sn_skin_selection, self.fr_skin_selection)
            # print(saved)
        except:
            print("Error loading skin selections")

            
    def draw_elements(self):

        distance = 10
        # Draw inventory menu title
        # title_font = pygame.font.Font('Font/bahnschrift.ttf', 40)
        # title_text = title_font.render('Inventory', True, (0, 0, 0))
        title_rect = self.inventory_title.get_rect(center=(screen.get_rect().centerx, 70))
        screen.blit(self.inventory_title, title_rect)

        # Create buttons for save, undo, and return
        self.return_button_rect = self.return_button.get_rect(topleft=(20, 20))
        self.save_button_rect = self.save_button.get_rect(midbottom=(screen.get_rect().centerx, screen.get_rect().bottom - 50))
        self.undo_button_rect = self.undo_button.get_rect(center=(title_rect.right + distance*1.5, 70 ))

        # Draw snake skin options
        sn_skin1_rect = self.sn_skin1_image.get_rect(center=(80, 230))
        sn_skin2_rect = self.sn_skin2_image.get_rect(center=(sn_skin1_rect.right + distance + sn_skin1_rect.width/2, 230))
        sn_skin3_rect = self.sn_skin3_image.get_rect(center=(sn_skin2_rect.right + distance + sn_skin2_rect.width/2, 230))
        sn_skin4_rect = self.sn_skin4_image.get_rect(center=(sn_skin3_rect.right + distance + sn_skin3_rect.width/2, 230))
        sn_skin5_rect = self.sn_skin5_image.get_rect(center=(sn_skin4_rect.right + distance + sn_skin4_rect.width/2, 230))

        screen.blit(self.sn_skin1_image, sn_skin1_rect)
        screen.blit(self.sn_skin2_image, sn_skin2_rect)
        screen.blit(self.sn_skin3_image, sn_skin3_rect)
        screen.blit(self.sn_skin4_image, sn_skin4_rect)
        screen.blit(self.sn_skin5_image, sn_skin5_rect)

        sn_skin1_checkbox_center_x = sn_skin1_rect.centerx
        sn_skin2_checkbox_center_x = sn_skin2_rect.centerx
        sn_skin3_checkbox_center_x = sn_skin3_rect.centerx
        sn_skin4_checkbox_center_x = sn_skin4_rect.centerx
        sn_skin5_checkbox_center_x = sn_skin5_rect.centerx
        
        sn_skin1_checkbox_center_y = sn_skin1_rect.centery + sn_skin1_rect.height // 2 + distance + self.sn_skin1_checkbox.height // 2
        sn_skin2_checkbox_center_y = sn_skin2_rect.centery + sn_skin2_rect.height // 2 + distance + self.sn_skin2_checkbox.height // 2
        sn_skin3_checkbox_center_y = sn_skin3_rect.centery + sn_skin3_rect.height // 2 + distance + self.sn_skin3_checkbox.height // 2
        sn_skin4_checkbox_center_y = sn_skin4_rect.centery + sn_skin4_rect.height // 2 + distance + self.sn_skin4_checkbox.height // 2
        sn_skin5_checkbox_center_y = sn_skin5_rect.centery + sn_skin5_rect.height // 2 + distance + self.sn_skin5_checkbox.height // 2

        self.sn_skin1_checkbox.center = (sn_skin1_checkbox_center_x, sn_skin1_checkbox_center_y)
        self.sn_skin2_checkbox.center = (sn_skin2_checkbox_center_x, sn_skin2_checkbox_center_y)
        self.sn_skin3_checkbox.center = (sn_skin3_checkbox_center_x, sn_skin3_checkbox_center_y)
        self.sn_skin4_checkbox.center = (sn_skin4_checkbox_center_x, sn_skin4_checkbox_center_y)
        self.sn_skin5_checkbox.center = (sn_skin5_checkbox_center_x, sn_skin5_checkbox_center_y)
        

        pygame.draw.rect(screen, (255, 255, 255), self.sn_skin1_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.sn_skin2_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.sn_skin3_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.sn_skin4_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.sn_skin5_checkbox, 2)

        if self.sn_skin_selection == 1:
            pygame.draw.circle(screen, (0, 0, 0), self.sn_skin1_checkbox.center, 10)
        elif self.sn_skin_selection == 2:
            pygame.draw.circle(screen, (0, 0, 0), self.sn_skin2_checkbox.center, 10)
        elif self.sn_skin_selection == 3:
            pygame.draw.circle(screen, (0, 0, 0), self.sn_skin3_checkbox.center, 10)
        elif self.sn_skin_selection == 4:
            pygame.draw.circle(screen, (0, 0, 0), self.sn_skin4_checkbox.center, 10)
        elif self.sn_skin_selection == 5:
            pygame.draw.circle(screen, (0, 0, 0), self.sn_skin5_checkbox.center, 10)

        # Draw fruit skin options
        distance =20 
        fr_skin1_rect = self.fr_skin1_image.get_rect(center=(100, 450))
        fr_skin2_rect = self.fr_skin2_image.get_rect(center=(fr_skin1_rect.right + distance + fr_skin1_rect.width/2, 450))
        fr_skin3_rect = self.fr_skin3_image.get_rect(center=(fr_skin2_rect.right + distance + fr_skin2_rect.width/2, 450))
        fr_skin4_rect = self.fr_skin4_image.get_rect(center=(fr_skin3_rect.right + distance + fr_skin3_rect.width/2, 450))
        fr_skin5_rect = self.fr_skin5_image.get_rect(center=(fr_skin4_rect.right + distance + fr_skin4_rect.width/2, 450))
        fr_skin6_rect = self.fr_skin6_image.get_rect(center=(fr_skin5_rect.right + distance + fr_skin5_rect.width/2, 450))
        fr_skin7_rect = self.fr_skin7_image.get_rect(center=(fr_skin6_rect.right + distance + fr_skin6_rect.width/2, 450))
        fr_skin8_rect = self.fr_skin8_image.get_rect(center=(fr_skin7_rect.right + distance + fr_skin7_rect.width/2, 450))
        fr_skin9_rect = self.fr_skin9_image.get_rect(center=(fr_skin8_rect.right + distance + fr_skin8_rect.width/2, 450))

        screen.blit(self.fr_skin1_image, fr_skin1_rect)
        screen.blit(self.fr_skin2_image, fr_skin2_rect)
        screen.blit(self.fr_skin3_image, fr_skin3_rect)
        screen.blit(self.fr_skin4_image, fr_skin4_rect)
        screen.blit(self.fr_skin5_image, fr_skin5_rect)
        screen.blit(self.fr_skin6_image, fr_skin6_rect)
        screen.blit(self.fr_skin7_image, fr_skin7_rect)
        screen.blit(self.fr_skin8_image, fr_skin8_rect)
        screen.blit(self.fr_skin9_image, fr_skin9_rect)

        checkbox_distance = 10
        fr_skin1_checkbox_center_x = fr_skin1_rect.centerx-8
        fr_skin2_checkbox_center_x = fr_skin2_rect.centerx-8
        fr_skin3_checkbox_center_x = fr_skin3_rect.centerx-8
        fr_skin4_checkbox_center_x = fr_skin4_rect.centerx-8
        fr_skin5_checkbox_center_x = fr_skin5_rect.centerx-8
        fr_skin6_checkbox_center_x = fr_skin6_rect.centerx-8
        fr_skin7_checkbox_center_x = fr_skin7_rect.centerx-8
        fr_skin8_checkbox_center_x = fr_skin8_rect.centerx-8
        fr_skin9_checkbox_center_x = fr_skin9_rect.centerx-8
    

        fr_skin1_checkbox_center_y = fr_skin1_rect.centery + fr_skin1_rect.height // 2 + checkbox_distance + self.fr_skin1_checkbox.height // 2
        fr_skin2_checkbox_center_y = fr_skin2_rect.centery + fr_skin2_rect.height // 2 + checkbox_distance + self.fr_skin2_checkbox.height // 2
        fr_skin3_checkbox_center_y = fr_skin3_rect.centery + fr_skin3_rect.height // 2 + checkbox_distance + self.fr_skin3_checkbox.height // 2
        fr_skin4_checkbox_center_y = fr_skin4_rect.centery + fr_skin4_rect.height // 2 + checkbox_distance + self.fr_skin4_checkbox.height // 2
        fr_skin5_checkbox_center_y = fr_skin5_rect.centery + fr_skin5_rect.height // 2 + checkbox_distance + self.fr_skin5_checkbox.height // 2
        fr_skin6_checkbox_center_y = fr_skin6_rect.centery + fr_skin6_rect.height // 2 + checkbox_distance + self.fr_skin6_checkbox.height // 2
        fr_skin7_checkbox_center_y = fr_skin7_rect.centery + fr_skin7_rect.height // 2 + checkbox_distance + self.fr_skin7_checkbox.height // 2
        fr_skin8_checkbox_center_y = fr_skin8_rect.centery + fr_skin8_rect.height // 2 + checkbox_distance + self.fr_skin8_checkbox.height // 2
        fr_skin9_checkbox_center_y = fr_skin9_rect.centery + fr_skin9_rect.height // 2 + checkbox_distance + self.fr_skin9_checkbox.height // 2

        self.fr_skin1_checkbox.center = (fr_skin1_checkbox_center_x, fr_skin1_checkbox_center_y)
        self.fr_skin2_checkbox.center = (fr_skin2_checkbox_center_x, fr_skin2_checkbox_center_y)
        self.fr_skin3_checkbox.center = (fr_skin3_checkbox_center_x, fr_skin3_checkbox_center_y)
        self.fr_skin4_checkbox.center = (fr_skin4_checkbox_center_x, fr_skin4_checkbox_center_y)
        self.fr_skin5_checkbox.center = (fr_skin5_checkbox_center_x, fr_skin5_checkbox_center_y)
        self.fr_skin6_checkbox.center = (fr_skin6_checkbox_center_x, fr_skin6_checkbox_center_y)
        self.fr_skin7_checkbox.center = (fr_skin7_checkbox_center_x, fr_skin7_checkbox_center_y)
        self.fr_skin8_checkbox.center = (fr_skin8_checkbox_center_x, fr_skin8_checkbox_center_y)
        self.fr_skin9_checkbox.center = (fr_skin9_checkbox_center_x, fr_skin9_checkbox_center_y)

        pygame.draw.rect(screen, (255, 255, 255), self.fr_skin1_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.fr_skin2_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.fr_skin3_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.fr_skin4_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.fr_skin5_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.fr_skin6_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.fr_skin7_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.fr_skin8_checkbox, 2)
        pygame.draw.rect(screen, (255, 255, 255), self.fr_skin9_checkbox, 2)


        if self.fr_skin_selection == 1:
            pygame.draw.circle(screen, (0, 0, 0), self.fr_skin1_checkbox.center, 10)
        elif self.fr_skin_selection == 2:
            pygame.draw.circle(screen, (0, 0, 0), self.fr_skin2_checkbox.center, 10)
        elif self.fr_skin_selection == 3:
            pygame.draw.circle(screen, (0, 0, 0), self.fr_skin3_checkbox.center, 10)
        elif self.fr_skin_selection == 4:
            pygame.draw.circle(screen, (0, 0, 0), self.fr_skin4_checkbox.center, 10)
        elif self.fr_skin_selection == 5:
            pygame.draw.circle(screen, (0, 0, 0), self.fr_skin5_checkbox.center, 10)
        elif self.fr_skin_selection == 6:
            pygame.draw.circle(screen, (0, 0, 0), self.fr_skin6_checkbox.center, 10)
        elif self.fr_skin_selection == 7:
            pygame.draw.circle(screen, (0, 0, 0), self.fr_skin7_checkbox.center, 10)
        elif self.fr_skin_selection == 8:
            pygame.draw.circle(screen, (0, 0, 0), self.fr_skin8_checkbox.center, 10)
        elif self.fr_skin_selection == 9:
            pygame.draw.circle(screen, (0, 0, 0), self.fr_skin9_checkbox.center, 10)

        # Draw save, undo, and return buttons
        if self.buttons_visible:
            mouse_pos = pygame.mouse.get_pos()
            if self.save_button_rect.collidepoint(mouse_pos):
                screen.blit(self.save_button_highlight, self.save_button_rect)
                screen.blit(self.undo_button, self.undo_button_rect)
            else: 
                screen.blit(self.save_button, self.save_button_rect)
                screen.blit(self.undo_button, self.undo_button_rect)
            
        screen.blit(self.return_button, self.return_button_rect)
        global saved

    def update_button_states(self):
        # if self.sn_skin_selection != 1 or self.fr_skin_selection != 1:
        # print(self.saved)
        global saved
        if (self.sn_skin_selection != saved[0]) or (self.fr_skin_selection != saved[1]):
            self.buttons_visible = True
            # print(self.save_button_enabled)
            # print(self.undo_button_enabled)
        else:
            self.buttons_visible = False

       
    def save_changes(self):
        # Save the skin selections to a file (or database, or any other storage mechanism)
        with open('skin_selections.txt', 'w') as f:
            f.write(str(self.sn_skin_selection) + '\n')
            f.write(str(self.fr_skin_selection) + '\n')
        global saved
        saved = (self.sn_skin_selection, self.fr_skin_selection)
        

    def undo_skin_selections(self):
        with open('skin_selections.txt', 'r') as f:
            lines = f.readlines()
        self.sn_skin_selection = int(lines[0])
        self.fr_skin_selection = int(lines[1])
        self.saved_selections = True
        

    def handle_save_click(self):
        self.save_changes()
        self.saved_selections = True

    def hide_buttons(self):
        self.buttons_visible = False
        


class MAIN:
    def __init__(self):
        self.screen_parameter= 230
        self.inventory_menu = InventoryMenu()

    def draw_elements(self):
        self.draw_grass()
        self.inventory_menu.draw_elements()
        

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

        # Check for mouse clicks on the checkboxes and buttons
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if main_game.inventory_menu.sn_skin1_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.sn_skin_selection = 1
            elif main_game.inventory_menu.sn_skin2_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.sn_skin_selection = 2
            elif main_game.inventory_menu.sn_skin3_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.sn_skin_selection = 3
            elif main_game.inventory_menu.sn_skin4_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.sn_skin_selection = 4
            elif main_game.inventory_menu.sn_skin5_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.sn_skin_selection = 5
            elif main_game.inventory_menu.fr_skin1_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.fr_skin_selection = 1
            elif main_game.inventory_menu.fr_skin2_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.fr_skin_selection = 2
            elif main_game.inventory_menu.fr_skin3_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.fr_skin_selection = 3
            elif main_game.inventory_menu.fr_skin4_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.fr_skin_selection = 4
            elif main_game.inventory_menu.fr_skin5_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.fr_skin_selection = 5
            elif main_game.inventory_menu.fr_skin6_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.fr_skin_selection = 6
            elif main_game.inventory_menu.fr_skin7_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.fr_skin_selection = 7
            elif main_game.inventory_menu.fr_skin8_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.fr_skin_selection = 8
            elif main_game.inventory_menu.fr_skin9_checkbox.collidepoint(mouse_pos):
                main_game.inventory_menu.fr_skin_selection = 9
            elif main_game.inventory_menu.save_button_rect.collidepoint(mouse_pos):
                # Handle save button click
                # Draw the highlighted save button
                main_game.inventory_menu.handle_save_click()
                main_game.inventory_menu.hide_buttons()
            elif main_game.inventory_menu.undo_button_rect.collidepoint(mouse_pos):
                # Handle undo button click
                main_game.inventory_menu.undo_skin_selections()
                main_game.inventory_menu.hide_buttons()
            elif main_game.inventory_menu.return_button_rect.collidepoint(mouse_pos):
                # Handle return button click
                pass
            else:
                 # Draw the regular save button
                 pass
            main_game.inventory_menu.update_button_states()
            if main_game.inventory_menu.saved_selections:
                main_game.inventory_menu.hide_buttons()
                main_game.inventory_menu.saved_selections = False



    screen.fill((179,207,178))
    main_game.draw_elements()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Snaking')
    pygame.display.update()
    clock.tick(60)