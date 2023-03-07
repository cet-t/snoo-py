﻿import pygame
from pygame.locals import *
import typing
from typing import Any
import os
import sys
from pynput.keyboard import Listener, Key, KeyCode
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
    class Setting:
        def window(_title: str, _res: tuple[int, int]) -> pygame.Surface:
            pygame.init()
            pygame.display.set_caption(_title)
            return pygame.display.set_mode(_res)

        def font(font_size: int, is_bold: bool = False) -> pygame.font.SysFont:
            return pygame.font.SysFont(None, font_size, is_bold)

    def quit() -> None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


class GetKey:
    def on_pressed(self, key) -> Key | KeyCode:
        return key

    def on_released(self, key) -> Key | KeyCode:
        return key

    def listen_start(self) -> None:
        self.listener = Listener(
            on_press=self.on_pressed, on_release=self.on_released)
        self.listener.start()

    def get_status(self):
        if (self.listener is None):
            return False
        return True


class Scene:
    class Settings:
        TITLE = "Snoo.py"
        SIZE = 664, 374
        X, Y = SIZE
        BG_COLOR: tuple[int, int, int] = 24, 27, 61

    def center():
        return Scene.Settings.SIZE / 2


def main() -> None:
    screen: pygame.Surface = App.window(
        _title=Scene.Settings.TITLE, _res=Scene.Settings.SIZE)
    font = App.font(50)
    key_input = GetKey()
    key_input.listen_start()

    while True:
        screen.fill(color=Scene.Settings.BG_COLOR)

        pressed_keys: pygame.ScancodeWrapper = pygame.key.get_pressed()
        pressed_key_names: list[str] = [
            pygame.key.name(key) for key, state in enumerate(pressed_keys) if state]
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
