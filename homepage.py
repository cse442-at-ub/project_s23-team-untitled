import pygame
import os

pygame.init()

# 定义窗口大小和格子大小
WINDOW_SIZE = (800, 600)
cell_size = 40
cell_number = WINDOW_SIZE[0] // cell_size

# 定义颜色
GREEN = (201, 223, 201)

# 创建窗口
screen = pygame.display.set_mode(WINDOW_SIZE)

# 设置窗口标题
pygame.display.set_caption("homepage")

# 加载图片
find_button = pygame.transform.scale(pygame.image.load('Graphics/title_newgame.png'), (150, 75))

# 加载 "daily_challenge" 按钮图片
daily_challenge_button = pygame.transform.scale(pygame.image.load('Graphics/button_daily_highlight.png'), (150, 75))

# 加载 "scores" 按钮图片
scores_button = pygame.transform.scale(pygame.image.load('Graphics/button_score.png'), (150, 75))

# 加载 "inventory" 按钮图片
inventory_button = pygame.transform.scale(pygame.image.load('Graphics/button_inventory.png'), (150, 75))

# 创建按钮矩形
button_rect = find_button.get_rect()
button_rect.centerx = screen.get_rect().centerx
button_rect.centery = screen.get_rect().centery-100

# 创建 "daily_challenge" 按钮矩形
daily_challenge_button_rect = daily_challenge_button.get_rect()
daily_challenge_button_rect.centerx = screen.get_rect().centerx
daily_challenge_button_rect.centery = screen.get_rect().centery - 200

# 创建 "scores" 按钮矩形
scores_button_rect = scores_button.get_rect()
scores_button_rect.centerx = screen.get_rect().centerx
scores_button_rect.centery = screen.get_rect().centery

# 创建 "inventory" 按钮矩形
inventory_button_rect = inventory_button.get_rect()
inventory_button_rect.centerx = screen.get_rect().centerx
inventory_button_rect.centery = screen.get_rect().centery + 100


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


# 游戏循环
while True:
    # 处理事件
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

 # 绘制背景
    screen.fill(GREEN)

    # 绘制草地背景
    draw_grass()

    # 绘制按钮矩形
    pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), daily_challenge_button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), scores_button_rect, 3)
    pygame.draw.rect(screen, (0, 0, 0), inventory_button_rect, 3)
    # 绘制按钮
    screen.blit(find_button, button_rect)
    screen.blit(daily_challenge_button, daily_challenge_button_rect)
    screen.blit(scores_button, scores_button_rect)
    screen.blit(inventory_button, inventory_button_rect)


    # 更新屏幕
    pygame.display.update()
