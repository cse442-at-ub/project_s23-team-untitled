from game_elements import *

def inventory():
    class InventoryMenu:
        def __init__(self):
            # Load images for buttons
            self.save_button = pygame.image.load('Buttons/button_save.png').convert_alpha()
            self.save_button_highlight = pygame.image.load('Buttons/button_save_highlight.png').convert_alpha()
            self.undo_button = pygame.image.load('Buttons/button_undo.png').convert_alpha()
            self.return_button = pygame.image.load('Buttons/button_return.png').convert_alpha()
            self.inventory_title = pygame.image.load('Buttons/title_inventory.png').convert_alpha()
            self.unlock_sn_button = pygame.image.load('Buttons/lock_snake.png').convert_alpha()
            self.unlock_fr_button = pygame.image.load('Buttons/lock_fruit.png').convert_alpha()
            self.coin = pygame.image.load('Graphics/coin.png').convert_alpha()


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
            self.coin_amn = 0
            self.sn_unlock = [] 
            self.fr_unlock = []
            self.load_skin_selections()

            # Set initial button state
            self.buttons_visible = False
            self.saved_selections = False
            distance = 10
                # Draw snake skin options
            self.sn_skin1_rect = self.sn_skin1_image.get_rect(center=(80, 230))
            self.sn_skin2_rect = self.sn_skin2_image.get_rect(center=(self.sn_skin1_rect.right + distance + self.sn_skin1_rect.width/2, 230))
            self.sn_skin3_rect = self.sn_skin3_image.get_rect(center=(self.sn_skin2_rect.right + distance + self.sn_skin2_rect.width/2, 230))
            self.sn_skin4_rect = self.sn_skin4_image.get_rect(center=(self.sn_skin3_rect.right + distance + self.sn_skin3_rect.width/2, 230))
            self.sn_skin5_rect = self.sn_skin5_image.get_rect(center=(self.sn_skin4_rect.right + distance + self.sn_skin4_rect.width/2, 230))

            self.unlock_sn_button_rect2= self.unlock_sn_button.get_rect(center = self.sn_skin2_rect.center)
            self.unlock_sn_button_rect3= self.unlock_sn_button.get_rect(center = self.sn_skin3_rect.center)
            self.unlock_sn_button_rect4= self.unlock_sn_button.get_rect(center = self.sn_skin4_rect.center)
            self.unlock_sn_button_rect5= self.unlock_sn_button.get_rect(center = self.sn_skin5_rect.center)

            distance =20 
            self.fr_skin1_rect = self.fr_skin1_image.get_rect(center=(100, 450))
            self.fr_skin2_rect = self.fr_skin2_image.get_rect(center=(self.fr_skin1_rect.right + distance + self.fr_skin1_rect.width/2, 450))
            self.fr_skin3_rect = self.fr_skin3_image.get_rect(center=(self.fr_skin2_rect.right + distance + self.fr_skin2_rect.width/2, 450))
            self.fr_skin4_rect = self.fr_skin4_image.get_rect(center=(self.fr_skin3_rect.right + distance + self.fr_skin3_rect.width/2, 450))
            self.fr_skin5_rect = self.fr_skin5_image.get_rect(center=(self.fr_skin4_rect.right + distance + self.fr_skin4_rect.width/2, 450))
            self.fr_skin6_rect = self.fr_skin6_image.get_rect(center=(self.fr_skin5_rect.right + distance + self.fr_skin5_rect.width/2, 450))
            self.fr_skin7_rect = self.fr_skin7_image.get_rect(center=(self.fr_skin6_rect.right + distance + self.fr_skin6_rect.width/2, 450))
            self.fr_skin8_rect = self.fr_skin8_image.get_rect(center=(self.fr_skin7_rect.right + distance + self.fr_skin7_rect.width/2, 450))
            self.fr_skin9_rect = self.fr_skin9_image.get_rect(center=(self.fr_skin8_rect.right + distance + self.fr_skin8_rect.width/2, 450))

            self.unlock_fr_button_rect2= self.unlock_fr_button.get_rect(center = (self.fr_skin2_rect.centerx - 7, self.fr_skin2_rect.centery +2))
            self.unlock_fr_button_rect3= self.unlock_fr_button.get_rect(center = (self.fr_skin3_rect.centerx - 7, self.fr_skin3_rect.centery +2))
            self.unlock_fr_button_rect4= self.unlock_fr_button.get_rect(center = (self.fr_skin4_rect.centerx - 7, self.fr_skin4_rect.centery +2))
            self.unlock_fr_button_rect5= self.unlock_fr_button.get_rect(center = (self.fr_skin5_rect.centerx - 7, self.fr_skin5_rect.centery +2))
            self.unlock_fr_button_rect6= self.unlock_fr_button.get_rect(center = (self.fr_skin6_rect.centerx - 7, self.fr_skin6_rect.centery +2))
            self.unlock_fr_button_rect7= self.unlock_fr_button.get_rect(center = (self.fr_skin7_rect.centerx - 7, self.fr_skin7_rect.centery +2))
            self.unlock_fr_button_rect8= self.unlock_fr_button.get_rect(center = (self.fr_skin8_rect.centerx - 7, self.fr_skin8_rect.centery +2))
            self.unlock_fr_button_rect9= self.unlock_fr_button.get_rect(center = (self.fr_skin9_rect.centerx - 7, self.fr_skin9_rect.centery +2))



        def load_skin_selections(self):
            try:
                with open('skin_selections.txt', 'r') as f:
                    lines = f.readlines()
                    if len(lines) == 4:
                        self.sn_skin_selection = int(lines[0])
                        self.fr_skin_selection = int(lines[1])
                        temp_list1 = lines[2].strip().split(',')
                        # print(temp_list)
                        for value in temp_list1:
                            #print(value)
                            #print(value)
                            #print(type(value))
                            if value == 'True':
                                self.sn_unlock.append(True)
                            else :
                                self.sn_unlock.append(False)
                            # print(self.sn_unlock)
                        temp_list2 = lines[3].strip().split(',')
                        for value in temp_list2:
                            if value == 'True':
                                self.fr_unlock.append(True)
                            else :
                                self.fr_unlock.append(False)
                            # print(self.fr_unlock)
                if not (os.path.exists('coins.bin')):
                    # create binary coins file
                    with open('coins.bin', 'wb') as file:
                        pickle.dump(0, file)
                else:
                    with open('coins.bin', 'rb') as file:
                        self.coin_amn = pickle.load(file)
                    print(self.coin_amn)
                # print(lines[3])
                # print(lines[4])
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
            self.coin_rect = self.coin.get_rect(center = (title_rect.left - distance*7, 70))

            # bo_font.set_bold(True)
            sn2_price = bo_font.render("5", True, (255, 0, 0))
            sn3_price = bo_font.render("20", True, (255, 0, 0))
            sn4_price = bo_font.render("50", True, (255, 0, 0))
            sn5_price = bo_font.render("100", True, (255, 0, 0))

            screen.blit(self.sn_skin1_image, self.sn_skin1_rect)
            screen.blit(self.sn_skin2_image, self.sn_skin2_rect)
            screen.blit(self.sn_skin3_image, self.sn_skin3_rect)
            screen.blit(self.sn_skin4_image, self.sn_skin4_rect)
            screen.blit(self.sn_skin5_image, self.sn_skin5_rect)

            sn_skin1_checkbox_center_x = self.sn_skin1_rect.centerx
            sn_skin2_checkbox_center_x = self.sn_skin2_rect.centerx
            sn_skin3_checkbox_center_x = self.sn_skin3_rect.centerx
            sn_skin4_checkbox_center_x = self.sn_skin4_rect.centerx
            sn_skin5_checkbox_center_x = self.sn_skin5_rect.centerx


            
            sn_skin1_checkbox_center_y = self.sn_skin1_rect.centery + self.sn_skin1_rect.height // 2 + distance + self.sn_skin1_checkbox.height // 2
            sn_skin2_checkbox_center_y = self.sn_skin2_rect.centery + self.sn_skin2_rect.height // 2 + distance + self.sn_skin2_checkbox.height // 2
            sn_skin3_checkbox_center_y = self.sn_skin3_rect.centery + self.sn_skin3_rect.height // 2 + distance + self.sn_skin3_checkbox.height // 2
            sn_skin4_checkbox_center_y = self.sn_skin4_rect.centery + self.sn_skin4_rect.height // 2 + distance + self.sn_skin4_checkbox.height // 2
            sn_skin5_checkbox_center_y = self.sn_skin5_rect.centery + self.sn_skin5_rect.height // 2 + distance + self.sn_skin5_checkbox.height // 2

            self.sn_skin1_checkbox.center = (sn_skin1_checkbox_center_x, sn_skin1_checkbox_center_y)
            self.sn_skin2_checkbox.center = (sn_skin2_checkbox_center_x, sn_skin2_checkbox_center_y)
            self.sn_skin3_checkbox.center = (sn_skin3_checkbox_center_x, sn_skin3_checkbox_center_y)
            self.sn_skin4_checkbox.center = (sn_skin4_checkbox_center_x, sn_skin4_checkbox_center_y)
            self.sn_skin5_checkbox.center = (sn_skin5_checkbox_center_x, sn_skin5_checkbox_center_y)
            # print(len(self.sn_unlock))
            
            if self.sn_unlock[0]:
                pygame.draw.rect(screen, (255, 255, 255), self.sn_skin2_checkbox, 2)
            else:
                screen.blit(sn2_price, self.sn_skin2_checkbox)
                screen.blit(self.unlock_sn_button,self.unlock_sn_button_rect2)
            
            if self.sn_unlock[1]:
                pygame.draw.rect(screen, (255, 255, 255), self.sn_skin3_checkbox, 2)
            else:
                screen.blit(sn3_price, self.sn_skin3_checkbox)
                screen.blit(self.unlock_sn_button,self.unlock_sn_button_rect3)
            
            if self.sn_unlock[2]:
                pygame.draw.rect(screen, (255, 255, 255), self.sn_skin4_checkbox, 2)
            else:
                screen.blit(sn4_price, self.sn_skin4_checkbox)
                screen.blit(self.unlock_sn_button,self.unlock_sn_button_rect4)
            
            if self.sn_unlock[3]:
                pygame.draw.rect(screen, (255, 255, 255), self.sn_skin5_checkbox, 2)
            else:
                screen.blit(sn5_price, self.sn_skin5_checkbox)
                screen.blit(self.unlock_sn_button,self.unlock_sn_button_rect5)
                
            
            pygame.draw.rect(screen, (255, 255, 255), self.sn_skin1_checkbox, 2)
            
            
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


            screen.blit(self.fr_skin1_image, self.fr_skin1_rect)
            screen.blit(self.fr_skin2_image, self.fr_skin2_rect)
            screen.blit(self.fr_skin3_image, self.fr_skin3_rect)
            screen.blit(self.fr_skin4_image, self.fr_skin4_rect)
            screen.blit(self.fr_skin5_image, self.fr_skin5_rect)
            screen.blit(self.fr_skin6_image, self.fr_skin6_rect)
            screen.blit(self.fr_skin7_image, self.fr_skin7_rect)
            screen.blit(self.fr_skin8_image, self.fr_skin8_rect)
            screen.blit(self.fr_skin9_image, self.fr_skin9_rect)

            fr2_price = bo_font.render("5", True, (255, 0, 0))
            fr3_price = bo_font.render("15", True, (255, 0, 0))
            fr4_price = bo_font.render("25", True, (255, 0, 0))
            fr5_price = bo_font.render("35", True, (255, 0, 0))
            fr6_price = bo_font.render("45", True, (255, 0, 0))
            fr7_price = bo_font.render("45", True, (255, 0, 0))
            fr8_price = bo_font.render("45", True, (255, 0, 0))
            fr9_price = bo_font.render("65", True, (255, 0, 0))

            checkbox_distance = 10
            fr_skin1_checkbox_center_x = self.fr_skin1_rect.centerx-8
            fr_skin2_checkbox_center_x = self.fr_skin2_rect.centerx-8
            fr_skin3_checkbox_center_x = self.fr_skin3_rect.centerx-8
            fr_skin4_checkbox_center_x = self.fr_skin4_rect.centerx-8
            fr_skin5_checkbox_center_x = self.fr_skin5_rect.centerx-8
            fr_skin6_checkbox_center_x = self.fr_skin6_rect.centerx-8
            fr_skin7_checkbox_center_x = self.fr_skin7_rect.centerx-8
            fr_skin8_checkbox_center_x = self.fr_skin8_rect.centerx-8
            fr_skin9_checkbox_center_x = self.fr_skin9_rect.centerx-8

            fr_skin1_checkbox_center_y = self.fr_skin1_rect.centery + self.fr_skin1_rect.height // 2 + checkbox_distance + self.fr_skin1_checkbox.height // 2
            fr_skin2_checkbox_center_y = self.fr_skin2_rect.centery + self.fr_skin2_rect.height // 2 + checkbox_distance + self.fr_skin2_checkbox.height // 2
            fr_skin3_checkbox_center_y = self.fr_skin3_rect.centery + self.fr_skin3_rect.height // 2 + checkbox_distance + self.fr_skin3_checkbox.height // 2
            fr_skin4_checkbox_center_y = self.fr_skin4_rect.centery + self.fr_skin4_rect.height // 2 + checkbox_distance + self.fr_skin4_checkbox.height // 2
            fr_skin5_checkbox_center_y = self.fr_skin5_rect.centery + self.fr_skin5_rect.height // 2 + checkbox_distance + self.fr_skin5_checkbox.height // 2
            fr_skin6_checkbox_center_y = self.fr_skin6_rect.centery + self.fr_skin6_rect.height // 2 + checkbox_distance + self.fr_skin6_checkbox.height // 2
            fr_skin7_checkbox_center_y = self.fr_skin7_rect.centery + self.fr_skin7_rect.height // 2 + checkbox_distance + self.fr_skin7_checkbox.height // 2
            fr_skin8_checkbox_center_y = self.fr_skin8_rect.centery + self.fr_skin8_rect.height // 2 + checkbox_distance + self.fr_skin8_checkbox.height // 2
            fr_skin9_checkbox_center_y = self.fr_skin9_rect.centery + self.fr_skin9_rect.height // 2 + checkbox_distance + self.fr_skin9_checkbox.height // 2

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

            if self.fr_unlock[0]:
                pygame.draw.rect(screen, (255, 255, 255), self.fr_skin2_checkbox, 2)
            else:
                screen.blit(fr2_price, self.fr_skin2_checkbox)
                screen.blit(self.unlock_fr_button,self.unlock_fr_button_rect2)
            
            if self.fr_unlock[1]:
                pygame.draw.rect(screen, (255, 255, 255), self.fr_skin3_checkbox, 2)
            else:
                screen.blit(fr3_price, self.fr_skin3_checkbox)
                screen.blit(self.unlock_fr_button,self.unlock_fr_button_rect3)
            
            if self.fr_unlock[2]:
                pygame.draw.rect(screen, (255, 255, 255), self.fr_skin4_checkbox, 2)
            else:
                screen.blit(fr4_price, self.fr_skin4_checkbox)
                screen.blit(self.unlock_fr_button,self.unlock_fr_button_rect4)
            
            if self.fr_unlock[3]:
                pygame.draw.rect(screen, (255, 255, 255), self.fr_skin5_checkbox, 2)
            else:
                screen.blit(fr5_price, self.fr_skin5_checkbox)
                screen.blit(self.unlock_fr_button,self.unlock_fr_button_rect5)

            if self.fr_unlock[4]:
                pygame.draw.rect(screen, (255, 255, 255), self.fr_skin6_checkbox, 2)
            else:
                screen.blit(fr6_price, self.fr_skin6_checkbox)
                screen.blit(self.unlock_fr_button,self.unlock_fr_button_rect6)

            if self.fr_unlock[5]:
                pygame.draw.rect(screen, (255, 255, 255), self.fr_skin7_checkbox, 2)
            else:
                screen.blit(fr7_price, self.fr_skin7_checkbox)
                screen.blit(self.unlock_fr_button,self.unlock_fr_button_rect7)

            if self.fr_unlock[6]:
                pygame.draw.rect(screen, (255, 255, 255), self.fr_skin8_checkbox, 2)
            else:
                screen.blit(fr8_price, self.fr_skin8_checkbox)
                screen.blit(self.unlock_fr_button,self.unlock_fr_button_rect8)

            if self.fr_unlock[7]:
                pygame.draw.rect(screen, (255, 255, 255), self.fr_skin9_checkbox, 2)
            else:
                screen.blit(fr9_price, self.fr_skin9_checkbox)
                screen.blit(self.unlock_fr_button,self.unlock_fr_button_rect9)


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
            screen.blit(self.coin, self.coin_rect)
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
                f.write((','.join(str(i) for i in self.sn_unlock)) + '\n')
                f.write((','.join(str(i) for i in self.fr_unlock)) + '\n')

            with open('coins.bin', 'wb') as file:
                pickle.dump(self.coin_amn, file)

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
            
        def unlock_skin(self):
            self.coin_amn -= 10



    class MAIN:
        def __init__(self):
            self.screen_parameter= 230
            self.inventory_menu = InventoryMenu()
            self.oops = False
            self.oops_start_time = 0


        def draw_elements(self):
            self.draw_grass()
            self.inventory_menu.draw_elements()
            self.draw_coin_amn()
            if self.oops:
                self.oops_message()
                if pygame.time.get_ticks() - self.oops_start_time > 1000:  # hide message after 2 seconds
                    self.oops = False

            

        def draw_grass(self):
            grass_color = (201,223,201)
            grass = [[grass_color if (row+col)%2==0 else (179,207,179) for col in range(cell_number)] for row in range(cell_number)]
            grass_surface = pygame.Surface((cell_number*cell_size, cell_number*cell_size))
            for row, cols in enumerate(grass):
                for col, color in enumerate(cols):
                    grass_rec = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(grass_surface, color, grass_rec)
            screen.blit(grass_surface, (0, 0))

        def draw_coin_amn(self):
            coin_amn_text = str(self.inventory_menu.coin_amn)
            coin_am_surface = game_font.render(coin_amn_text,True, (0, 0, 0, 128))
            coin_amn_rect = coin_am_surface.get_rect(center = (self.inventory_menu.coin_rect.right + 10, 70))
            screen.blit(coin_am_surface,coin_amn_rect)

        def oops_message(self):
            font = pygame.font.Font(None, 36)  # choose a font and size
            text = font.render("Not enough coin", True, (255, 0, 0))  # create a text surface
            global screen_width, screen_height
            text_rect = text.get_rect(center=(screen_width//2, screen_height//2))  # position the text at the center of the screen
            screen.blit(text, text_rect)  # draw the text surface onto the screen
    
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
                
                if main_game.inventory_menu.sn_skin2_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.sn_unlock[0]:
                    main_game.inventory_menu.sn_skin_selection = 2
                elif main_game.inventory_menu.unlock_sn_button_rect2.collidepoint(mouse_pos) and not main_game.inventory_menu.sn_unlock[0]:
                    if main_game.inventory_menu.coin_amn - 5 >= 0:
                        main_game.inventory_menu.sn_unlock[0] = True
                        main_game.inventory_menu.coin_amn -= 5
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()

                        
                        

                if main_game.inventory_menu.sn_skin3_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.sn_unlock[1]:
                    main_game.inventory_menu.sn_skin_selection = 3
                elif main_game.inventory_menu.unlock_sn_button_rect3.collidepoint(mouse_pos) and not main_game.inventory_menu.sn_unlock[1]:
                    if main_game.inventory_menu.coin_amn - 20 >= 0:
                        main_game.inventory_menu.sn_unlock[1] = True
                        main_game.inventory_menu.coin_amn -= 20
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()
                        
                        
                if main_game.inventory_menu.sn_skin4_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.sn_unlock[2]:
                    main_game.inventory_menu.sn_skin_selection = 4
                elif main_game.inventory_menu.unlock_sn_button_rect4.collidepoint(mouse_pos) and not main_game.inventory_menu.sn_unlock[2]:
                    if main_game.inventory_menu.coin_amn - 50 >= 0:
                        main_game.inventory_menu.sn_unlock[2] = True
                        main_game.inventory_menu.coin_amn -= 50
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()
                        


                if main_game.inventory_menu.sn_skin5_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.sn_unlock[3]:
                    main_game.inventory_menu.sn_skin_selection = 5
                elif main_game.inventory_menu.unlock_sn_button_rect5.collidepoint(mouse_pos) and not main_game.inventory_menu.sn_unlock[3]:
                    if main_game.inventory_menu.coin_amn - 100 >= 0:
                        main_game.inventory_menu.sn_unlock[3] = True
                        main_game.inventory_menu.coin_amn -= 100
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()
                        


                if main_game.inventory_menu.fr_skin1_checkbox.collidepoint(mouse_pos):
                    main_game.inventory_menu.fr_skin_selection = 1
                

                if main_game.inventory_menu.fr_skin2_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.fr_unlock[0]:
                    main_game.inventory_menu.fr_skin_selection = 2
                elif main_game.inventory_menu.unlock_fr_button_rect2.collidepoint(mouse_pos) and not main_game.inventory_menu.fr_unlock[0]:
                    if main_game.inventory_menu.coin_amn - 5 >= 0:
                        main_game.inventory_menu.fr_unlock[0] = True
                        main_game.inventory_menu.coin_amn -= 5
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()

                if main_game.inventory_menu.fr_skin3_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.fr_unlock[1]:
                    main_game.inventory_menu.fr_skin_selection = 3
                elif main_game.inventory_menu.unlock_fr_button_rect3.collidepoint(mouse_pos) and not main_game.inventory_menu.fr_unlock[1]:
                    if main_game.inventory_menu.coin_amn - 15 >= 0:
                        main_game.inventory_menu.fr_unlock[1] = True
                        main_game.inventory_menu.coin_amn -= 15
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()

                if main_game.inventory_menu.fr_skin4_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.fr_unlock[2]:
                    main_game.inventory_menu.fr_skin_selection = 4
                elif main_game.inventory_menu.unlock_fr_button_rect4.collidepoint(mouse_pos) and not main_game.inventory_menu.fr_unlock[2]:
                    if main_game.inventory_menu.coin_amn - 25 >= 0:
                        main_game.inventory_menu.fr_unlock[2] = True
                        main_game.inventory_menu.coin_amn -= 25
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()

                if main_game.inventory_menu.fr_skin5_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.fr_unlock[3]:
                    main_game.inventory_menu.fr_skin_selection = 5
                elif main_game.inventory_menu.unlock_fr_button_rect5.collidepoint(mouse_pos) and not main_game.inventory_menu.fr_unlock[3]:
                    if main_game.inventory_menu.coin_amn - 35 >= 0:
                        main_game.inventory_menu.fr_unlock[3] = True
                        main_game.inventory_menu.coin_amn -= 35
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()

                if main_game.inventory_menu.fr_skin6_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.fr_unlock[4]:
                    main_game.inventory_menu.fr_skin_selection = 6
                elif main_game.inventory_menu.unlock_fr_button_rect6.collidepoint(mouse_pos) and not main_game.inventory_menu.fr_unlock[4]:
                    if main_game.inventory_menu.coin_amn - 45 >= 0:
                        main_game.inventory_menu.fr_unlock[4] = True
                        main_game.inventory_menu.coin_amn -= 45
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()

                if main_game.inventory_menu.fr_skin7_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.fr_unlock[5]:
                    main_game.inventory_menu.fr_skin_selection = 7
                elif main_game.inventory_menu.unlock_fr_button_rect7.collidepoint(mouse_pos) and not main_game.inventory_menu.fr_unlock[5]:
                    if main_game.inventory_menu.coin_amn - 45 >= 0:
                        main_game.inventory_menu.fr_unlock[5] = True
                        main_game.inventory_menu.coin_amn -= 45
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()

                if main_game.inventory_menu.fr_skin8_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.fr_unlock[6]:
                    main_game.inventory_menu.fr_skin_selection = 8
                elif main_game.inventory_menu.unlock_fr_button_rect8.collidepoint(mouse_pos) and not main_game.inventory_menu.fr_unlock[6]:
                    if main_game.inventory_menu.coin_amn - 45 >= 0:
                        main_game.inventory_menu.fr_unlock[6] = True
                        main_game.inventory_menu.coin_amn -= 45
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()

                if main_game.inventory_menu.fr_skin9_checkbox.collidepoint(mouse_pos) and main_game.inventory_menu.fr_unlock[7]:
                    main_game.inventory_menu.fr_skin_selection = 9
                elif main_game.inventory_menu.unlock_fr_button_rect9.collidepoint(mouse_pos) and not main_game.inventory_menu.fr_unlock[7]:
                    if main_game.inventory_menu.coin_amn - 65 >= 0:
                        main_game.inventory_menu.fr_unlock[7] = True
                        main_game.inventory_menu.coin_amn -= 65
                        main_game.inventory_menu.handle_save_click()
                    else:
                        main_game.oops = True
                        main_game.oops_start_time = pygame.time.get_ticks()
                        main_game.inventory_menu.save_changes()
                        pygame.display.update()

                if main_game.inventory_menu.save_button_rect.collidepoint(mouse_pos):
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
                    return
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
    