import random
import sys
import pygame

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode(
    (cell_number * cell_size, cell_number*cell_size))
icon = pygame.image.load('Graphics/snake.png')
clock = pygame.time.Clock()
food_src = pygame.image.load('Graphics/apple_39.png').convert_alpha()
plate_src = pygame.image.load('Graphics/fruit_basket.png').convert_alpha()
turtle_src = pygame.image.load('Graphics/turtle.png').convert_alpha()
game_font = pygame.font.Font('Font/bahnschrift.ttf', 30)
wall_segment = pygame.image.load('Graphics/wall_segment.png').convert_alpha()
score = pygame.image.load('Graphics/score.png').convert_alpha()

# buttons for selection page
level1_button = pygame.image.load('Graphics/level1_sample.png')
level2_button = pygame.image.load('Graphics/level2_sample.png')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 200)
