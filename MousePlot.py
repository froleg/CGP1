import pygame
from pygame.locals import *
from Utils import *

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Graphs in Python')

def plot_point(points):
    pygame.draw.line(screen, (255, 255, 255), points[0], points[1], 3)
    print(points)

done = False
points = []
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            points.append(p)
    if len(points)>1:
        plot_point(points)
        points = []
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()
