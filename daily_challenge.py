import datetime
import os
import pickle
import random
import sys
import pygame
from pygame.math import Vector2
from game_elements import *

game_started = False
coins = 0
todays_goal_coin = 0

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

        self.head_up = head_up
        self.head_down = head_down
        self.head_right = head_right
        self.head_left = head_left

        self.tail_up = tail_up
        self.tail_down = tail_down
        self.tail_right = tail_right
        self.tail_left = tail_left

        self.body_vertical = body_vertical
        self.body_horizontal = body_horizontal

        self.body_tr = body_tr
        self.body_tl = body_tl
        self.body_bl = body_bl
        self.body_br = body_br

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
    def __init__(self, snake, wall):
        self.snake = snake
        self.wall = wall
        self.randomize()

    def draw_fruit(self):
        fruit_rec = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(coin_single, fruit_rec)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class POWERUP:
    def __init__(self,snake,wall):
        self.snake = snake
        self.wall = wall
        self.randomize()

    def draw_powerup(self):
        powerup_rec = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(coin_plate, powerup_rec)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)



# class TASK2:
#     def __init__(self, title, description):
#         pygame.init()
#         self.title = title
#         self.task = description
#         self.font = pygame.font.SysFont("Arial", 30)
#         self.width, self.height = 800, 800
#         self.screen = pygame.display.set_mode((self.width, self.height))
#         self.description = "survive for 5 seconds"

#     def popup(self):
#         while True:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     quit()
#                 if event.type == pygame.KEYDOWN:
#                     global game_started
#                     game_started = True
#                     return False

#             self.screen.fill((255, 255, 255))
#             text_surface = self.font.render(self.title, True, (0, 0, 0))
#             self.screen.blit(text_surface, (20, 20))
#             text_surface = self.font.render(self.task, True, (0, 0, 0))
#             self.screen.blit(text_surface, (20, 70))

#             pygame.display.update()


