import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

clock = pygame.time.Clock()

# naše proměnné, které udávají výšku a šířku
screen_height = 600
screen_width = 800
# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))


player_surf = pygame.image.load("player_sprite.png").convert_alpha()
player_x = 100
player_y = 200

monster_surf = pygame.image.load("monster_sprite.png").convert_alpha()


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

    # pokud je stisknutá šipka doleva
    if key[pygame.K_LEFT]:
        player_x -= 10
    elif key[pygame.K_RIGHT]:
        player_x += 10
    elif key[pygame.K_UP]:
        player_y -= 10
    elif key[pygame.K_DOWN]:
        player_y += 10

    # obarví obrazovku na bílo
    screen.fill((255, 255, 255))

    screen.blit(player_surf, (player_x, player_y))
    screen.blit(monster_surf, (300, 500))

    # updatuje vše
    pygame.display.update()
    clock.tick(60)
