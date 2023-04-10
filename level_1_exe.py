import random
import sys
import pygame
from pygame.math import Vector2
from game_elements import *


class WALL1:
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
                        direction = random.choice(
                            [Vector2(1, 0), Vector2(0, 1)])
                        obstacle_pos = Vector2(
                            start_x, start_y) + i * direction
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
            wall_square = pygame.Rect(
                int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            screen.blit(wall_segment, wall_square)


class SNAKE1:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(1, 0)
        self.new_block = False
        self.score = 0

        self.head_up = pygame.image.load('Graphics/head_u.png').convert_alpha()
        self.head_down = pygame.image.load(
            'Graphics/head_d.png').convert_alpha()
        self.head_right = pygame.image.load(
            'Graphics/head_r.png').convert_alpha()
        self.head_left = pygame.image.load(
            'Graphics/head_l.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_d.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'Graphics/tail_u.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'Graphics/tail_l.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'Graphics/tail_r.png').convert_alpha()

        self.body_vertical = pygame.image.load(
            'Graphics/body_v.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'Graphics/body_h.png').convert_alpha()

        self.body_tr = pygame.image.load(
            'Graphics/body_br.png').convert_alpha()
        self.body_tl = pygame.image.load(
            'Graphics/body_bl.png').convert_alpha()
        self.body_bl = pygame.image.load(
            'Graphics/body_tr.png').convert_alpha()
        self.body_br = pygame.image.load(
            'Graphics/body_tl.png').convert_alpha()

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


class FRUIT1:
    def __init__(self, snake, wall):
        self.snake = snake
        self.wall = wall
        self.randomize()

    def draw_fruit(self):
        fruit_rec = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(food_src, fruit_rec)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class PLATE1:
    def __init__(self, snake, wall):
        self.snake = snake
        self.wall = wall
        self.randomize()

    def draw_plate(self):
        powerup_rec = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(plate_src, powerup_rec)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class TURTLE1:
    def __init__(self, snake, wall):
        self.snake = snake
        self.wall = wall
        self.randomize()

    def draw_turtle(self):
        fruit_rec = pygame.Rect(
            int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(turtle_src, fruit_rec)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN1:
    def __init__(self):
        self.snake = SNAKE1()
        self.wall = WALL1(self.snake)
        self.fruit = FRUIT1(self.snake, self.wall)
        self.plate = PLATE1(self.snake, self.wall)
        self.turtle = TURTLE1(self.snake, self.wall)
        self.game_over_flag = False
        self.back_to_menu_flag = False

    def update(self):
        self.snake.move_snake()
        if self.snake.score % 10 == 5:
            self.check_collision_plate()
        elif self.snake.score % 10 == 9:
            self.check_collision_turtle()
        else:
            self.check_collision_fruit()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        if self.snake.score % 10 == 5:
            self.plate.draw_plate()
        elif self.snake.score % 10 == 9:
            self.turtle.draw_turtle()
        else:
            self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.wall.draw_wall()
        self.draw_score()

    def check_collision_fruit(self):
        if self.fruit.pos == self.snake.body[0]:
            self.snake.score += 1
            self.fruit.randomize()
            self.snake.add_block()

        combine_list = self.snake.body[1:] + self.wall.wall_blocks
        for block in combine_list:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_collision_plate(self):
        if self.plate.pos == self.snake.body[0]:
            self.snake.score += 3
            self.plate.randomize()
            self.snake.add_block()
        combine_list = self.snake.body[1:] + self.wall.wall_blocks
        for block in combine_list:
            if block == self.plate.pos:
                self.plate.randomize()

    def check_collision_turtle(self):
        if self.turtle.pos == self.snake.body[0]:
            self.snake.score += 1
            self.turtle.randomize()
            self.snake.add_block()
            # random_speed
            random_speed = [130, 280]
            pygame.time.set_timer(SCREEN_UPDATE, random.choice(random_speed))

        combine_list = self.snake.body[1:] + self.wall.wall_blocks
        for block in combine_list:
            if block == self.turtle.pos:
                self.turtle.randomize()

    def check_fail(self):
        if (not 0 <= self.snake.body[0].x < cell_number) or (not 0 <= self.snake.body[0].y < cell_number):
            self.game_over_flag = True

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over_flag = True

        for block in self.wall.wall_blocks:
            if block == self.snake.body[0]:
                self.game_over_flag = True

    # def game_over(self):
    #     self.snake.reset()

    def draw_grass(self):
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

    def draw_score(self):
        score_text = str(self.snake.score)
        # print(score_text)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 700)
        score_y = int(cell_size * cell_number - 750)
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = score.get_rect(
            midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6,
                              apple_rect.height)
        pygame.draw.rect(screen, (201, 223, 201), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(score, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)
    
    def game_over_screen(self):
        game_over_image = pygame.image.load('Graphics/game_over.png').convert_alpha()
        game_over_rect = game_over_image.get_rect(center=screen.get_rect().center)
        bg_rect = game_over_rect.copy()
        #game_over_image = pygame.transform.scale(game_over_image, (bg_rect.w, bg_rect.h))
        game_over_rect.y -= 150 # Move the game over image up 
        # Move the game over image to the right

        # Load restart and main menu buttons
        restart_button = pygame.image.load('Buttons/restart.png').convert_alpha()
        restart_highlighted_button = pygame.image.load('Buttons/restart_highlight.png').convert_alpha()
        restart_rect = restart_button.get_rect(center=screen.get_rect().center)
        restart_rect.y += 80  # Move the restart button down 
        restart_highlighted_rect = restart_highlighted_button.get_rect(center=restart_rect.center)
        restart_highlighted = False

        main_menu_button = pygame.image.load('Buttons/main_menu.png').convert_alpha()
        main_menu_highlighted_button = pygame.image.load('Buttons/main_menu_hightlight.png').convert_alpha()
        main_menu_rect = main_menu_button.get_rect(center=screen.get_rect().center)
        main_menu_rect.y += 200  # Move the main menu button down 
        main_menu_highlighted_button_rec = main_menu_highlighted_button.get_rect(center=main_menu_rect.center)
        main_menu_highlighted = False

        # Create background rectangle
        bg_rect = game_over_rect.union(restart_rect).union(main_menu_rect)
        bg_rect.inflate_ip(70, 80)  # Expand the background rectangle to fit the buttons
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
                    screen.blit(restart_highlighted_button,restart_highlighted_rect)
                else:
                    screen.blit(restart_button, restart_rect)

                if main_menu_highlighted:
                    screen.blit(main_menu_highlighted_button,main_menu_highlighted_button_rec)
                else:
                    screen.blit(main_menu_button, main_menu_rect)

            pygame.display.update()

    def game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == SCREEN_UPDATE:
                    self.update()
                    if self.game_over_flag:
                        self.game_over_screen()
                        if self.back_to_menu_flag:
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
            pygame.display.set_caption('Snaking')
            pygame.display.update()
            clock.tick(60)



