from level_1_exe import *
from level_2_exe import *
from level_3_exe import *
from game_elements import *


def selection_background(screen):
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


def selection():

    while True:
        screen.fill((179, 207, 178))
        selection_background(screen)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Snaking')
        level1_image = pygame.transform.scale(level1_button, (200, 50))
        level2_image = pygame.transform.scale(level2_button, (200, 50))
        level3_image = pygame.transform.scale(level3_button, (200, 50))
        level1_rect = level1_image.get_rect()
        level1_rect.x = 300
        level1_rect.y = 200
        level2_rect = level2_image.get_rect()
        level2_rect.x = 300
        level2_rect.y = 400
        level3_rect = level3_image.get_rect()
        level3_rect.x = 300
        level3_rect.y = 600

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

            if event.type == pygame.MOUSEBUTTONDOWN and level2_rect.collidepoint(pos):
                main_game = MAIN2()
                main_game.game()
            
            if event.type == pygame.MOUSEBUTTONDOWN and level3_rect.collidepoint(pos):
                main_game = MAIN3()
                main_game.game()

        pygame.display.update()
        clock.tick(60)
