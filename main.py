#!/usr/bin/python3

import pygame, sys
from pygame.locals import KEYDOWN, K_ESCAPE
from physics import *

pygame.font.init()

# Colors
BLACK = [0, 0, 0]
PURPLE = [193, 99, 217]
PINK = [238, 101, 122]
RED = [219, 56, 56]
ORANGE = [246, 98, 31]
LIGHT_ORANGE = [249, 162, 40]
YELLOW = [254, 204, 47]
GREEN = [178, 194, 37]
LIGHT_BLUE = [51, 190, 184]
BLUE = [64, 164, 216]
ALL_COLORS = [BLUE, LIGHT_BLUE, GREEN, YELLOW, LIGHT_ORANGE, ORANGE, RED, PINK, PURPLE]

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WIN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Template")

clock = pygame.time.Clock()
FPS = 60

def color_shift(color, shift):
    color = list(color)
    for i in range(3):
        if shift[i] + color[i] > 255 or shift[i] + color[i] < 0:
            shift[i] *= -1
            color[i] += shift[i]
        else:
            color[i] += shift[i]
    return color

font = pygame.font.SysFont("Ariel", 95)
particles = [Particles((120, 260), colors = ALL_COLORS), Particles((680, 260), colors = ALL_COLORS)]

def draw(color, shift):
    WIN.fill(BLACK)
    text = font.render("HAPPY BIRTHDAY!", True, color)
    WIN.blit(text, (100, 272))
    for particle in particles:
        particle.draw(WIN)
    pygame.draw.rect(WIN, color, pygame.Rect(100, 335, 603, 10))
    pygame.display.update()
    return color_shift(color, shift)

def main():
    color = [83, 166, 255]
    shift = [1, 1, 1]
    
    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        color = draw(color, shift)

        clock.tick(FPS)

if __name__ == '__main__':
    main()