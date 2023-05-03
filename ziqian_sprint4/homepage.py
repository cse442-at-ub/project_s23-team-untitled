import pygame
from level_select import *
from game_elements import *
from scoreboard import *
from inventory import *


def homepage():
    if not (os.path.exists('scores_easy.bin') and os.path.exists('scores_medium.bin') and os.path.exists('scores_hard.bin')):
    # create binary score file
        with open('scores_easy.bin', 'wb') as file:
            pickle.dump([], file)

        with open('scores_medium.bin', 'wb') as file:
            pickle.dump([], file)

        with open('scores_hard.bin', 'wb') as file:
            pickle.dump([], file)

    with open('sound.bin', 'wb') as f:
        pickle.dump(True, f)
        
    sound_on_button = pygame.image.load(
        'Buttons/sound_on.png').convert_alpha()
    sound_off_button = pygame.image.load(
        'Buttons/sound_off.png').convert_alpha()
    sound_on_button = pygame.transform.scale(sound_on_button, (296, 82))
    sound_off_button = pygame.transform.scale(sound_off_button, (296, 82))
    sound_on_rect = sound_on_button.get_rect(
            center=(screen.get_rect().centerx, 670))
    sound_off_rect = sound_on_button.get_rect(
            center=(screen.get_rect().centerx, 670))
    default_sound_button = sound_on_button
    default_sound_rect = sound_on_rect
    while True:
        screen.fill((179, 207, 178))
        selection_background(screen)
        pygame.display.set_icon(icon)
        pygame.display.set_caption('Homepage')

        daily_challenge_visible = False
        game_visible = False
        scores_visible = False
        inventory_visible = False

        daily_challenge_button = pygame.image.load(
            'Buttons/button_daily.png').convert_alpha()
        game_button = pygame.image.load(
            'Buttons/button_newgame.png').convert_alpha()
        scores_button = pygame.image.load(
            'Buttons/button_score.png').convert_alpha()
        inventory_button = pygame.image.load(
            'Buttons/button_inventory.png').convert_alpha()

        daily_challenge_highlight = pygame.image.load(
            'Buttons/button_daily_highlight.png').convert_alpha()
        game_highlight = pygame.image.load(
            'Buttons/button_newgame_highlight.png').convert_alpha()
        scores_highlight = pygame.image.load(
            'Buttons/button_score_highlight.png').convert_alpha()
        inventory_highlight = pygame.image.load(
            'Buttons/button_inventory_highlight.png').convert_alpha()

        daily_rect = daily_challenge_button.get_rect(
            center=(screen.get_rect().centerx, 150))
        game_rect = game_button.get_rect(center=(daily_rect.centerx, 280))
        scores_rect = scores_button.get_rect(center=(game_rect.centerx, 410))
        inventory_rect = inventory_button.get_rect(
            center=(scores_rect.centerx, 540))

        daily_rect_highlight = daily_challenge_highlight.get_rect(
            center=daily_rect.center)
        game_rect_highlight = game_highlight.get_rect(center=game_rect.center)
        scores_rect_highlight = scores_highlight.get_rect(
            center=scores_rect.center)
        inventory_rect_highlight = inventory_highlight.get_rect(
            center=inventory_rect.center)

        mouse_pos = pygame.mouse.get_pos()
        if daily_rect.collidepoint(mouse_pos):
            daily_challenge_visible = True
        else:
            daily_challenge_visible = False
        if game_rect.collidepoint(mouse_pos):
            game_visible = True
        else:
            game_visible = False
        if scores_rect.collidepoint(mouse_pos):
            scores_visible = True
        else:
            scores_visible = False
        if inventory_rect.collidepoint(mouse_pos):
            inventory_visible = True
        else:
            inventory_visible = False

        if daily_challenge_visible:
            screen.blit(daily_challenge_highlight, daily_rect_highlight)
        else:
            screen.blit(daily_challenge_button, daily_rect)

        if game_visible:
            screen.blit(game_highlight, game_rect_highlight)
        else:
            screen.blit(game_button, game_rect)

        if scores_visible:
            screen.blit(scores_highlight, scores_rect_highlight)
        else:
            screen.blit(scores_button, scores_rect)
        if inventory_visible:
            screen.blit(inventory_highlight, inventory_rect_highlight)
        else:
            screen.blit(inventory_button, inventory_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN and game_rect.collidepoint(pos):
                selection()

            if event.type == pygame.MOUSEBUTTONDOWN and daily_rect.collidepoint(pos):
                pass

            if event.type == pygame.MOUSEBUTTONDOWN and scores_rect.collidepoint(pos):
                scoreboard()

            if event.type == pygame.MOUSEBUTTONDOWN and inventory_rect.collidepoint(pos):
                inventory()
            if event.type == pygame.MOUSEBUTTONDOWN and default_sound_rect.collidepoint(pos):
                if default_sound_button == sound_on_button:
                    with open('sound.bin', 'wb') as f:
                        pickle.dump(False, f)
                    default_sound_button = sound_off_button
                    default_sound_rect = sound_off_rect
                elif default_sound_button == sound_off_button:
                    with open('sound.bin', 'wb') as f:
                        pickle.dump(True, f)
                    default_sound_button = sound_on_button
                    default_sound_rect = sound_on_rect

        screen.blit(default_sound_button, default_sound_rect)
        pygame.display.update()
        clock.tick(60)
