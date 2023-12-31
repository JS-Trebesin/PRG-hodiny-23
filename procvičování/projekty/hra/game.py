import pygame
from sys import exit

pygame.init()

screen_height = 800
screen_width = 600
screen = pygame.display.set_mode((screen_height, screen_width))

player = pygame.Rect((100, 200, 50, 50))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        player.move_ip(-1, 0)
    elif key[pygame.K_d]:
        player.move_ip(1, 0)
    elif key[pygame.K_w]:
        player.move_ip(0, -1)
    elif key[pygame.K_s]:
        player.move_ip(0, 1)

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.update()
