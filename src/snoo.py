import pygame
from pygame.locals import *
from typing import Any
import os
import sys
from pynput import keyboard


class GetPath:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def get_path(self) -> str:
        # return os.path.abspath(self.file_name)
        return f'{os.path.basename(self.file_name)}'


class Mine:
    def window_init(
        window_title: str,
        resolution: tuple[int, int]
    ) -> pygame.Surface:
        pygame.init()
        pygame.display.set_caption(window_title)
        return pygame.display.set_mode(resolution)

    def app_quit():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def font_setting(font_size: int, is_bold: bool = False) -> pygame.font.SysFont:
        return pygame.font.SysFont(None, font_size, is_bold)

    def getstatus(self):
        if self.listener == None:
            return False
        return True


class GetKey:

    def on_press(self, key) -> keyboard.Key | keyboard.KeyCode:
        return key

    def on_release(self, key) -> keyboard.Key | keyboard.KeyCode:
        return key

    def start(self):
        self.listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        )
        self.listener.start()

    def get_status(self):
        if (self.listener is None):
            return False
        return True


class Scene:
    class Settings:
        TITLE: str = 'Snoo.py'
        SIZE: tuple[int, int] = (664, 374)
        BG_COLOR: tuple[int, int, int] = (24, 27, 61)

    def center() -> tuple[int, int]:
        return Scene.Settings.SIZE / 2


def main() -> None:
    screen: pygame.Surface = Mine.window_init(
        window_title=Scene.Settings.TITLE,
        resolution=Scene.Settings.SIZE
    )

    font = Mine.font_setting(50)
    key_input = GetKey()
    key_input.start()

    while True:
        screen.fill(color=Scene.Settings.BG_COLOR)

        pressed_keys: pygame.ScancodeWrapper = pygame.key.get_pressed()
        pressed_key_names: list[str] = [
            pygame.key.name(key)
            for key, state in enumerate(pressed_keys) if state]
        pressed_key_str = ' + '.join(pressed_key_names)

        text: pygame.Surface = font.render(
            pressed_key_str, True, (255, 255, 255))
        screen.blit(text, (10, 10))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                key_name: str = pygame.key.name(event.key)
                # print(key_name)
                text = font.render(key_name, True, (128, 128, 128))
                screen.blit(source=text, dest=[332, 187])

        if not key_input.get_status():
            break

        Mine.app_quit()

        pygame.display.update()


if __name__ == '__main__':
    main()
