import os
import pickle
import random
import sys
import pygame
from pygame.math import Vector2
import time
import datetime

game_started = False
coins = 0

if not (os.path.exists('coins.bin')):
    # create binary coins file
    with open('coins.bin', 'wb') as file:
        pickle.dump(0, file)


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

        self.body_tr = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_bl.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_tl.png').convert_alpha()

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


class TASK:
    def __init__(self, title, task):
        pygame.init()
        self.title = title
        self.task = task
        self.font = pygame.font.SysFont("Arial", 30)
        self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode((self.width, self.height))

    def popup(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    global game_started
                    game_started = True
                    return False

            self.screen.fill((255, 255, 255))
            text_surface = self.font.render(self.title, True, (0, 0, 0))
            self.screen.blit(text_surface, (20, 20))
            text_surface = self.font.render(self.task, True, (0, 0, 0))
            self.screen.blit(text_surface, (20, 70))

            pygame.display.update()

    def continue_or_not(self):

        coins = main_game.read_bin('coins.bin') + 5
        main_game.write_bin('coins.bin', coins)
        print(coins)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 150 < event.pos[0] < 300 and 400 < event.pos[1] < 450:
                        # 点击“退出”按钮
                        pygame.quit()
                        quit()
                    elif 500 < event.pos[0] < 650 and 400 < event.pos[1] < 450:
                        # 点击“继续”按钮
                        return True

            self.screen.fill((255, 255, 255))
            text_surface = self.font.render("Congratulations! You have completed the task1!", True, (0, 0, 0))
            self.screen.blit(text_surface, (100, 200))

            text_surface = self.font.render("Current coins:" + str(5), True, (0, 0, 0))
            self.screen.blit(text_surface, (250, 250))

            text_surface = self.font.render("Total coins:" + str(coins), True, (0, 0, 0))
            self.screen.blit(text_surface, (250, 300))

            # 绘制“退出”按钮
            pygame.draw.rect(self.screen, (255, 0, 0), (150, 400, 150, 50))
            text_surface = self.font.render("Exit", True, (255, 255, 255))
            self.screen.blit(text_surface, (175, 410))

            # 绘制“继续”按钮
            pygame.draw.rect(self.screen, (0, 255, 0), (500, 400, 150, 50))
            text_surface = self.font.render("Continue", True, (255, 255, 255))
            self.screen.blit(text_surface, (515, 410))

            pygame.display.update()


class TASK2:
    def __init__(self, title, description):
        pygame.init()
        self.title = title
        self.task = description
        self.font = pygame.font.SysFont("Arial", 30)
        self.width, self.height = 800, 800
        self.screen = pygame.display.set_mode((self.width, self.height))

    def popup(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    global game_started
                    game_started = True
                    return False

            self.screen.fill((255, 255, 255))
            text_surface = self.font.render(self.title, True, (0, 0, 0))
            self.screen.blit(text_surface, (20, 20))
            text_surface = self.font.render(self.task, True, (0, 0, 0))
            self.screen.blit(text_surface, (20, 70))

            pygame.display.update()


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.wall = WALL(self.snake)
        self.powerup = POWERUP()
        self.score = 0
        self.start_time = pygame.time.get_ticks()
        self.task_completed = False
        self.task2_completed = False
        self.task_switch_time = 1 * 60 * 1000  # 10分钟
        self.got_current_time = False
        self.current_time = 0

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        # self.check_task()
        # self.check_task2()

    # def check_task(self):
    #     if self.score >= 5 and not self.task_completed:
    #         self.task_completed = True
    #         TASK("Congratulations", "You have completed the task1!").popup()
    #
    # def check_task2(self):
    #     current_time = pygame.time.get_ticks()
    #     if current_time - self.start_time >= 20 * 1000 and not self.task2_completed:
    #         self.task2_completed = True
    #         TASK2("Congratulations", "You have completed Task 2!").popup()

    def update_tasks(self):

        # print("Updating tasks")

        if not self.got_current_time:
            self.current_time = pygame.time.get_ticks()
            self.got_current_time = True
        else:
            current_time = self.current_time

        # print("Current time: ", self.current_time)

        # record the current minute
        current_minute = datetime.datetime.now().day

        # check if the current minute is odd
        is_odd_minute = current_minute % 2 == 1

        # Task 1: player needs to get a score of 5
        if is_odd_minute and not self.task_completed:
            # print("Task 1")
            if self.score >= 5:
                self.task_completed = True
                print("Task 1 completed!")
                TASK("Congratulations", "You have completed the task1!").continue_or_not()

        # Task 2: player needs to survive for 5 seconds
        if not is_odd_minute and not self.task2_completed:
            # print("Task 2")
            # print(pygame.time.get_ticks() - self.current_time)
            if pygame.time.get_ticks() - self.current_time >= 5 * 1000:
                self.task2_completed = True
                print("Task 2 completed!")
                TASK2("Congratulations", "You have completed Task 2!").popup()

    def check_switch_task(self, task1_description, task2_description):
        print("check_switch_task")

        self.task_completed = False
        self.task2_completed = False

        current_minute = datetime.datetime.now().day
        is_odd_minute = current_minute % 2 == 1

        if is_odd_minute:
            print("Task 1")
            TASK("Today's Task", task1_description).popup()
        else:
            print("Task 2")
            TASK2("Today's Task 2", task2_description).popup()

    def draw_elements(self):
        self.draw_grass()
        self.snake.draw_snake()
        self.draw_score()
        self.wall.draw_wall()

    def draw_powerup(self):
        self.powerup.draw_powerup()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.score += 1
            # self.random_num = random.random()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

        if self.powerup.pos == self.snake.body[0]:
            self.powerup.randomize()
            self.snake.add_block()
            self.score += 3

        for block in self.snake.body[1:]:
            if block == self.powerup.pos:
                self.powerup.randomize()

        # eat on the wall, NO
        for block in self.wall.wall_blocks:
            if block == self.fruit.pos:
                self.fruit.randomize()
        for block in self.wall.wall_blocks:
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
        self.score = 0

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
        score_text = str(self.score)
        # print(score_text)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 700)
        score_y = int(cell_size * cell_number - 750)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = score.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                              apple_rect.height)
        pygame.draw.rect(screen, (201, 223, 201), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(score, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

    def read_bin(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

    def write_bin(self, filename, data):
        with open(filename, 'wb') as file:
            pickle.dump(data, file)


if __name__ == "__main__":

    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    cell_size = 40
    cell_number = 20
    screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
    icon = pygame.image.load('Graphics/snake.png')
    clock = pygame.time.Clock()
    apple = pygame.image.load('Graphics/coin.png').convert_alpha()
    fruit_plate = pygame.image.load('Graphics/new3coins.png').convert_alpha()
    score = pygame.image.load('Graphics/coin.png').convert_alpha()
    game_font = pygame.font.Font('Font/bahnschrift.ttf', 25)
    wall_segment = pygame.image.load('Graphics/wall_segment.png').convert_alpha()

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    main_game = MAIN()

    last_randomize_time = pygame.time.get_ticks()

    main_game.check_switch_task("Get 5 coins", "survive for 5 seconds")

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

        if main_game.score % 5 == 0:
            main_game.powerup.draw_powerup()
        else:
            main_game.fruit.draw_fruit()

        pygame.display.set_icon(icon)
        pygame.display.set_caption('Snake')
        pygame.display.update()
        clock.tick(60)

        if pygame.time.get_ticks() - last_randomize_time >= 5000:
            main_game.wall.randomize()
            last_randomize_time = pygame.time.get_ticks()

        if game_started:
            main_game.update_tasks()