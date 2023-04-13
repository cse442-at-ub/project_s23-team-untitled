import pygame
import os

pygame.init()
#test

WINDOW_SIZE = (800, 600)
cell_size = 40
cell_number = WINDOW_SIZE[0] // cell_size


GREEN = (201, 223, 201)


screen = pygame.display.set_mode(WINDOW_SIZE)


pygame.display.set_caption("homepage")


find_button = pygame.transform.scale(pygame.image.load('Graphics/title_newgame.png'), (300, 100))


daily_challenge_button = pygame.transform.scale(pygame.image.load('Graphics/button_daily_highlight.png'), (300, 100))


scores_button = pygame.transform.scale(pygame.image.load('Graphics/button_score.png'), (300, 100))


inventory_button = pygame.transform.scale(pygame.image.load('Graphics/button_inventory.png'), (300, 100))


button_rect = find_button.get_rect()
button_rect.centerx = screen.get_rect().centerx
button_rect.centery = screen.get_rect().centery-100


daily_challenge_button_rect = daily_challenge_button.get_rect()
daily_challenge_button_rect.centerx = screen.get_rect().centerx
daily_challenge_button_rect.centery = screen.get_rect().centery - 225


scores_button_rect = scores_button.get_rect()
scores_button_rect.centerx = screen.get_rect().centerx
scores_button_rect.centery = screen.get_rect().centery +50


inventory_button_rect = inventory_button.get_rect()
inventory_button_rect.centerx = screen.get_rect().centerx
inventory_button_rect.centery = screen.get_rect().centery + 200


def draw_grass():
    grass_color = (181, 206, 181)
    for row in range(cell_number):
        if row % 2 == 0:
            for col in range(cell_number):
                if col % 2 == 0:
                    grass_rec = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rec)
        else:
            for col in range(cell_number):
                if col % 2 != 0:
                    grass_rec = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, grass_color, grass_rec)



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 关闭窗口
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # 点击了 "newgame" 按钮
            if button_rect.collidepoint(event.pos):
                # 加载 newgame_page.py 文件
                os.system("python newgame_page.py")

            if scores_button_rect.collidepoint(event.pos):

                os.system("python scoreboard.py")


    screen.fill(GREEN)


    draw_grass()


    pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), daily_challenge_button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), scores_button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), inventory_button_rect, 3)

    screen.blit(find_button, button_rect)
    screen.blit(daily_challenge_button, daily_challenge_button_rect)
    screen.blit(scores_button, scores_button_rect)
    screen.blit(inventory_button, inventory_button_rect)


    
    pygame.display.update()
