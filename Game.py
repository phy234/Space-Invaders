import pygame
import sys
import math
from Rocket import *
from Bullet import *
from Star import *
from Opponent import *
from random import randrange

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

def initialize(size):
    screen = pygame.display.set_mode(size)
    pygame.init()
    return screen

def drawGameScreen(screen, rocket, bullets, opponents, stars):
    screen.fill(BLACK)
    for s in stars:
        s.draw(screen)
    for b in bullets:
        b.draw(screen)
    for o in opponents:
        o.draw(screen)
    rocket.draw(screen)
    font = pygame.font.SysFont('Calibri', 35, True, False)
    text = font.render("Score: ",True,WHITE)
    screen.blit(text, [10, 860])
    
def game():
    size = (900, 910)
    screen = initialize(size)

    rocket = Rocket(size[0]/2, size[1]-100)
    bullets = []
    opponents = [Opponent((i+1)*125,25,size[0],size[1]) for i in range(math.floor(size[0]/125))]
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
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_q) or (event.type == pygame.QUIT):
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

        for o in opponents:
            o.move(3)

        # Draw loop
            
        drawGameScreen(screen, rocket, bullets, opponents, stars)
        
        pygame.display.flip()
        clock.tick(60)

game()