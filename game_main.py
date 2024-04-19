import pygame

pygame.init()

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Cloudy with a Chance of Pizza') #window display caption

run = True
while run is True:

    homescreen = pygame.image.load('assets/img/homescreen.png')

    screen.blit(homescreen, (0, 0)) #display homescreen img

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
