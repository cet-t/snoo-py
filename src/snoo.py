import pygame
from pygame.locals import *
from typing import Any
import os
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
        return pygame.font.SysFont(None, font_size)

    def getstatus(self):
        if self.listener == None:
            return False
        return True


window_settings: dict[str, Any] = {
    'title': 'Snoopy',
    'size': (664, 374),  # 16:9
    'bg_color': (24, 27, 61)  # darkest navy
}


def main() -> None:
    screen = Mine.window_init(
        window_settings['title'], window_settings['size'])

    font = Mine.font_setting(50)

    while True:
        screen.fill(color=window_settings['bg_color'])
        Mine.app_quit()

        pressed_keys = pygame.key.get_pressed()
        pressed_key_names = [
            pygame.key.name(key)
            for key, state in enumerate(pressed_keys) if state]
        pressed_key_str = ' + '.join(pressed_key_names)

        text = font.render(pressed_key_str, True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.update()


if __name__ == '__main__':
    main()
