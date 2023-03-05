import pygame
from pygame.locals import *
import typing
from typing import Any
import os
import sys
from pynput import keyboard
import pynput
from enum import Enum


class SceneState(Enum):
    Title = 0,
    Credit = 1,
    Play = 2,


class GetPath:
    def __init__(self, file_name: str) -> typing.Any:
        self.file_name = file_name
        GetPath.get_path()

    def get_path(self) -> str:
        return str(os.path.abspath(self.file_name))


class App:
    def window(window_title: str, resolution: tuple[int, int]) -> pygame.Surface:
        pygame.init()
        pygame.display.set_caption(window_title)
        return pygame.display.set_mode(resolution)

    def quit():
        for event in pygame.event.get():
            if event.type == K_ESCAPE and event.type == QUIT:
                pygame.quit()
                sys.exit()

    def font(font_size: int, is_bold: bool = False) -> pygame.font.SysFont:
        return pygame.font.SysFont(None, font_size, is_bold)


class GetKey:
    def on_press(self, key) -> keyboard.Key | keyboard.KeyCode:
        return key

    def on_release(self, key) -> keyboard.Key | keyboard.KeyCode:
        return key

    def start(self) -> None:
        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def get_status(self):
        if (self.listener is None):
            return False
        return True


class Scene:
    class Settings:
        TITLE = 'Snoo.py'
        SIZE = (664, 374)
        BG_COLOR = (24, 27, 61)

    def center():
        return Scene.Settings.SIZE / 2


def main() -> None:
    screen: pygame.Surface = App.window(
        window_title=Scene.Settings.TITLE,
        resolution=Scene.Settings.SIZE
    )
    font = App.font(50)
    key_input = GetKey()
    key_input.start()

    while True:
        screen.fill(color=Scene.Settings.BG_COLOR)

        pressed_keys: pygame.ScancodeWrapper = pygame.key.get_pressed()
        pressed_key_names: list[str] = [
            pygame.key.name(key)
            for key, state in enumerate(pressed_keys) if state
        ]
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

        App.quit()
        pygame.display.update()


if __name__ == '__main__':
    main()
