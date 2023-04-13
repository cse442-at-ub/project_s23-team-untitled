import csv
import sys
import random
import pygame

# Initial
pygame.init()

# Screen size and title
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WINDOW_TITLE = 'ScoreBoard'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(WINDOW_TITLE)

# images
image_return = pygame.transform.scale(pygame.image.load("Graphics/button_return.png"), (50, 50))
image_easy = pygame.image.load("Graphics/title_score_easy.png")
image_easy = pygame.transform.scale(image_easy, (int(image_easy.get_width()/2), int(image_easy.get_height())/2))
image_medium = pygame.image.load("Graphics/title_score_medium.png")
image_medium = pygame.transform.scale(image_medium, (int(image_medium.get_width()/2), int(image_medium.get_height())/2))
image_hard = pygame.image.load("Graphics/title_score_hard.png")
image_hard = pygame.transform.scale(image_hard, (int(image_hard.get_width()/2), int(image_hard.get_height())/2))
title = image_easy
image_score1 = pygame.image.load("Graphics/score_1.png")
image_score1 = pygame.transform.scale(image_score1, (100, 100))
image_score2 = pygame.image.load("Graphics/score_2.png")
image_score2 = pygame.transform.scale(image_score2, (100, 100))
image_score3 = pygame.image.load("Graphics/score_3.png")
image_score3 = pygame.transform.scale(image_score3, (100, 100))
image_score4 = pygame.image.load("Graphics/score_4.png")
image_score4 = pygame.transform.scale(image_score4, (100, 100))
image_score5 = pygame.image.load("Graphics/score_5.png")
image_score5 = pygame.transform.scale(image_score5, (100, 100))

rect_1 = pygame.Rect(265, 10, 300, 100)

# score_easy = sorted([random.randint(0, 100) for _ in range(5)], reverse=True)
score_easy = []
score_medium = sorted([random.randint(0, 100) for _ in range(5)], reverse=True)
score_hard = sorted([random.randint(0, 100) for _ in range(5)], reverse=True)
scores = score_easy

# read 5 easy level scores from file
with open('scores_easy.csv', 'r') as file:

    reader = csv.reader(file)
    next(reader)
    count = 0
    for row in file:
        if count < 5:
            row = row.split(',')
            score_easy.append(int(row[1]))
            count += 1
        else:
            break
    score_easy.sort(reverse=True)


class SETTINGS:

    def __init__(self):
        self.cell_size = 40
        self.cell_number = 20

        # Colors
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        # Font
        self.font_size = 80
        self.font = pygame.font.SysFont("Font/bahnschrift.ttf", self.font_size)

    def draw_grass(self):
        grass_color = (201, 223, 201)
        for row in range(self.cell_number):
            if row % 2 == 0:
                for col in range(self.cell_number):
                    if col % 2 == 0:
                        grass_rec = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size,
                                                self.cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rec)
            else:
                for col in range(self.cell_number):
                    if col % 2 != 0:
                        grass_rec = pygame.Rect(col * self.cell_size, row * self.cell_size, self.cell_size,
                                                self.cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rec)

    def draw_scoreboard(self):
        y = 170
        x = 300
        for i, score in enumerate(scores):
            text = f'{i + 1}     {score}'
            surface = settings.font.render(text, True, settings.black)
            screen.blit(surface, (x, y))
            y += settings.font_size + 10


settings = SETTINGS()

if __name__ == "__main__":

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse_pos = pygame.mouse.get_pos()
                # check if mouse is in the area
                if image_return.get_rect().collidepoint(mouse_pos):
                    print('Returned to the main menu!')
                    pygame.quit()
                    sys.exit()
                elif rect_1.collidepoint(mouse_pos):
                    print('Level changed!')
                    if title == image_easy:
                        title = image_medium
                        scores = score_medium
                    elif title == image_medium:
                        title = image_hard
                        scores = score_hard
                    else:
                        title = image_easy
                        scores = score_easy

        # Draw background
        screen.fill((179, 207, 178))
        settings.draw_grass()

        # Draw scoreboard
        settings.draw_scoreboard()

        # Draw return button
        screen.blit(image_return, (10, 10))

        # Draw title
        # pygame.draw.rect(screen, settings.white, rect_1)
        screen.blit(title, (250, 10))

        # Draw ranking
        screen.blit(image_score1, (269, 145))
        screen.blit(image_score2, (269, 145+90))
        screen.blit(image_score3, (269, 145+90*2))
        # screen.blit(image_score4, (250, 445))
        # screen.blit(image_score5, (250, 545))

        # Update display
        pygame.display.update()
