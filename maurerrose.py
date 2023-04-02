from math import sin
from math import cos
from math import radians

import pygame

(width, height) = (1000, 700)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Rose Curve in Python !')

def drawMaurerRose(n, d, size):
    points =[]
    for i in range(0, 361):
        k = i * d
        r = size * sin(radians(n * k))
        x = r * cos(radians(k))
        y = r * sin(radians(k))
        list.append(points, (width / 2 + x, height / 2 + y))
    pygame.draw.lines(screen, (0, 0, 0), False, points, 5)
def drawPattern():
    drawMaurerRose(6, 71, 350)

screen.fill((250, 250, 205))
drawPattern()
pygame.display.flip()
while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        pygame.display.update()