# from level_1_exe import *
# from level_2_exe import *
import pygame
import sys
import random
import time
from pygame.math import Vector2

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number * cell_size))
icon = pygame.image.load('Graphics/snake.png')
clock = pygame.time.Clock()
level1_button = pygame.image.load('Graphics/level1_sample.png')
level2_button = pygame.image.load('Graphics/level2_sample.png')
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)


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


click = False


def selection():

    while True:
        screen.fill((179, 207, 178))
        selection_background(screen)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Snaking')
        level1_image = pygame.transform.scale(level1_button, (200, 50))
        level2_image = pygame.transform.scale(level2_button, (200, 50))
        level1_rect = level1_image.get_rect()
        level1_rect.x = 300
        level1_rect.y = 200
        level2_rect = level2_image.get_rect()
        level2_rect.x = 300
        level2_rect.y = 400

        pos = pygame.mouse.get_pos()
        if level1_rect.collidepoint(pos):
            if click:
                print("level1")
        if level2_rect.collidepoint(pos):
            if click:
                print("level2")

        screen.blit(level1_image, level1_rect)
        screen.blit(level2_image, level2_rect)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    selection()
