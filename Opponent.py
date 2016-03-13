import pygame

class Opponent:
    # Colors
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    BLUE     = (   0,   0, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)
    MYCOLOR  = ( 255, 190,   0)
    
    def __init__(self, x, y, maxX, maxY, lives):
        self.x = x
        self.y = y
        self.maxX = maxX
        self.maxY = maxY
        self.maxLives = lives
        self.lives = lives
        self.downwards = 0
        self.phase = 0    # Phase 0: move left, Phase 1: move down, Phase 2: move right
    
    def move(self, by = 1):
        if (self.phase == 0):
            self.x -= by
            if (self.x < 25):
                self.phase = 1
                self.downwards = 0
        elif (self.phase == 1):
            self.y += by
            self.downwards += by
            if (self.downwards > 150):
                self.phase = 2
        elif (self.phase == 2):
            self.x += by
            if (self.x > self.maxX-60):
                self.phase = 3
                self.downwards = 0
        elif (self.phase == 3):
            self.y += by
            self.downwards += by
            if (self.downwards > 150):
                self.phase = 0

    def isHitByBullet(self, b):
        if (b.x > self.x-12 and b.x < self.x+38 and b.y > self.y-6 and b.y < self.y+63):
            self.lives -= 1
            return True
        else:
            return False
            
    def isHitByRocket(self, rocket):
        if (rocket.x > self.x-12 and rocket.x < self.x+38 and rocket.y > self.y-6 and rocket.y < self.y+63):
            return True
        else:
            return False
            
    def isDead(self):
        return (self.lives <= 0)
        
            
    def isOffSreen(self):
        if self.y > self.maxY:
            return True
        else:
            return False
            
    def draw(self, screen):
        # Show live
        pygame.draw.rect(screen, Opponent.WHITE, [self.x-14, self.y-17, 58, 9])
        pygame.draw.rect(screen, Opponent.GREEN, [self.x-12, self.y-15, 54 * self.lives/self.maxLives, 5])

        #Rocket Body
        pygame.draw.rect(screen, Opponent.WHITE, [self.x, self.y, 30, 45])
        pygame.draw.rect(screen, Opponent.MYCOLOR, [self.x + 2.5, self.y + 2.5, 26, 40])
        pygame.draw.rect(screen, Opponent.WHITE, [self.x + 12.5, self.y, 5, 45])
        pygame.draw.polygon(screen, Opponent.WHITE, [[self.x + 28, self.y + 45], [self.x + 15, self.y + 63], [self.x + 1, self.y + 45]])
        pygame.draw.polygon(screen, Opponent.WHITE, [[self.x + 28, self.y + 45], [self.x + 15, self.y + 25], [self.x + 1, self.y + 45]])
        pygame.draw.polygon(screen, Opponent.MYCOLOR, [[self.x + 24, self.y + 44], [self.x + 15, self.y + 59], [self.x + 5, self.y + 44]])
        pygame.draw.polygon(screen, Opponent.MYCOLOR, [[self.x + 24, self.y + 44], [self.x + 15, self.y + 29], [self.x + 5, self.y + 44]])
        #Left Holder
        pygame.draw.rect(screen, Opponent.WHITE, [self.x - 10, self.y + 22, 10, 8])
        pygame.draw.rect(screen, Opponent.MYCOLOR, [self.x - 6, self.y + 25, 6, 4])
        #Right Holder
        pygame.draw.rect(screen, Opponent.WHITE, [self.x + 30, self.y + 22, 10, 8])
        pygame.draw.rect(screen, Opponent.MYCOLOR, [self.x + 30, self.y + 25, 6, 4])
        #Right Arm
        pygame.draw.rect(screen, Opponent.WHITE, [self.x + 36, self.y - 6, 6, 55])
        pygame.draw.rect(screen, Opponent.MYCOLOR, [self.x + 38, self.y - 3, 2, 50])
        #Left Arm
        pygame.draw.rect(screen, Opponent.WHITE, [self.x - 12, self.y - 6, 6, 55])
        pygame.draw.rect(screen, Opponent.MYCOLOR, [self.x - 10, self.y - 3, 2, 50])

        