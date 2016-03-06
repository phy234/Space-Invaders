import pygame

class Bullet:
    # Colors
    YELLOW    = ( 255, 255, 0)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def move(self, byY = 1):
        self.y -= byY
        
    def isOffScreen(self):
        if (self.y <= 0):
            return True
        else:
            return False
        
    def draw(self, screen):
        pygame.draw.rect(screen, Bullet.YELLOW, [self.x, self.y, 7.5, 12.5])
