import pygame
import sys
from Rocket import *
from Bullet import *
from Star import *
from random import randrange

# Colors
BLACK    = (   0,   0,   0)

def initialize(size):
    screen = pygame.display.set_mode(size)
    pygame.init()
    return screen

def drawGameScreen(screen, rocket, bullets, stars):
    screen.fill(BLACK)
    for b in bullets:
        b.draw(screen)
    for s in stars:
        s.draw(screen)
    rocket.draw(screen)
    
def game():
    size = (700, 900)
    screen = initialize(size)

    rocket = Rocket(size[0]/2, size[1]-100)
    bullets = []
    stars = [Star(randrange(size[0]), randrange(size[1]), size[1]) for i in range(200)]
    
    rocketYSpeed = 3
    rocketXSpeed = 3
    done = False
    bulletSpeed = 5
    pygame.display.set_caption("Spiel")

    # =================
    # = Main Programm =
    # =================
 
    clock = pygame.time.Clock()
    while not done:
        # Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.key == pygame.K_q:
                print ("The game was quit")
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                print ("Color changed")
                rocket.switchColor()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bullets.append(Bullet(rocket.x - 17, rocket.y - 5))
                bullets.append(Bullet(rocket.x + 58, rocket.y - 5))

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            rocket.moveY(-rocketYSpeed)
        if pressed[pygame.K_DOWN]:
            rocket.moveY(+rocketYSpeed)
        if pressed[pygame.K_LEFT]:
            rocket.moveX(-rocketXSpeed)
        if pressed[pygame.K_RIGHT]:
            rocket.moveX(+rocketXSpeed)

            
        # Game dynamics
        for b in bullets:
            b.move(bulletSpeed)
            if (b.isOffScreen()):
                bullets.remove(b)
                
        for s in stars:    
            s.move()
                        
        # Draw loop
            
        drawGameScreen(screen, rocket, bullets, stars)
        
        pygame.display.flip()
        clock.tick(60)

game()