import pygame
from random import random

class Star:
    # Colors
    WHITE    = ( 255, 255, 255)
    GRAY     = ( 128, 128, 128)
    
    def __init__(self, x = 100, y = 100, maxY = 100):
        self.x = x
        self.y = y
        self.counter = 0
        self.maxY = maxY
        
    def move(self, byY = 1):
        self.y += byY
        if (self.y > self.maxY):
            self.y -= self.maxY
        
    def draw(self, screen):
        if (self.counter > 0):
            pygame.draw.circle(screen, Star.WHITE, (self.x, self.y), 4)
            self.counter -=1
        elif (random() < 0.001):
            pygame.draw.circle(screen, Star.WHITE, (self.x, self.y), 4)
            self.counter = 30
        else:
            pygame.draw.circle(screen, Star.GRAY, (self.x, self.y), 2)
