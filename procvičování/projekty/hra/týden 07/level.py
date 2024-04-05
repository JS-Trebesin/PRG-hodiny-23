import pygame
from items import Desk
from pytmx.util_pygame import load_pygame


class Level:
    def __init__(self, level_data, screen, desk_group):
        self.data = load_pygame(level_data)
        self.desk_group = desk_group
        for layer in self.data.visible_layers:
            setattr(self, layer.name, self.data.get_layer_by_name(layer.name))

        self.background = pygame.Surface((self.data.width * self.data.tilewidth, self.data.height * self.data.tileheight))
        self.screen = screen 
        
        self.create_desk()

        

    def draw_background(self):
        for x, y, image in self.ground.tiles():
            self.background.blit(image, (x * self.data.tilewidth, y * self.data.tileheight))
        self.screen.blit(self.background, (0,0))
    
    def create_desk(self):
        for desk in self.furniture:
            new_desk = Desk(desk.image, desk.width, desk.height, (desk.x, desk.y))
            self.desk_group.add(new_desk)
            

