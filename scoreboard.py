from game_elements import *
from level_1 import *
from level_2 import *
from level_3 import *



def scoreboard():
    image_return = pygame.image.load('Buttons/button_return.png').convert_alpha()
    image_easy = pygame.image.load("Graphics/title_score_easy.png")
    image_easy = pygame.transform.scale(image_easy, (int(image_easy.get_width()/2), int(image_easy.get_height())/2))
    image_medium = pygame.image.load("Graphics/title_score_medium.png")
    image_medium = pygame.transform.scale(image_medium, (int(image_medium.get_width()/2), int(image_medium.get_height())/2))
    image_hard = pygame.image.load("Graphics/title_score_hard.png")
    image_hard = pygame.transform.scale(image_hard, (int(image_hard.get_width()/2), int(image_hard.get_height())/2))
    title_sb = image_easy
    image_score1 = pygame.image.load("Graphics/score_1.png")
    image_score1 = pygame.transform.scale(image_score1, (100, 100))
    image_score2 = pygame.image.load("Graphics/score_2.png")
    image_score2 = pygame.transform.scale(image_score2, (100, 100))
    image_score3 = pygame.image.load("Graphics/score_3.png")
    image_score3 = pygame.transform.scale(image_score3, (100, 100))
    rect_1 = pygame.Rect(265, 10, 300, 100)

    score_easy = []
    score_medium = []
    score_hard = []
    # read scores from file
    if not os.path.exists('scores_easy.bin'):
        with open('scores_easy.bin', 'wb') as file:
            pickle.dump([], file)
    with open('scores_easy.bin', 'rb') as file:
        score_easy = [int(element[1]) for element in pickle.load(file)]
        score_easy.sort(reverse=True)
        score_easy = score_easy[:5]
        print(score_easy)

    if not os.path.exists('scores_medium.bin'):
        with open('scores_medium.bin', 'wb') as file:
            pickle.dump([], file)
    with open('scores_medium.bin', 'rb') as file:
        score_medium = [int(element[1]) for element in pickle.load(file)]
        score_medium.sort(reverse=True)
        score_medium = score_medium[:5]
        print(score_medium)

    if not os.path.exists('scores_hard.bin'):
        with open('scores_hard.bin', 'wb') as file:
            pickle.dump([], file)
    with open('scores_hard.bin', 'rb') as file:
        score_hard = [int(element[1]) for element in pickle.load(file)]
        score_hard.sort(reverse=True)
        score_hard = score_hard[:5]
        print(score_hard)

    scores = score_easy


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
    while True:
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Scoreboard')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse position
                mouse_pos = pygame.mouse.get_pos()
                # check if mouse is in the area
                if image_return.get_rect().collidepoint(mouse_pos):
                    return
                elif rect_1.collidepoint(mouse_pos):
                    if title_sb == image_easy:
                        title_sb = image_medium
                        scores = score_medium
                    elif title_sb == image_medium:
                        title_sb = image_hard
                        scores = score_hard
                    else:
                        title_sb = image_easy
                        scores = score_easy

        # Draw background
        screen.fill((179, 207, 178))
        settings.draw_grass()

        # Draw scoreboard
        settings.draw_scoreboard()

        # Draw return button
        screen.blit(image_return, (20, 20))

        # Draw title
        # pygame.draw.rect(screen, settings.white, rect_1)
        screen.blit(title_sb, (250, 10))

        # Draw ranking
        screen.blit(image_score1, (269, 145))
        screen.blit(image_score2, (269, 145+90))
        screen.blit(image_score3, (269, 145+90*2))

        # Update display
        pygame.display.update()
        clock.tick(60)

    