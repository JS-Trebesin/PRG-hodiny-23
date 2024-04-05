import pygame
# potřeba nainstalovat pomocí pip install pytmx
# umožní pracovat s .tmx soubory, které vytváří program Tiles, který používáme k vytvoření herního světa
from pytmx.util_pygame import load_pygame
from items import Desk

# vytvoř classu Level - jedná se o čistou pythonovskou classu, které nedědí vlastnosti žádné předchozí classy
# pytmx vyžaduje informace o screenu, proto jej musíme přidat do __init__ naší classy
class Level:
    def __init__(self, level_data, screen, desk_group):
        # využij funkci load_pygame, kterou jsme importovali z pytmx výše a načti data k levelu
        self.data = load_pygame(level_data)
        self.desk_group = desk_group
        self.screen = screen

        # pro každou vrstvu z vrstev, které se nacházejí v našem souboru s herním světem, vytvoř attribut (self.něco)
        for layer in self.data.visible_layers:
            setattr(self, layer.name, self.data.get_layer_by_name(layer.name))

        # vytvoř Surface pro pozadí - velikost pozadí je odvozena od velikosti herního světa a rozměrů jednotlivých tiles (dlaždic)
        self.background = pygame.Surface((self.data.width * self.data.tilewidth, self.data.height * self.data.tileheight))

        # spusť funkci create_desk() při vytvoření classy        
        self.create_desk()

        

    def draw_background(self):
        # ve vrstvě self.ground má každý tiles 3 vlastnosti - pozici x a y a grafiku (obrázek)
        # pro každý tiles blitneme grafiku na self.background vytvořené výše a na souřadnice x a y které jsme získali z .tmx souboru
        for x, y, image in self.ground.tiles():
            self.background.blit(image, (x * self.data.tilewidth, y * self.data.tileheight))
        
        # vytvořené pozadí blitneme na obrazovku na souřadnice 0,0 - úplně nahoru
        self.screen.blit(self.background, (0,0))
    
    def create_desk(self):
        # pro každou lavici ve vrstvě furniture v .tmx souboru vytvoř instanci classy Desk a následně ji přidej do skupiny desk_group
        for desk in self.furniture:
            new_desk = Desk(desk.image, desk.width, desk.height, (desk.x, desk.y))
            self.desk_group.add(new_desk)
            

