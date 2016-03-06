import pygame
from random import randrange

class Star:
    # Colors
    WHITE    = ( 255, 255, 255)
    
    def __init__(self, x = 100, y = 100, maxY = 100):
        self.x = x
        self.y = y
        self.maxY = maxY
        
    def move(self, byY = 1):
        self.y += byY
        if (self.y > self.maxY):
            self.y -= self.maxY
        
    def draw(self, screen):
        pygame.draw.circle(screen, Star.WHITE, (self.x, self.y), 2)