import pygame
import sys
import random
from pygame.math import Vector2
from game_elements import *

class SNAKE3:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        self.food_gain = 0

        self.head_up = head_up
        self.head_down = head_down
        self.head_right = head_right
        self.head_left =  head_left

        self.tail_up = tail_up
        self.tail_down =  tail_down
        self.tail_right = tail_right
        self.tail_left = tail_left

        self.body_vertical = body_vertical
        self.body_horizontal = body_horizontal

        self.body_tr = body_tr
        self.body_tl = body_tl
        self.body_bl = body_bl
        self.body_br = body_br

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index,block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos,y_pos,cell_size,cell_size)

            if index ==0:
                screen.blit(self.head,block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail,block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body [index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical,block_rect)
                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal,block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): self.head = self.head_left
        elif head_relation == Vector2(-1,0): self.head = self.head_right
        elif head_relation == Vector2(0,1): self.head = self.head_up
        elif head_relation == Vector2(0,-1): self.head = self.head_down
    
    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): self.tail = self.tail_down 

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self,):
        self.new_block = True

    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)       

class FRUIT3:
    def __init__(self,snake):
        self.snake = snake
        self.randomize()

    def draw_fruit(self):
        fruit_rec = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(food_src,fruit_rec)
    
    def randomize(self):
        while True:
            x = random.randint(0, cell_number - 1)
            y = random.randint(0, cell_number - 1)
            self.pos = Vector2(x, y)
            if self.pos not in self.snake.body:
                break

class WALL3:
    def __init__(self,snake,fruit):
        self.snake = snake
        self.fruit = fruit
        self.wall_blocks = []
        self.randomize()
        self.gg_flag = False

    def randomize(self):
        self.wall_blocks = []
        wall_numbers = 4
        for i in range(wall_numbers):
            # Generate first wall
            start_x = random.randint(1, cell_number - 3)
            start_y = random.randint(1, cell_number - 3)
            direction = random.choice([Vector2(1, 0), Vector2(0, 1)])
            wall_shape = random.choice(["line", "L_shape"])
            num_walls = random.randint(3, 5)

            if wall_shape == "line":
                for i in range(num_walls):
                    obstacle_pos = Vector2(start_x, start_y) + i * direction
                    while obstacle_pos in self.wall_blocks or obstacle_pos in self.snake.body or obstacle_pos == self.fruit.pos:
                        start_x = random.randint(1, cell_number - 3)
                        start_y = random.randint(1, cell_number - 3)
                        direction = random.choice([Vector2(1, 0), Vector2(0, 1)])
                        obstacle_pos = Vector2(start_x, start_y) + i * direction
                    self.wall_blocks.append(obstacle_pos)
            else: # "L_shape"
                if direction == Vector2(1, 0):
                    for i in range(num_walls):
                        if i == 0:
                            obstacle_pos = Vector2(start_x, start_y)
                        elif i == 1:
                            obstacle_pos = Vector2(start_x, start_y + 1)
                        else:
                            obstacle_pos = Vector2(start_x + i - 1, start_y + 1)
                        while obstacle_pos in self.wall_blocks or obstacle_pos in self.snake.body or obstacle_pos == self.fruit.pos:
                            start_x = random.randint(1, cell_number - 3)
                            start_y = random.randint(1, cell_number - 3)
                            obstacle_pos = Vector2(start_x, start_y + 1)
                        self.wall_blocks.append(obstacle_pos)
                else: # direction == Vector2(0, 1)
                    for i in range(num_walls):
                        if i == 0:
                            obstacle_pos = Vector2(start_x, start_y)
                        elif i == 1:
                            obstacle_pos = Vector2(start_x + 1, start_y)
                        else:
                            obstacle_pos = Vector2(start_x + 1, start_y + i - 1)
                        while obstacle_pos in self.wall_blocks or obstacle_pos in self.snake.body or obstacle_pos == self.fruit.pos:
                            start_x = random.randint(1, cell_number - 3)
                            start_y = random.randint(1, cell_number - 3)
                            obstacle_pos = Vector2(start_x + 1, start_y)
                        self.wall_blocks.append(obstacle_pos)

    def draw_wall(self):
        for block in self.wall_blocks:
            wall_suqre = pygame.Rect(int(block.x * cell_size), int(block.y * cell_size), cell_size, cell_size)
            screen.blit(wall_segment,wall_suqre)

class SlowdownPowerUp3:
    def __init__(self, snake,wall):
        self.snake = snake
        self.wall = wall
        self.active = False
        self.duration = 5000  # 5 seconds
        self.start_time = 0 # use for limit slowdown time
        self.pos = None
        self.limit = 0 # use for limit exsisting time

    def draw(self):
        if not self.active and self.pos is not None:

            slow_rec = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size)
            screen.blit(turtle_src,slow_rec)

    def randomize(self):
            while True:
                        x = random.randint(0, cell_number - 1)
                        y = random.randint(0, cell_number - 1)
                        pos = Vector2(x, y)
