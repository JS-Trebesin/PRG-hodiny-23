import pygame
from pytmx.util_pygame import load_pygame


class Level:
    def __init__(self, level_data):
        self.data = load_pygame(level_data)
        self.ground = self.data.get_layer_by_name("ground")

    def draw_background(self):
        for tile in self.ground.tiles():
            print(tile)

path = "../assets/tiled/ucebna2.tmx"
level = Level(path)