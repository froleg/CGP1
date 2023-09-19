import pygame
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Graphics in Python")


green = (0,255,0)
done = False
pix_arr = pygame.PixelArray(screen)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.line(screen, (255, 255, 255), [10, 30], [13, 30], 3)
    _rect = pygame.Rect([250, 300], [100, 200])
    pygame.draw.rect(screen, (0, 255, 200), _rect, 0)
    pygame.draw.rect(screen, (255, 255, 255), _rect, 5)
    for i in range(100):
        for j in range(i):
            pix_arr[200+j][200+i] = green
            pix_arr[200+i][200+j] = green
        pix_arr[200+i][200+i] = green

    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()
