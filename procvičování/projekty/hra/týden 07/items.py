# v tomto souboru budeme vytvářet classy k předmětům ve hře
import pygame


class Desk(pygame.sprite.Sprite):
    def __init__(self, image, width, height, position):
        super().__init__()
        self.image = image
        self.width = width
        self.height = height
        self.position = position

        self.rect = self.image.get_rect(topleft=self.position)