class MAIN:
    def __init__(self):
        global head_up, head_down, head_right, head_left, tail_up, tail_down, tail_right, tail_left, body_vertical, body_horizontal, body_tr, body_tl, body_bl, body_br
        with open('skin_selections.txt', 'r') as f:
            lines = f.readlines()
            sn_skin_slection = int(lines[0])

        if sn_skin_slection == 1:
            head_up = pygame.image.load('Graphics/head_u.png').convert_alpha()
            head_down = pygame.image.load(
                'Graphics/head_d.png').convert_alpha()
            head_right = pygame.image.load(
                'Graphics/head_r.png').convert_alpha()
            head_left = pygame.image.load(
                'Graphics/head_l.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d.png').convert_alpha()
            tail_down = pygame.image.load(
                'Graphics/tail_u.png').convert_alpha()
            tail_right = pygame.image.load(
                'Graphics/tail_l.png').convert_alpha()
            tail_left = pygame.image.load(
                'Graphics/tail_r.png').convert_alpha()
            body_vertical = pygame.image.load(
                'Graphics/body_v.png').convert_alpha()
            body_horizontal = pygame.image.load(
                'Graphics/body_h.png').convert_alpha()
            body_tr = pygame.image.load(
                'Graphics//body_br.png').convert_alpha()
            body_tl = pygame.image.load(
                'Graphics//body_bl.png').convert_alpha()
            body_bl = pygame.image.load(
                'Graphics//body_tr.png').convert_alpha()
            body_br = pygame.image.load(
                'Graphics//body_tl.png').convert_alpha()
        elif sn_skin_slection == 2:
            head_up = pygame.image.load('Graphics/head_u2.png').convert_alpha()
            head_down = pygame.image.load(
                'Graphics/head_d2.png').convert_alpha()
            head_right = pygame.image.load(
                'Graphics/head_r2.png').convert_alpha()
            head_left = pygame.image.load(
                'Graphics/head_l2.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d2.png').convert_alpha()
            tail_down = pygame.image.load(
                'Graphics/tail_u2.png').convert_alpha()
            tail_right = pygame.image.load(
                'Graphics/tail_l2.png').convert_alpha()
            tail_left = pygame.image.load(
                'Graphics/tail_r2.png').convert_alpha()
            body_vertical = pygame.image.load(
                'Graphics/body_v2.png').convert_alpha()
            body_horizontal = pygame.image.load(
                'Graphics/body_h2.png').convert_alpha()
            body_tr = pygame.image.load(
                'Graphics//body_br2.png').convert_alpha()
            body_tl = pygame.image.load(
                'Graphics//body_bl2.png').convert_alpha()
            body_bl = pygame.image.load(
                'Graphics//body_tr2.png').convert_alpha()
            body_br = pygame.image.load(
                'Graphics//body_tl2.png').convert_alpha()
        elif sn_skin_slection == 3:
            head_up = pygame.image.load('Graphics/head_u3.png').convert_alpha()
            head_down = pygame.image.load(
                'Graphics/head_d3.png').convert_alpha()
            head_right = pygame.image.load(
                'Graphics/head_r3.png').convert_alpha()
            head_left = pygame.image.load(
                'Graphics/head_l3.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d3.png').convert_alpha()
            tail_down = pygame.image.load(
                'Graphics/tail_u3.png').convert_alpha()
            tail_right = pygame.image.load(
                'Graphics/tail_l3.png').convert_alpha()
            tail_left = pygame.image.load(
                'Graphics/tail_r3.png').convert_alpha()
            body_vertical = pygame.image.load(
                'Graphics/body_v3.png').convert_alpha()
            body_horizontal = pygame.image.load(
                'Graphics/body_h3.png').convert_alpha()
            body_tr = pygame.image.load(
                'Graphics//body_br3.png').convert_alpha()
            body_tl = pygame.image.load(
                'Graphics//body_bl3.png').convert_alpha()
            body_bl = pygame.image.load(
                'Graphics//body_tr3.png').convert_alpha()
            body_br = pygame.image.load(
                'Graphics//body_tl3.png').convert_alpha()
        elif sn_skin_slection == 4:
            head_up = pygame.image.load('Graphics/head_u4.png').convert_alpha()
            head_down = pygame.image.load(
                'Graphics/head_d4.png').convert_alpha()
            head_right = pygame.image.load(
                'Graphics/head_r4.png').convert_alpha()
            head_left = pygame.image.load(
                'Graphics/head_l4.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d4.png').convert_alpha()
            tail_down = pygame.image.load(
                'Graphics/tail_u4.png').convert_alpha()
            tail_right = pygame.image.load(
                'Graphics/tail_l4.png').convert_alpha()
            tail_left = pygame.image.load(
                'Graphics/tail_r4.png').convert_alpha()
            body_vertical = pygame.image.load(
                'Graphics/body_v4.png').convert_alpha()
            body_horizontal = pygame.image.load(
                'Graphics/body_h4.png').convert_alpha()
            body_tr = pygame.image.load(
                'Graphics//body_br4.png').convert_alpha()
            body_tl = pygame.image.load(
                'Graphics//body_bl4.png').convert_alpha()
            body_bl = pygame.image.load(
                'Graphics//body_tr4.png').convert_alpha()
            body_br = pygame.image.load(
                'Graphics//body_tl4.png').convert_alpha()
        else:
            head_up = pygame.image.load('Graphics/head_u5.png').convert_alpha()
            head_down = pygame.image.load(
                'Graphics/head_d5.png').convert_alpha()
            head_right = pygame.image.load(
                'Graphics/head_r5.png').convert_alpha()
            head_left = pygame.image.load(
                'Graphics/head_l5.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d5.png').convert_alpha()
            tail_down = pygame.image.load(
                'Graphics/tail_u5.png').convert_alpha()
            tail_right = pygame.image.load(
                'Graphics/tail_l5.png').convert_alpha()
            tail_left = pygame.image.load(
                'Graphics/tail_r5.png').convert_alpha()
            body_vertical = pygame.image.load(
                'Graphics/body_v5.png').convert_alpha()
            body_horizontal = pygame.image.load(
                'Graphics/body_h5.png').convert_alpha()
            body_tr = pygame.image.load(
                'Graphics//body_br5.png').convert_alpha()
            body_tl = pygame.image.load(
                'Graphics//body_bl5.png').convert_alpha()
            body_bl = pygame.image.load(
                'Graphics//body_tr5.png').convert_alpha()
            body_br = pygame.image.load(
                'Graphics//body_tl5.png').convert_alpha()
        self.snake = SNAKE()
        self.wall = WALL(self.snake)
        self.fruit = FRUIT(self.snake, self.wall)
        self.powerup = POWERUP(self.snake, self.wall)
        self.score = 0
        self.start_time = pygame.time.get_ticks()
        self.task_completed = False
        self.task2_completed = False
        self.task_switch_time = 1 * 60 * 1000 # 10 mins
        self.got_current_time = False
        self.current_time = 0
        self.game_over_flag = False
        self.back_to_menu_flag = False
        self.btm_after_task_flag = False

        if os.path.exists("sound.bin"):
            with open("sound.bin", "rb") as f:
                sound_flag = pickle.load(f)
            if sound_flag:
                pygame.mixer.music.load(game_sound)
                pygame.mixer.music.play(-1)
        
        

    def update(self):
        self.snake.move_snake()
        if self.score % 5 == 0:
            self.check_collision_coins()
        else:
            self.check_collision_coin()
        self.check_fail()


    def draw_elements(self):
        self.draw_grass()
        if self.score % 5 == 0:
            self.powerup.draw_powerup()
        else:
            self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.wall.draw_wall()

    def check_collision_coin(self):
        if self.fruit.pos == self.snake.body[0]:
            if os.path.exists("sound.bin"):
                with open("sound.bin", "rb") as f:
                    sound_flag = pickle.load(f)
                if sound_flag:
                    pygame.mixer.Sound.play(coin_sound)
            self.score += 1
            self.fruit.randomize()
            self.snake.add_block()

        combine_list = self.snake.body[1:] + self.wall.wall_blocks
        for block in combine_list:
            if block == self.fruit.pos:
                self.fruit.randomize()


    def check_collision_coins(self):
        if self.powerup.pos == self.snake.body[0]:
            if os.path.exists("sound.bin"):
                with open("sound.bin", "rb") as f:
                    sound_flag = pickle.load(f)
                if sound_flag:
                    pygame.mixer.Sound.play(coin_sound)
            self.score += 3
            self.powerup.randomize()
            self.snake.add_block()
        combine_list = self.snake.body[1:] + self.wall.wall_blocks
        for block in combine_list:
            if block == self.powerup.pos:
                self.powerup.randomize()

    def check_fail(self):
        if (not 0 <= self.snake.body[0].x < cell_number) or (not 0 <= self.snake.body[0].y < cell_number):
            self.game_over_flag = True
            
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                if self.score >=1:
                    self.game_over_flag = True
                self.snake.reset()

        for block in self.wall.wall_blocks:
            if block == self.snake.body[0]:
                self.game_over_flag = True

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
        score_y = int(cell_size * cell_number - 760)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = score.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                              apple_rect.height)
        pygame.draw.rect(screen, (201, 223, 201), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(coin_score, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

    # def read_bin(self, filename):
    #     with open(filename, 'rb') as file:
    #         return pickle.load(file)

    # def write_bin(self, filename, data):
    #     with open(filename, 'wb') as file:
    #         pickle.dump(data, file)
    
    def game_over_screen(self):
        if os.path.exists("sound.bin"):
                with open("sound.bin", "rb") as f:
                    sound_flag = pickle.load(f)
                if sound_flag:
                    pygame.mixer.Sound.play(game_over_sound)
        # global highest_scores
        # if self.game_over_flag:
        # highest_scores.append(self.snake.food_gain)
        # highest_scores.sort(reverse=True)
        # highest_scores = highest_scores[:5]
        # Load game over image and resize it to fit background rectangle size

        game_over_image = pygame.image.load(
            'Graphics/game_over.png').convert_alpha()
        game_over_rect = game_over_image.get_rect(
            center=screen.get_rect().center)
        bg_rect = game_over_rect.copy()
        #game_over_image = pygame.transform.scale(game_over_image, (bg_rect.w, bg_rect.h))
        game_over_rect.y -= 150  # Move the game over image up
        # Move the game over image to the right

        # Load restart and main menu buttons
        restart_button = pygame.image.load(
            'Buttons/restart.png').convert_alpha()
        restart_highlighted_button = pygame.image.load(
            'Buttons/restart_highlight.png').convert_alpha()
        restart_rect = restart_button.get_rect(center=screen.get_rect().center)
        restart_rect.y += 80  # Move the restart button down
        restart_highlighted_rect = restart_highlighted_button.get_rect(
            center=restart_rect.center)
        restart_highlighted = False

        main_menu_button = pygame.image.load(
            'Buttons/main_menu.png').convert_alpha()
        main_menu_highlighted_button = pygame.image.load(
            'Buttons/main_menu_hightlight.png').convert_alpha()
        main_menu_rect = main_menu_button.get_rect(
            center=screen.get_rect().center)
        main_menu_rect.y += 200  # Move the main menu button down
        main_menu_highlighted_button_rec = main_menu_highlighted_button.get_rect(
            center=main_menu_rect.center)
        main_menu_highlighted = False

        # Create background rectangle
        bg_rect = game_over_rect.union(restart_rect).union(main_menu_rect)
        # Expand the background rectangle to fit the buttons
        bg_rect.inflate_ip(70, 80)
        bg_rect.center = screen.get_rect().center

        # Draw background rectangle, game over image, and buttons
        pygame.draw.rect(screen, (160, 198, 160), bg_rect, border_radius=30)
        pygame.draw.rect(screen, (0, 0, 0), bg_rect, border_radius=30, width=3)
        screen.blit(game_over_image, game_over_rect)
        screen.blit(restart_button, restart_rect)
        screen.blit(main_menu_button, main_menu_rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(event.pos):
                    self.__init__()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and main_menu_rect.collidepoint(event.pos):
                    self.back_to_menu_flag = True
                    pygame.mixer.music.stop()
                    return

                mouse_pos = pygame.mouse.get_pos()
                if restart_rect.collidepoint(mouse_pos):
                    restart_highlighted = True
                else:
                    restart_highlighted = False

                if main_menu_rect.collidepoint(mouse_pos):
                    main_menu_highlighted = True
                else:
                    main_menu_highlighted = False

                if restart_highlighted:
                    screen.blit(restart_highlighted_button,
                                restart_highlighted_rect)
                else:
                    screen.blit(restart_button, restart_rect)

                if main_menu_highlighted:
                    screen.blit(main_menu_highlighted_button,
                                main_menu_highlighted_button_rec)
                else:
                    screen.blit(main_menu_button, main_menu_rect)

            pygame.display.update()

    def popup(self):
        now = datetime.datetime.now()

        # retrieve the current month and day
        month = now.month
        day = now.day

        # multiply the month by the day
        result = int(month + day)

        global todays_goal_coin
        todays_goal_coin = result
        task_description = "Today's task is to get " + str(result) + " coins"
        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE, 150)
        while True:
            screen.fill((179, 207, 178))
            selection_background(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    if self.back_to_menu_flag or self.btm_after_task_flag:
                        return
                if event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(event.pos):
                    # play
                    global game_started
                    game_started = True
                    self.game()
                    
                if event.type == pygame.MOUSEBUTTONDOWN and main_menu_rect.collidepoint(event.pos):
                    # exit to main menu
                    pygame.mixer.music.stop()
                    return


            # self.screen.fill((255, 255, 255))
            # text_surface = self.font.render(self.title, True, (0, 0, 0))
            # self.screen.blit(text_surface, (20, 20))
            # text_surface = self.font.render(self.task, True, (0, 0, 0))
            # self.screen.blit(text_surface, (20, 70))

            game_over_image = pygame.image.load('Buttons/button_daily.png').convert_alpha()
            text = bo_font.render(task_description, True, (0, 0, 0))

            game_over_rect = game_over_image.get_rect(center=screen.get_rect().center)
            game_over_rect.y -= 150

            restart_button = pygame.image.load('Buttons/button_play.png').convert_alpha()
            restart_button = pygame.transform.scale(restart_button, (300, 85))
            restart_highlighted_button = pygame.image.load('Buttons/button_play_highlight.png').convert_alpha()
            restart_rect = restart_button.get_rect(center=screen.get_rect().center)
            restart_rect.y += 80
            restart_highlighted_rect = restart_highlighted_button.get_rect(center=restart_rect.center)
            restart_highlighted = False
            main_menu_button = pygame.image.load('Buttons/button_exit_to_desktop.png').convert_alpha()
            main_menu_highlighted_button = pygame.image.load('Buttons/button_return_highlight.png').convert_alpha()
            main_menu_rect = main_menu_button.get_rect(center=screen.get_rect().center)
            main_menu_rect.y += 200
            main_menu_highlighted_button_rec = main_menu_highlighted_button.get_rect(center=main_menu_rect.center)
            main_menu_highlighted = False

            bg_rect = game_over_rect.union(restart_rect).union(main_menu_rect)
            bg_rect.inflate_ip(70, 80)
            bg_rect.center = screen.get_rect().center

            pygame.draw.rect(screen, (160, 198, 160), bg_rect, border_radius=30)
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, border_radius=30, width=3)
            # screen.blit(game_over_image, game_over_rect)
            screen.blit(restart_button, restart_rect)
            screen.blit(main_menu_button, main_menu_rect)
            screen.blit(text, (250, 250))

            # screen.fill((179, 207, 178))
            # text_surface = self.font.render(self.title, True, (0, 0, 0))
            # self.screen.blit(text_surface, (20, 20))
            # text_surface = self.font.render(self.task, True, (0, 0, 0))
            # self.screen.blit(text_surface, (20, 70))

            pygame.display.update()
        

    def game(self):
        SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(SCREEN_UPDATE, 150)
        last_randomize_time = pygame.time.get_ticks()
        # self.check_switch_task("Get 5 coins", "survive for 5 seconds")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    self.update()
                    if game_started:
                        global todays_goal_coin
                        if self.score >= todays_goal_coin and self.task_completed == False:
                            self.task_completed = True
                            # print("Task 1 completed!")
                            # TASK("Congratulations", "You have completed the task1!").continue_or_not()
                            self.continue_or_not()
                            # self.update_tasks()
                    if self.game_over_flag:
                        pygame.mixer.music.stop()
                        self.game_over_screen()
                        if self.back_to_menu_flag:
                            return
                    if self.btm_after_task_flag:
                        return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0, -1)
                    if event.key == pygame.K_RIGHT:
                        if self.snake.direction.x != -1:
                            self.snake.direction = Vector2(1, 0)
                    if event.key == pygame.K_DOWN:
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0, 1)
                    if event.key == pygame.K_LEFT:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1, 0)

            screen.fill((179, 207, 178))
            self.draw_elements()
            pygame.display.set_icon(icon)
            pygame.display.set_caption('Snake')
            pygame.display.update()
            clock.tick(60)

            if pygame.time.get_ticks() - last_randomize_time >= 5000:
                self.wall.randomize()
                last_randomize_time = pygame.time.get_ticks()

            # if game_started:
            #     self.update_tasks()


    def continue_or_not(self):
        global todays_goal_coin
        # load the coins
        with open('coins.bin', 'rb') as file:
            coins = pickle.load(file) + todays_goal_coin
        # save the coins
        with open('coins.bin', 'wb') as file:
            pickle.dump(coins, file)
        # load the sound flag
        if os.path.exists("sound.bin"):
            with open("sound.bin", "rb") as f:
                sound_flag = pickle.load(f)
            if sound_flag:
                pygame.mixer.Sound.play(congra_sound)

        print(coins)
        # SCREEN_UPDATE = pygame.USEREVENT
        # pygame.time.set_timer(SCREEN_UPDATE, 150)
        while True:
            screen.fill((179, 207, 178))
            selection_background(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and main_menu_rect.collidepoint(event.pos):
                    # back to mainmenu
                    pygame.mixer.music.stop()
                    self.btm_after_task_flag = True
                    return
                if event.type == pygame.MOUSEBUTTONDOWN and restart_rect.collidepoint(event.pos):
                    # play the game
                    global game_started
                    game_started = True
                    return 

            # self.screen.fill((255, 255, 255))
            # text_surface = self.font.render(self.title, True, (0, 0, 0))
            # self.screen.blit(text_surface, (20, 20))
            # text_surface = self.font.render(self.task, True, (0, 0, 0))
            # self.screen.blit(text_surface, (20, 70))

            game_over_image = pygame.image.load('Buttons/button_daily.png').convert_alpha()
            # text = bo_font.render(self.description, True, (0, 0, 0))

            game_over_rect = game_over_image.get_rect(center=screen.get_rect().center)
            game_over_rect.y -= 150

            restart_button = pygame.image.load('Buttons/button_play.png').convert_alpha()
            restart_button = pygame.transform.scale(restart_button, (300, 85))
            restart_highlighted_button = pygame.image.load('Buttons/button_play_highlight.png').convert_alpha()
            restart_rect = restart_button.get_rect(center=screen.get_rect().center)
            restart_rect.y += 80
            restart_highlighted_rect = restart_highlighted_button.get_rect(center=restart_rect.center)
            restart_highlighted = False
            main_menu_button = pygame.image.load('Buttons/button_exit_to_desktop.png').convert_alpha()
            # main_menu_highlighted_button = pygame.image.load('Buttons/button_return_highlight.png').convert_alpha()
            main_menu_rect = main_menu_button.get_rect(center=screen.get_rect().center)
            main_menu_rect.y += 200
            # main_menu_highlighted_button_rec = main_menu_highlighted_button.get_rect(center=main_menu_rect.center)
            # main_menu_highlighted = False

            bg_rect = game_over_rect.union(restart_rect).union(main_menu_rect)
            bg_rect.inflate_ip(70, 80)
            bg_rect.center = screen.get_rect().center

            pygame.draw.rect(screen, (160, 198, 160), bg_rect, border_radius=30)
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, border_radius=30, width=3)
            # screen.blit(game_over_image, game_over_rect)
            screen.blit(restart_button, restart_rect)
            screen.blit(main_menu_button, main_menu_rect)
            #screen.blit(text, (170, 250))
            text_surface = bo_font.render("Current coins:" + str(todays_goal_coin), True, (0, 0, 0))
            screen.blit(text_surface, (250, 275))

            text_surface = bo_font.render("Total coins:" + str(coins), True, (0, 0, 0))
            screen.blit(text_surface, (250, 325))

            # screen.fill((179, 207, 178))
            text_surface = bo_font.render("Congratulations", True, (0, 0, 0))
            screen.blit(text_surface, (250, 175))
            text_surface = bo_font.render("You have completed the task1!", True, (0, 0, 0))
            screen.blit(text_surface, (250, 225))

            pygame.display.update()
        





