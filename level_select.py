from level_1_exe import *
from level_2_exe import *
from level_3_exe import *
from game_elements import *

def selection():
    while True:
        screen.fill((179, 207, 178))
        selection_background(screen)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Snaking')
        return_image = pygame.transform.scale(return_button, (60, 60))
        return_rect = return_image.get_rect()
        return_rect.x = 10
        return_rect.y = 10
        level1_image = pygame.transform.scale(level1_button, (300, 100))
        level2_image = pygame.transform.scale(level2_button, (300, 100))
        level3_image = pygame.transform.scale(level3_button, (300, 100))
        level1_rect = level1_image.get_rect()
        level1_rect.x = 250
        level1_rect.y = 160
        level2_rect = level2_image.get_rect()
        level2_rect.x = 250
        level2_rect.y = 360
        level3_rect = level3_image.get_rect()
        level3_rect.x = 250
        level3_rect.y = 560

        screen.blit(return_image, return_rect)
        screen.blit(level1_image, level1_rect)
        screen.blit(level2_image, level2_rect)
        screen.blit(level3_image, level3_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and level1_rect.collidepoint(pos):
                main_game = MAIN1()
                main_game.game()
                if main_game.back_to_menu_flag == True:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN and level2_rect.collidepoint(pos):
                main_game = MAIN2()
                main_game.game()
                if main_game.back_to_menu_flag == True:
                    return
            
            if event.type == pygame.MOUSEBUTTONDOWN and level3_rect.collidepoint(pos):
                main_game = MAIN3()
                main_game.game()
                if main_game.back_to_menu_flag == True:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN and return_rect.collidepoint(pos):
                return

        pygame.display.update()
        clock.tick(60)