#                       print('1' + str(self.pos))
                        if pos not in self.snake.body and pos not in self.wall.wall_blocks:
                            self.pos = pos
                            break
    
    def update(self):
        current_tick = pygame.time.get_ticks()
        if self.pos is None and self.snake.food_gain >= 10 and self.snake.food_gain % 10 == 0 and not self.active and not self.limit:
            self.randomize() 
            self.limit = current_tick
        if self.pos and current_tick - self.limit >= 6000:
            self.pos = None  

    def reset(self):
        self.start_time =0
        self.limit = 0
        self.pos = None

class FruitPlate3:
    def __init__(self, snake, wall):
        self.snake = snake
        self.wall = wall
        self.pos = None
        self.flag = False
        self.initialized = 0

    def draw(self):
        if self.pos is not None:
            fruit_plate_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
            screen.blit(plate_src, fruit_plate_rect)

    def randomize(self):
        while True:
            x = random.randint(0, cell_number - 1)
            y = random.randint(0, cell_number - 1)
            pos = Vector2(x, y)
            if pos not in self.snake.body and pos not in self.wall.wall_blocks:
                self.pos = pos
                break

    def update(self):
        if self.pos is None and not self.flag:
            if not self.initialized:
                if self.snake.food_gain >= 8 and self.snake.food_gain % 8 == 0 :
                    self.randomize()
                    self.flag = True
                    self.initialized = self.snake.food_gain
            elif self.initialized:
                if self.snake.food_gain >= 19 and (self.snake.food_gain - self.initialized) % 11 == 0 :
                    self.randomize()
                    self.flag = True
                    self.initialized = self.snake.food_gain

    def reset(self):
        self.flag = False
        self.pos = None

class ScreenUpdate3:
    def __init__(self,time):
        self.time = time
        self.screen_updates = pygame.USEREVENT
        pygame.time.set_timer(self.screen_updates,self.time)

    def set_update_time(self, time):
        self.time = time
        pygame.time.set_timer(self.screen_updates, self.time)
    
