import pygame
from level_select import *
from game_elements import *
from scoreboard import *

def homepage():
    while True:
        screen.fill((179, 207, 178))
        selection_background(screen)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Homepage')
        game_button = pygame.transform.scale(pygame.image.load('Graphics/title_newgame.png'), (300, 100))
        daily_challenge_button = pygame.transform.scale(pygame.image.load('Graphics/button_daily_highlight.png'), (300, 100))
        scores_button = pygame.transform.scale(pygame.image.load('Graphics/button_score.png'), (300, 100))
        inventory_button = pygame.transform.scale(pygame.image.load('Graphics/button_inventory.png'), (300, 100))
        button_rect = game_button.get_rect()
        button_rect.centerx = screen.get_rect().centerx
        button_rect.centery = screen.get_rect().centery-100
        daily_challenge_button_rect = daily_challenge_button.get_rect()
        daily_challenge_button_rect.centerx = screen.get_rect().centerx
        daily_challenge_button_rect.centery = screen.get_rect().centery - 225
        scores_button_rect = scores_button.get_rect()
        scores_button_rect.centerx = screen.get_rect().centerx
        scores_button_rect.centery = screen.get_rect().centery +50
        inventory_button_rect = inventory_button.get_rect()
        inventory_button_rect.centerx = screen.get_rect().centerx
        inventory_button_rect.centery = screen.get_rect().centery + 200
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 3)
        screen.blit(game_button, button_rect)
        screen.blit(daily_challenge_button, daily_challenge_button_rect)
        screen.blit(scores_button, scores_button_rect)
        screen.blit(inventory_button, inventory_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(pos):
                selection()

            if event.type == pygame.MOUSEBUTTONDOWN and daily_challenge_button_rect.collidepoint(pos):
                pass

            if event.type == pygame.MOUSEBUTTONDOWN and scores_button_rect.collidepoint(pos):
                scoreboard()

            if event.type == pygame.MOUSEBUTTONDOWN and inventory_button_rect.collidepoint(pos):
                pass
        
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    homepage()
