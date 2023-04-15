import pygame
import os

pygame.init()

WINDOW_SIZE = (800, 600)
cell_size = 40
cell_number = WINDOW_SIZE[0] // cell_size

background_color = (175, 215, 70)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (201, 223, 201)


WINDOW_SIZE = (800, 600)

# 创建窗口
screen = pygame.display.set_mode(WINDOW_SIZE)

# 设置窗口标题
pygame.display.set_caption("new game")


font = pygame.font.Font(None, 36)

# 加载关卡按钮图片
level1_button = pygame.transform.scale(pygame.image.load('Graphics/button_easy.png'), (200, 50)).convert_alpha()
level2_button = pygame.transform.scale(pygame.image.load('Graphics/button_medium.png'), (200, 50)).convert_alpha()
level3_button = pygame.transform.scale(pygame.image.load('Graphics/button_hard.png'), (200, 50)).convert_alpha()
# 创建关卡1按钮矩形
level1_rect = level1_button.get_rect()
level1_rect.centerx = screen.get_rect().centerx
level1_rect.y = 200

# 创建关卡2按钮矩形
level2_rect = level2_button.get_rect()
level2_rect.centerx = screen.get_rect().centerx
level2_rect.y = 300

# 创建关卡3按钮矩形
level3_rect = level3_button.get_rect()
level3_rect.centerx = screen.get_rect().centerx
level3_rect.y = 400

# 加载返回按钮图片
return_button = pygame.transform.scale(pygame.image.load('Graphics/button_return.png'), (50, 50)).convert_alpha()

# 创建返回按钮矩形
return_rect = return_button.get_rect()
return_rect.x = 20
return_rect.y = 20
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
            if return_rect.collidepoint(event.pos):
                # 关闭窗口
                pygame.quit()
                exit()
            # 点击了关卡1按钮
            if level1_rect.collidepoint(event.pos):
                # 加载level_1.py文件
                os.system("python level_1.py")

            # 点击了关卡2按钮
            if level2_rect.collidepoint(event.pos):
                # 加载level2.py文件
                os.system("python level2.py")

            if level3_rect.collidepoint(event.pos):
                # 加载level2.py文件
                os.system("python level_3.py")

    # 绘制背景
    screen.fill(GREEN)

    # 绘制草地背景
    draw_grass()

    # 绘制关卡1按钮
    screen.blit(level1_button, level1_rect)

    # 绘制关卡2按钮
    screen.blit(level2_button, level2_rect)
    # 绘制关卡3按钮
    screen.blit(level3_button, level3_rect)
    screen.blit(return_button,return_rect)

    # 更新屏幕
    pygame.display.update()