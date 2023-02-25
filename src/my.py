import sys
import pygame
from pygame.locals import *


class _mine:
    def window_init(
        _window_title: str,
        _resolutions: tuple[int, int]
    ) -> pygame.Surface:
        pygame.init()
        pygame.display.set_caption(_window_title)
        return pygame.display.set_mode(_resolutions)

    def app_quit():
        def q():
            pygame.quit()
            sys.exit()

        for e in pygame.event.get():
            if e.type == QUIT or (
                e.type == KEYDOWN and e.type == K_ESCAPE
            ):
                q()
