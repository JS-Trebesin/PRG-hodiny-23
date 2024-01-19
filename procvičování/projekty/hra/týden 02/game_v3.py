import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

# vytvoř hodiny
clock = pygame.time.Clock()

# naše proměnné, které udávají výšku a šířku
screen_height = 600
screen_width = 800
# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))

player_x = 100
player_y = 200
# vytvoření surface pro postavičku hráče - načtení obrázku
player_surf = pygame.image.load("player_sprite.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))


# vytvoření surface pro postavičku monster - nepřítele - načtení obrázku
monster_surf = pygame.image.load("monster_sprite.png").convert_alpha()
monster_rect = monster_surf.get_rect(midbottom=(300, 600))

lives = 3
font = pygame.font.Font(None, 25)

# herní smyčka
while True:
    # kontroluje nám události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud dojde k události vypnout, vypne
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # proměnná key, pod ní schováme stisknutou klávesu
    key = pygame.key.get_pressed()

    # pokud je stisknutá šipka doleva, atd.
    if key[pygame.K_LEFT]:
        player_rect.left -= 10
    elif key[pygame.K_RIGHT]:
        player_rect.right += 10
    elif key[pygame.K_UP]:
        player_rect.top -= 10
    elif key[pygame.K_DOWN]:
        player_rect.bottom += 10

    # obarví obrazovku na bílo
    screen.fill((255, 255, 255))

    text = font.render(f"Lives: {lives}", False, "#000000")
    screen.blit(text, (700, 10))

    monster_rect.left -= 5
    # na screen vykresli - surface hráče, na x,y
    screen.blit(player_surf, player_rect)
    # na screen vykresli - surface monstra, na x,y
    screen.blit(monster_surf, monster_rect)

    if player_rect.colliderect(monster_rect):
        lives -= 1

    # updatuje vše
    pygame.display.update()

    # omez tickrate (jak rychle hra poběží) na 60 fps
    clock.tick(60)