# pygame.mixer.pre_init(44100, -16, 2, 512)
# pygame.init()
# cell_size = 40
# cell_number = 20
# screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
# icon = pygame.image.load('Graphics/snake.png')
# clock = pygame.time.Clock()
# apple = pygame.image.load('Graphics/coin.png').convert_alpha()
# fruit_plate = pygame.image.load('Graphics/new3coins.png').convert_alpha()
# coin_score = pygame.image.load('Graphics/coin.png').convert_alpha()
# game_font = pygame.font.Font('Font/bahnschrift.ttf', 30)
# bo_font = pygame.font.Font('Font/bo.ttf', 40)


# SCREEN_UPDATE = pygame.USEREVENT
# pygame.time.set_timer(SCREEN_UPDATE, 150)

# main_game = MAIN()

# last_randomize_time = pygame.time.get_ticks()

# main_game.check_switch_task("Get 5 coins", "survive for 5 seconds")

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == SCREEN_UPDATE:
#             main_game.update()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 if main_game.snake.direction.y != 1:
#                     main_game.snake.direction = Vector2(0, -1)
#             if event.key == pygame.K_RIGHT:
#                 if main_game.snake.direction.x != -1:
#                     main_game.snake.direction = Vector2(1, 0)
#             if event.key == pygame.K_DOWN:
#                 if main_game.snake.direction.y != -1:
#                     main_game.snake.direction = Vector2(0, 1)
#             if event.key == pygame.K_LEFT:
#                 if main_game.snake.direction.x != 1:
#                     main_game.snake.direction = Vector2(-1, 0)

#     screen.fill((179, 207, 178))
#     main_game.draw_elements()

#     if main_game.score % 5 == 0:
#         main_game.powerup.draw_powerup()
#     else:
#         main_game.fruit.draw_fruit()

#     pygame.display.set_icon(icon)
#     pygame.display.set_caption('Snake')
#     pygame.display.update()
#     clock.tick(60)

#     if pygame.time.get_ticks() - last_randomize_time >= 5000:
#         main_game.wall.randomize()
#         last_randomize_time = pygame.time.get_ticks()

#     if game_started:
#         main_game.update_tasks()
