import pygame
# potřeba nainstalovat pomocí pip install pytmx
# umožní pracovat s .tmx soubory, které vytváří program Tiles, který používáme k vytvoření herního světa
from pytmx.util_pygame import load_pygame

# vytvoř classu Level - jedná se o čistou pythonovskou classu, které nedědí vlastnosti žádné předchozí classy
# pytmx vyžaduje informace o screenu, proto jej musíme přidat do __init__ naší classy
class Level:
    def __init__(self, level_data, screen):
        # využij funkci load_pygame, kterou jsme importovali z pytmx výše a načti data k levelu
        self.data = load_pygame(level_data)
        # ulož vrstvu s názvem ground pod proměnnou self.ground
        self.ground = self.data.get_layer_by_name("ground")

    def draw_background(self):
        for tile in self.ground.tiles():
            print(tile)
