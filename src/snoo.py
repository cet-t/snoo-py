import pygame
from pygame.locals import *
import sys
import typing
# from my import *

# sys.path.append('./my.py')

window_settings: dict[str, typing.Any] = {
    'title': 'Snoopy',
    'size': (664, 374),  # 16:9
    'bg_color': (32, 107, 0)
}


class mine:
    def screen_init(
        _window_title: str,
        _resolutions: tuple[int, int]
    ) -> pygame.Surface:
        pygame.init()
        pygame.display.set_caption(_window_title)
        return pygame.display.set_mode(_resolutions)

    def app_quit():
        for e in pygame.event.get():
            if e.type == QUIT or (
                e.type == KEYDOWN and e.type == K_ESCAPE
            ):
                pygame.quit()
                sys.exit()


def main(_bg_color: tuple[int, int, int]):
    screen = mine.window_init(
        window_settings['title'], window_settings['size'])

    while True:
        screen.fill(_bg_color)
        mine.app_quit()


if __name__ == '__main__':
    main(window_settings['bg_color'])
