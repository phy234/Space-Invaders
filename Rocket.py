import pygame

class Rocket:
    # Colors
    BLACK    = (   0,   0,   0)
    WHITE    = ( 255, 255, 255)
    BLUE     = (   0,   0, 255)
    GREEN    = (   0, 255,   0)
    RED      = ( 255,   0,   0)

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.color = Rocket.BLUE
        self.rocketVelocity = 0.5
        self.rocketOffset = 0
    
    def moveX(self, byX = 1):
        self.x += byX
    
    def moveY(self, byY = 1):
        self.y += byY
        
    def switchColor(self):
        if (self.color == Rocket.RED):
            self.color = Rocket.BLUE
        else:
            self.color = Rocket.RED
            
    def draw(self, screen):
        #Rocket Body
        pygame.draw.rect(screen, Rocket.WHITE, [self.x, self.y , 50, 70])
        pygame.draw.rect(screen, self.color, [self.x + 2.5, self.y + 2.5 , 46, 66])
        pygame.draw.rect(screen, Rocket.WHITE, [self.x + 22.2, self.y, 5, 70])
        pygame.draw.polygon(screen, Rocket.WHITE, [[self.x + 48, self.y - 1], [self.x + 24, self.y - 30], [self.x + 1, self.y - 1]])
        pygame.draw.polygon(screen, Rocket.WHITE, [[self.x + 48, self.y - 1], [self.x + 24, self.y + 30], [self.x + 1, self.y - 1]])
        pygame.draw.polygon(screen, self.color, [[self.x + 42, self.y - 1], [self.x + 24, self.y - 23], [self.x + 7, self.y - 1]])
        pygame.draw.polygon(screen, self.color, [[self.x + 42, self.y - 1], [self.x + 24, self.y + 23], [self.x + 7, self.y - 1]])
        #Left Holder
        pygame.draw.rect(screen, Rocket.WHITE, [self.x - 15, self.y + 32.5 + self.rocketOffset, 15, 10])
        pygame.draw.rect(screen, self.color, [self.x - 10, self.y + 35 + self.rocketOffset, 10, 5])
        #Right Holder        
        pygame.draw.rect(screen, Rocket.WHITE, [self.x + 50, self.y + 32.5 + self.rocketOffset, 10, 10])
        pygame.draw.rect(screen, self.color, [self.x + 50, self.y + 35 + self.rocketOffset, 10, 5])
        #Right Arm        
        pygame.draw.rect(screen, Rocket.WHITE, [self.x + 58, self.y - 7.5 + self.rocketOffset, 9, 75])
        pygame.draw.rect(screen, self.color, [self.x + 60, self.y - 5 + self.rocketOffset, 5, 70])
        #Left Arm
        pygame.draw.rect(screen, Rocket.WHITE, [self.x - 17, self.y - 7.5 + self.rocketOffset, 9, 75])
        pygame.draw.rect(screen, self.color, [self.x - 15, self.y - 5 + self.rocketOffset, 5, 70])
        
        self.rocketOffset += self.rocketVelocity
        if (self.rocketOffset > 0.5):
            self.rocketVelocity *= -1
        elif (self.rocketOffset < -3):
            self.rocketVelocity *= -1