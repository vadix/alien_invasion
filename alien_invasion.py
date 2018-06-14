import sys

import pygame

#from settings import Settings
#from ship import Ship
#import game_functions as gf


def run_game():
    # Инциализирует игру и создает объект экрана.
    pygame.init()
#    ai_settings = Settings()
#    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля.
#    ship = Ship(screen)

    # Запуск основного цикла игры.
    while True:
    # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
    # while True:
    #     gf.check_events()
    #     gf.update_screen(ai_settings, screen, ship)
run_game()