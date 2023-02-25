import pygame
from pygame.locals import *
import typing
import os
from cree import *
import sys


class GetPath:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def get_path(self) -> str:
        return os.path.abspath(self.file_name)
        # return './{}'.format(os.path.basename(self.file_name))


class Mine:
    def window_init(
        window_title: str,
        resolution: tuple[int, int]
    ) -> pygame.Surface:
        pygame.init()
        pygame.display.set_caption(window_title)
        return pygame.display.set_mode(resolution)

    def app_quit():
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()

    def font_setting(font_size: int):
        return pygame.font.Font(None, font_size)


def main(_bg_color: tuple[int, int, int]):
    screen = Mine.window_init(
        window_settings['title'], window_settings['size'])

    font = Mine.font_setting(30)

    while True:
        screen.fill(_bg_color)
        pygame.display.update()
        Mine.app_quit()

        for e in pygame.event.get():
            if e.type == KEYDOWN:
                key_name = pygame.key.name(e.key)
                print(key_name)
                text = font.render(
                    key_name, True, (128, 128, 128))
                screen.blit(source=text, dest=[332, 187])


if __name__ == '__main__':
    from pathlib import Path
    # file = GetPath('snoo.py')
    # print(file.get_path())

    main(window_settings['bg_color'])
