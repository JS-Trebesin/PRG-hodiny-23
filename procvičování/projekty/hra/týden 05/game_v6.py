import pygame
from sys import exit
from settings import *
from utility import get_image
from player import Player
from monster import Monster


# inicializuje hru - spustíme pygame
pygame.init()

# vytvoř hodiny
clock = pygame.time.Clock()


# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))



# player_x a player_y v nové verzi kódu už řeší pouze spawn
# player_x = 100
# player_y = 200
# player_index = 0
# player_spritesheet = pygame.image.load("man_brownhair_run.png").convert_alpha()
# vytvoření surface pro postavičku hráče - načtení obrázku
# player_surf = get_image(player_spritesheet, 0, 0, 15, 16, 3)

# kvůli detekci kolize nejprve vytvoříme rectangle pro hráče
# player_rect = player_surf.get_rect(midbottom=(player_x, player_y))


# vytvoření surface pro postavičku monster - nepřítele - načtení obrázku
monster_walk_1 = pygame.image.load("monster_sprite.png").convert_alpha()
monster_walk_2 = pygame.image.load("monster_sprite_walk.png").convert_alpha()
monster_walk = [monster_walk_1, monster_walk_2]
monster_index = 0

monster_surf = monster_walk[monster_index]

# kvůli detekci kolize nejprve vytvoříme rectangle pro monstrum
monster_rect = monster_surf.get_rect(midbottom=(300, 600))

# počítání životů - začátek
lives = 3

# vytvoření fontu - None znamená defaultní font, 25 je velikost
font = pygame.font.Font(None, 25)



game_over = False

elapsed_time = 0

invul = False

player = Player()
monster = Monster()

# herní smyčka
while True:
    # kontroluje nám události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud dojde k události vypnout, vypne
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    

    if game_over == False:
        # proměnná key, pod ní schováme stisknutou klávesu
        

        # pokud je stisknutá šipka doleva, atd.
        # změna ovládání - nyní pohybujeme vytvořením rectanglem
        

        # obarví obrazovku na bílo
        screen.fill((255, 255, 255))

        # renderování našeho fontu - pomocí fontu vytvoříme text, antialiasing a barvu
        text = font.render(f"Lives: {lives}", False, "#000000")

        # text vypíšeme do obrazovky
        screen.blit(text, (700, 10))



        
        monster.draw(screen)
        monster.update()

        # na screen vykresli - surface hráče, na x,y
        # screen.blit(player_surf, player_rect)
        # na screen vykresli - surface monstra, na x,y
        player.draw(screen)
        player.update()
        


        elapsed_time += clock.get_time()
        if elapsed_time > 2000:
            invul = False

        # detekce kolize a ubírání životů v případě kolize
        if player.rect.colliderect(monster_rect):
            if not invul:
                lives -= 1
                invul = True
                elapsed_time = 0


        if lives <= 0:
            game_over = True
    else:
        screen.fill((0, 0, 0))

    # updatuje vše
    pygame.display.update()

    # omez tickrate (jak rychle hra poběží) na 60 fps
    clock.tick(60)
