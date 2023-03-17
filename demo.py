import pygame
import random
import sys
from pygame.math import Vector2


class WALL:
    def __init__(self, snake):
        self.snake = snake
        self.wall_blocks = []
        self.randomize()

    def randomize(self):
        self.wall_blocks = []
        wall_numbers = 1  # how many wall groups
        for i in range(wall_numbers):
            # Generate first wall
            start_x = random.randint(1, cell_number - 3)
            start_y = random.randint(1, cell_number - 3)
            direction = random.choice([Vector2(1, 0), Vector2(0, 1)])
            wall_shape = "line"
            # wall_shape = random.choice(["line", "L_shape"])
            num_walls = random.randint(1, 2)

            if wall_shape == "line":
                for i in range(num_walls):
                    obstacle_pos = Vector2(start_x, start_y) + i * direction
                    while obstacle_pos in self.wall_blocks or obstacle_pos in self.snake.body:
                        start_x = random.randint(1, cell_number - 3)
                        start_y = random.randint(1, cell_number - 3)
                        direction = random.choice([Vector2(1, 0), Vector2(0, 1)])
                        obstacle_pos = Vector2(start_x, start_y) + i * direction
                    self.wall_blocks.append(obstacle_pos)
            #   "L_shape"
            # else:
            #     if direction == Vector2(1, 0):
            #         for i in range(num_walls):
            #             if i == 0:
            #                 obstacle_pos = Vector2(start_x, start_y)
            #             elif i == 1:
            #                 obstacle_pos = Vector2(start_x, start_y + 1)
            #             else:
            #                 obstacle_pos = Vector2(start_x + i - 1, start_y + 1)
            #             while obstacle_pos in self.wall_blocks or obstacle_pos in self.snake.body:
            #                 start_x = random.randint(1, cell_number - 3)
            #                 start_y = random.randint(1, cell_number - 3)
            #                 obstacle_pos = Vector2(start_x, start_y + 1)
            #             self.wall_blocks.append(obstacle_pos)
            #     else: # direction == Vector2(0, 1)
            #         for i in range(num_walls):
            #             if i == 0:
            #                 obstacle_pos = Vector2(start_x, start_y)
            #             elif i == 1:
            #                 obstacle_pos = Vector2(start_x + 1, start_y)
            #             else:
            #                 obstacle_pos = Vector2(start_x + 1, start_y + i - 1)
            #             while obstacle_pos in self.wall_blocks or obstacle_pos in self.snake.body:
            #                 start_x = random.randint(1, cell_number - 3)
            #                 start_y = random.randint(1, cell_number - 3)
            #                 obstacle_pos = Vector2(start_x + 1, start_y)
            #             self.wall_blocks.append(obstacle_pos)

    def draw_wall(self):
        for block in self.wall_blocks:
            wall_square = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            screen.blit(wall_segment, wall_square)

class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_u.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_d.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_r.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_l.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_d.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_u.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_l.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_r.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_v.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_h.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics//body_br.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics//body_bl.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics//body_tr.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics//body_tl.png').convert_alpha()

    def draw_snake(self):
        # for block in self.body:
        #     x_pos = int(block.x * cell_size)
        #     y_pos = int(block.y * cell_size)
        #     block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)
        #     pygame.draw.rect(screen,(183,111,122),block_rect)
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)
                # pygame.draw.rect(screen,(150,100,100),block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rec = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rec)
        # pygame.draw.rect(screen,(126,166,114),fruit_rec)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class POWERUP:
    def __init__(self):
        self.randomize()

    def draw_powerup(self):
        powerup_rec = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(fruit_plate, powerup_rec)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.wall = WALL(self.snake)
        self.powerup = POWERUP()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.powerup.draw_powerup()
        self.snake.draw_snake()
        self.draw_score()
        self.wall.draw_wall()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

        if self.powerup.pos == self.snake.body[0]:
            self.powerup.randomize()
            self.snake.add_block()

        for block in self.snake.body[1:]:
            if block == self.powerup.pos:
                self.powerup.randomize()

    def check_fail(self):
        if (not 0 <= self.snake.body[0].x < cell_number) or (not 0 <= self.snake.body[0].y < cell_number):
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

        for block in self.wall.wall_blocks:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (201, 223, 201)
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

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        # print(score_text)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 700)
        score_y = int(cell_size * cell_number -750)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = score.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                              apple_rect.height)
        pygame.draw.rect(screen, (201, 223, 201), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(score, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
icon = pygame.image.load('Graphics/snake.png')
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/banana.png').convert_alpha()
fruit_plate = pygame.image.load('Graphics/fruit_basket.png').convert_alpha()
score = pygame.image.load('Graphics/score.png').convert_alpha()
game_font = pygame.font.Font('Font/bahnschrift.ttf', 25)
wall_segment =pygame.image.load('Graphics/wall_segment.png').convert_alpha()



SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    screen.fill((179, 207, 178))

    main_game.draw_elements()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Snaking')
    pygame.display.update()
    clock.tick(60)