class MAIN3:
    def __init__(self):
        global head_up, head_down, head_right, head_left, tail_up, tail_down, tail_right, tail_left, body_vertical, body_horizontal, body_tr, body_tl, body_bl, body_br
        with open('skin_selections.txt','r') as f:
                lines = f.readlines()
                if len(lines) == 2 :
                    sn_skin_slection = int(lines[0])
        if sn_skin_slection == 1:
            head_up = pygame.image.load('Graphics/head_u.png').convert_alpha()
            head_down = pygame.image.load('Graphics/head_d.png').convert_alpha()
            head_right = pygame.image.load('Graphics/head_r.png').convert_alpha()
            head_left = pygame.image.load('Graphics/head_l.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d.png').convert_alpha()
            tail_down = pygame.image.load('Graphics/tail_u.png').convert_alpha()
            tail_right = pygame.image.load('Graphics/tail_l.png').convert_alpha()
            tail_left = pygame.image.load('Graphics/tail_r.png').convert_alpha()
            body_vertical = pygame.image.load('Graphics/body_v.png').convert_alpha()
            body_horizontal = pygame.image.load('Graphics/body_h.png').convert_alpha()
            body_tr = pygame.image.load('Graphics//body_br.png').convert_alpha()
            body_tl = pygame.image.load('Graphics//body_bl.png').convert_alpha()
            body_bl = pygame.image.load('Graphics//body_tr.png').convert_alpha()
            body_br = pygame.image.load('Graphics//body_tl.png').convert_alpha()
        elif sn_skin_slection == 2:
            head_up = pygame.image.load('Graphics/head_u2.png').convert_alpha()
            head_down = pygame.image.load('Graphics/head_d2.png').convert_alpha()
            head_right = pygame.image.load('Graphics/head_r2.png').convert_alpha()
            head_left = pygame.image.load('Graphics/head_l2.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d2.png').convert_alpha()
            tail_down = pygame.image.load('Graphics/tail_u2.png').convert_alpha()
            tail_right = pygame.image.load('Graphics/tail_l2.png').convert_alpha()
            tail_left = pygame.image.load('Graphics/tail_r2.png').convert_alpha()
            body_vertical = pygame.image.load('Graphics/body_v2.png').convert_alpha()
            body_horizontal = pygame.image.load('Graphics/body_h2.png').convert_alpha()
            body_tr = pygame.image.load('Graphics//body_br2.png').convert_alpha()
            body_tl = pygame.image.load('Graphics//body_bl2.png').convert_alpha()
            body_bl = pygame.image.load('Graphics//body_tr2.png').convert_alpha()
            body_br = pygame.image.load('Graphics//body_tl2.png').convert_alpha()
        elif sn_skin_slection == 3:
            head_up = pygame.image.load('Graphics/head_u3.png').convert_alpha()
            head_down = pygame.image.load('Graphics/head_d3.png').convert_alpha()
            head_right = pygame.image.load('Graphics/head_r3.png').convert_alpha()
            head_left = pygame.image.load('Graphics/head_l3.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d3.png').convert_alpha()
            tail_down = pygame.image.load('Graphics/tail_u3.png').convert_alpha()
            tail_right = pygame.image.load('Graphics/tail_l3.png').convert_alpha()
            tail_left = pygame.image.load('Graphics/tail_r3.png').convert_alpha()
            body_vertical = pygame.image.load('Graphics/body_v3.png').convert_alpha()
            body_horizontal = pygame.image.load('Graphics/body_h3.png').convert_alpha()
            body_tr = pygame.image.load('Graphics//body_br3.png').convert_alpha()
            body_tl = pygame.image.load('Graphics//body_bl3.png').convert_alpha()
            body_bl = pygame.image.load('Graphics//body_tr3.png').convert_alpha()
            body_br = pygame.image.load('Graphics//body_tl3.png').convert_alpha()
        elif sn_skin_slection == 4:
            head_up = pygame.image.load('Graphics/head_u4.png').convert_alpha()
            head_down = pygame.image.load('Graphics/head_d4.png').convert_alpha()
            head_right = pygame.image.load('Graphics/head_r4.png').convert_alpha()
            head_left = pygame.image.load('Graphics/head_l4.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d4.png').convert_alpha()
            tail_down = pygame.image.load('Graphics/tail_u4.png').convert_alpha()
            tail_right = pygame.image.load('Graphics/tail_l4.png').convert_alpha()
            tail_left = pygame.image.load('Graphics/tail_r4.png').convert_alpha()
            body_vertical = pygame.image.load('Graphics/body_v4.png').convert_alpha()
            body_horizontal = pygame.image.load('Graphics/body_h4.png').convert_alpha()
            body_tr = pygame.image.load('Graphics//body_br4.png').convert_alpha()
            body_tl = pygame.image.load('Graphics//body_bl4.png').convert_alpha()
            body_bl = pygame.image.load('Graphics//body_tr4.png').convert_alpha()
            body_br = pygame.image.load('Graphics//body_tl4.png').convert_alpha()
        else:
            head_up = pygame.image.load('Graphics/head_u5.png').convert_alpha()
            head_down = pygame.image.load('Graphics/head_d5.png').convert_alpha()
            head_right = pygame.image.load('Graphics/head_r5.png').convert_alpha()
            head_left = pygame.image.load('Graphics/head_l5.png').convert_alpha()
            tail_up = pygame.image.load('Graphics/tail_d5.png').convert_alpha()
            tail_down = pygame.image.load('Graphics/tail_u5.png').convert_alpha()
            tail_right = pygame.image.load('Graphics/tail_l5.png').convert_alpha()
            tail_left = pygame.image.load('Graphics/tail_r5.png').convert_alpha()
            body_vertical = pygame.image.load('Graphics/body_v5.png').convert_alpha()
            body_horizontal = pygame.image.load('Graphics/body_h5.png').convert_alpha()
            body_tr = pygame.image.load('Graphics//body_br5.png').convert_alpha()
            body_tl = pygame.image.load('Graphics//body_bl5.png').convert_alpha()
            body_bl = pygame.image.load('Graphics//body_tr5.png').convert_alpha()
            body_br = pygame.image.load('Graphics//body_tl5.png').convert_alpha()
        self.snake = SNAKE3()
        self.fruit = FRUIT3(self.snake)
        self.wall = WALL3(self.snake,self.fruit)
        self.slowpower = SlowdownPowerUp3(self.snake,self.wall)
        self.fruit_plate = FruitPlate3(self.snake, self.wall)
        self.screen_parameter= 230
        self.screen_update_in_main = ScreenUpdate3(self.screen_parameter)
        self.game_over_flag = False
        self.back_to_menu_flag = False

    def update(self):
        # self.game_over_screen()
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.slowpower.update()
        self.fruit_plate.update()    

    def draw_elements(self):
        self.draw_grass()
        # if not self.game_over_flag:
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.wall.draw_wall()
        self.draw_score()
        self.slowpower.draw()
        self.fruit_plate.draw()
        # else:
        #     self.game_over_screen()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()
                self.snake.food_gain += 1
                #stop fruit from generating on wall segments
                if self.fruit.pos in self.wall.wall_blocks:
                    self.fruit.randomize()

        elif self.slowpower.pos == self.snake.body[0] and not self.slowpower.active :
            self.slowpower.active = True
            self.slowpower.pos = None
            self.slowpower.start_time = pygame.time.get_ticks()
            self.screen_parameter = 320
            self.screen_update_in_main.set_update_time(self.screen_parameter)

        # New condition to handle fruit_plate collision
        elif self.fruit_plate.pos == self.snake.body[0]:
            self.snake.food_gain += 3
            self.fruit_plate.reset()

        if self.slowpower.active:
            if pygame.time.get_ticks() - self.slowpower.start_time >= self.slowpower.duration:
                self.screen_parameter = 230
                self.screen_update_in_main.set_update_time(self.screen_parameter)
                self.slowpower.reset()
        
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()
            elif block == self.slowpower.pos:
                self.slowpower.pos = None
            elif block == self.fruit_plate.pos:
                self.fruit_plate.pos = None

    def check_fail(self):
        if (not 0 <= self.snake.body[0].x < cell_number) or (not 0 <= self.snake.body[0].y < cell_number):
            self.game_over_flag = True   
            
        for block in self.snake.body[1:] :
            if block == self.snake.body[0]:
                    if self.snake.food_gain >= 1 : 
                        self.game_over_flag = True
                    self.snake.reset()

        for block in self.wall.wall_blocks:
            if block == self.snake.body[0]:
                self.game_over_flag = True 

    def game_over_screen(self):
        global highest_scores
        # if self.game_over_flag:
        highest_scores.append(self.snake.food_gain)
        highest_scores.sort(reverse=True)
        highest_scores = highest_scores[:5]
        # Load game over image and resize it to fit background rectangle size
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

    def draw_grass(self):
        grass_color = (201,223,201)
        grass = [[grass_color if (row+col)%2==0 else (179,207,179) for col in range(cell_number)] for row in range(cell_number)]

        # Change the color of the first row to (179,207,178)
 #       grass[0] = [(179,207,178) for _ in range(cell_number)]

        grass_surface = pygame.Surface((cell_number*cell_size, cell_number*cell_size))
        for row, cols in enumerate(grass):
            for col, color in enumerate(cols):
                grass_rec = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                pygame.draw.rect(grass_surface, color, grass_rec)
        screen.blit(grass_surface, (0, 0))

    def draw_score(self):
        score_text = str(self.snake.food_gain)
        score_surface = game_font.render(score_text, True, (56, 74, 12, 128))

        score_x = int(cell_size * cell_number - 700)
        # Set the score_y value to cell_size/2 to center it in the first row
        score_y = int(cell_size/2)

        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = score.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 6, apple_rect.height)
        bg_surface = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        bg_surface.fill((201, 223, 201, 128))
        pygame.draw.rect(bg_surface, (56, 74, 12), bg_surface.get_rect(), 2)
        screen.blit(bg_surface, bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(score, apple_rect)
    def game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == self.screen_update_in_main.screen_updates:
                    self.update()
                    if self.game_over_flag:
                        self.game_over_screen()
                        if self.back_to_menu_flag:
                            return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0,-1)
                    if event.key == pygame.K_RIGHT:
                        if self.snake.direction.x != -1:
                            self.snake.direction = Vector2(1,0)
                    if event.key == pygame.K_DOWN:
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0,1)
                    if event.key == pygame.K_LEFT:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1,0)
                
            screen.fill((179,207,178))
            with open('skin_selections.txt','r') as f:
                lines = f.readlines()
                if len(lines) == 2 :
                    sn_skin_slection = int(lines[0])
                    fr_skin_slection = int(lines[1])
            global food_src
            if fr_skin_slection == 1:
                food_src = pygame.image.load('Graphics/fr1.png').convert_alpha()
            elif fr_skin_slection == 2:
                food_src = pygame.image.load('Graphics/fr2.png').convert_alpha()
            elif fr_skin_slection == 3:
                food_src = pygame.image.load('Graphics/fr3.png').convert_alpha()
            elif fr_skin_slection == 4:
                food_src = pygame.image.load('Graphics/fr4.png').convert_alpha()
            elif fr_skin_slection == 5:
                food_src = pygame.image.load('Graphics/fr5.png').convert_alpha()
            elif fr_skin_slection == 6:
                food_src = pygame.image.load('Graphics/fr6.png').convert_alpha()
            elif fr_skin_slection == 7:
                food_src = pygame.image.load('Graphics/fr7.png').convert_alpha()
            elif fr_skin_slection == 8:
                food_src = pygame.image.load('Graphics/fr8.png').convert_alpha()
            elif fr_skin_slection == 9:
                food_src = pygame.image.load('Graphics/fr9.png').convert_alpha()
            self.draw_elements()
            pygame.display.set_icon(icon)
            pygame.display.set_caption('Snaking')
            pygame.display.update()
            clock.tick(60)

