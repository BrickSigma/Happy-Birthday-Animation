import pygame
import random

class Particles:
    def __init__(self, pos, spread = 20, height = -5, verticle = True, timer = 6, decay = 0.05, gravity = 0.1, colors = [(255, 0, 0)]):
        self.pos = list(pos)
        self.spread = spread
        self.__spread_offset = spread/20
        self.height = height
        self.verticle = verticle
        self.timer = timer
        self.decay = decay
        self.gravity = gravity
        self.colors = colors
        self.particles = []
    def draw(self, surface):
        if self.verticle:
            self.particles.append([self.pos[:], [(random.randint(0, self.spread) / 10 - self.__spread_offset), self.height], random.randint(self.timer-2, self.timer)])
        else:
            self.particles.append([self.pos[:], [self.height, (random.randint(0, self.spread) / 10 - self.__spread_offset)], random.randint(self.timer-2, self.timer)])
 
        for particle in self.particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= self.decay
            if self.verticle:
                particle[1][1] += self.gravity
            else:
                particle[1][0] += self.gravity
            pygame.draw.circle(surface, random.choice(self.colors), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)