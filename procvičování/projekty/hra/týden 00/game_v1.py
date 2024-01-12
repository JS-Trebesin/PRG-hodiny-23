import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

# naše proměnné, které udávají výšku a šířku
screen_height = 600
screen_width = 800
# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))

# vytvoření hráče - hráč je obdélník - x, y, šířka, výška
player = pygame.Rect((100, 200, 50, 50))

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

    # pokud je stisknutá klávesa A
    if key[pygame.K_LEFT]:
        player.move_ip(-1, 0)
    if key[pygame.K_RIGHT]:
        player.move_ip(1, 0)
    if key[pygame.K_UP]:
        player.move_ip(0, -1)
    if key[pygame.K_DOWN]:
        player.move_ip(0, 1)

    # obarví obrazovku na černo
    screen.fill((0, 0, 0))

    # nakreslí vytvořený obdélník - na obrazovku, červenou barvou, obdélník-hráč
    pygame.draw.rect(screen, (255, 0, 0), player)

    # updatuje vše
    pygame.display.update()
