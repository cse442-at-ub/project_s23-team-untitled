import random
import sys
import pygame
from pygame.math import Vector2
from food_src import fruit_source

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number*cell_size))
icon = pygame.image.load('Graphics/snake.png')
clock = pygame.time.Clock()
food_src = pygame.image.load(fruit_source).convert_alpha()
plate_src = pygame.image.load('Graphics/fruit_basket.png').convert_alpha()
turtle_src = pygame.image.load('Graphics/turtle.png').convert_alpha()
game_font = pygame.font.Font('Font/bahnschrift.ttf', 30)
wall_segment = pygame.image.load('Graphics/wall_segment.png').convert_alpha()
score = pygame.image.load('Graphics/score.png').convert_alpha()
highest_scores = []
# return button
return_button = pygame.image.load('Buttons/button_return.png')
# buttons for selection page
level1_button = pygame.image.load('Buttons/button_easy.png')
level2_button = pygame.image.load('Buttons/button_medium.png')
level3_button = pygame.image.load('Buttons/button_hard.png')

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

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 200)

# for inventory
saved = None