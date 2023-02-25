import sys
import pygame
from pygame.locals import *


class mine:
    def display_init(
        window_title: str,
        resolutions: tuple[int, int]
    ) -> pygame.Surface:
        pygame.init()
        pygame.display.set_caption(window_title)
        return pygame.display.set_mode(resolutions)

    def app_quit():
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
