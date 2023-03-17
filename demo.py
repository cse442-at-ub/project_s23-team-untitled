import pygame,sys,random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        self.food_gain = 0

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

class FRUIT:
    def __init__(self,snake):
        self.snake = snake
        self.randomize()

    def draw_fruit(self):
        fruit_rec = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(apple,fruit_rec)
    
    def randomize(self):
        while True:
            x = random.randint(0, cell_number - 1)
            y = random.randint(0, cell_number - 1)
            self.pos = Vector2(x, y)
            if self.pos not in self.snake.body:
                break

class WALL:
    def __init__(self,snake,fruit):
        self.snake = snake
        self.fruit = fruit
        self.wall_blocks = []
        self.randomize()
        self.gg_flag = False

    def randomize(self):
        self.wall_blocks = []
        wall_numbers = 2
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

class SlowdownPowerUp:
    def __init__(self, snake,wall):
        self.snake = snake
        self.wall = wall
        self.active = False
        self.duration = 5000  # 5 seconds
        self.start_time = 0
        self.pos = None
        self.initialized = 0

    def draw(self):
        if not self.active and self.pos is not None:

            slow_rec = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size),cell_size,cell_size)
            screen.blit(turtle,slow_rec)

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
        if self.pos is None and  self.snake.food_gain >= 10 and self.snake.food_gain % 10 == 0 and not self.active:
            self.randomize() 
            self.initialized = self.snake.food_gain
        if  self.snake.food_gain == self.initialized  and self.pos is None and not self.active:
            self.pos = None
    
    def reset(self):
        self.active = False
        self.start_time =0
        self.pos = None

class FruitPlate:
    def __init__(self, snake, wall):
        self.snake = snake
        self.wall = wall
        self.pos = None
        self.flag = False
        self.initialized = 0

    def draw(self):
        if self.pos is not None:
            fruit_plate_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
            screen.blit(fruit_plate, fruit_plate_rect)

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


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT(self.snake)
        self.wall = WALL(self.snake,self.fruit)
        self.slowpower = SlowdownPowerUp(self.snake,self.wall)
        self.fruit_plate = FruitPlate(self.snake, self.wall)  # New instance of FruitPlate class
        self.n = 200
        self.SCREEN_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(self.SCREEN_UPDATE, self.n)
        self.game_over_flag = False

    def update(self):
        self.game_over_screen(main_game)
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.slowpower.update()
        self.fruit_plate.update()

    def draw_elements(self):
        self.draw_grass()
        if not self.game_over_flag:
            self.fruit.draw_fruit()
            self.snake.draw_snake()
            self.wall.draw_wall()
            self.draw_score()
            self.slowpower.draw()
            self.fruit_plate.draw()
        else:
            self.game_over_screen(main_game)

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
                self.fruit.randomize()
                self.snake.add_block()
                self.snake.food_gain += 1
                if self.fruit.pos in self.wall.wall_blocks:
                    self.fruit.randomize()

        elif self.slowpower.pos == self.snake.body[0] and not self.slowpower.active :
            self.slowpower.active = True
            self.slowpower.pos = None
            self.slowpower.start_time = pygame.time.get_ticks()
            self.n = 350
            pygame.time.set_timer(self.SCREEN_UPDATE, self.n)

        # New condition to handle fruit_plate collision
        elif self.fruit_plate.pos == self.snake.body[0]:
            self.snake.food_gain += 3
            self.fruit_plate.reset()
            

        if self.slowpower.active and pygame.time.get_ticks() - self.slowpower.start_time >= self.slowpower.duration:
                self.n = 200
                pygame.time.set_timer(self.SCREEN_UPDATE, self.n)
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

                

    def game_over_screen(self, main_game):
        if self.game_over_flag:
            # Load game over image and resize it to fit background rectangle size
            game_over_image = pygame.image.load('Graphics/game_over.png').convert_alpha()
            bg_rect = game_over_image.get_rect(center=screen.get_rect().center)
            game_over_image = pygame.transform.scale(game_over_image, (bg_rect.w, bg_rect.h))

            # Create background rectangle
            bg_rect.w += 50
            bg_rect.h += 20
            bg_rect.center = screen.get_rect().center
            # Center game over image in background rectangle
            game_over_rect = game_over_image.get_rect(center=bg_rect.center)
            # Draw background rectangle and game over image
            pygame.draw.rect(screen, (160, 198, 160), bg_rect, border_radius=30)
            pygame.draw.rect(screen, (0, 0, 0), bg_rect, border_radius=30, width=3)
            screen.blit(game_over_image, game_over_rect)
            
            pygame.display.update()
            

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        main_game.__init__()
                        return
                pygame.display.update()


    def draw_grass(self):
        grass_color = (201,223,201)
        for row in range (cell_number):
            if row % 2 ==0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rec = pygame.Rect(col * cell_size, row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rec)
            else:
                for col in range(cell_number):
                    if col %2 != 0:
                        grass_rec = pygame.Rect(col * cell_size, row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rec)
    def draw_score(self):
#        self.current_score = len(self.snake.body) - 3
        score_text = str(self.snake.food_gain)
        score_surface = game_font.render(score_text, True, (56,74,12))
        score_rect = score_surface.get_rect(bottomright=(cell_number * cell_size - 10, cell_number * cell_size - 10))
        padding = 5
        bg_rect = pygame.Rect(score_rect.left - padding, score_rect.top - padding,
                            score_rect.width + padding * 2, score_rect.height + padding * 2)
        bg_surface = pygame.Surface((bg_rect.width, bg_rect.height), pygame.SRCALPHA)
        bg_surface.fill((0, 0, 0, 0))
        pygame.draw.rect(bg_surface, (201, 223, 201, 10), bg_surface.get_rect(), border_radius=10)
        screen.blit(bg_surface, bg_rect)
        screen.blit(score_surface, score_rect)


pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number*cell_size))
icon = pygame.image.load('Graphics/snake.png')
clock = pygame.time.Clock()
apple = pygame.image.load('Graphics/apple_39.png').convert_alpha()
game_font = pygame.font.Font('Font/bahnschrift.ttf',25)
wall_segment = pygame.image.load('Graphics/wall_segment.png').convert_alpha()
turtle = pygame.image.load('Graphics/turtle.png').convert_alpha()
fruit_plate = pygame.image.load('Graphics/fruit_plate.png').convert_alpha()

main_game = MAIN()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == main_game.SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1,0)
        
    screen.fill((179,207,178))
    main_game.draw_elements()
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Snaking')
    pygame.display.update()
    clock.tick(60) #auto reset after 60s
 