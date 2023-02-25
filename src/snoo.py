import pygame
from pygame.locals import *
import sys
import typing
# import my as mine

type_rgb = tuple[int, int, int]

# sys.path.append('./my.py')

screen_settings: dict[str, typing.Any] = {
    'title': 'Snoopy',
    'size': (1280, 720),
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


def main(_background_rgb: type_rgb):
    screen = mine.screen_init(
        screen_settings['title'], screen_settings['size'])

    while True:
        screen.fill(_background_rgb)
        mine.app_quit()


if __name__ == '__main__':
    main(screen_settings['bg_color'])
