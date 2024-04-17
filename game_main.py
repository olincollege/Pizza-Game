import pygame

pygame.init()

screen = pygame.display.set_mode((412, 771))

run = True
while run is True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
