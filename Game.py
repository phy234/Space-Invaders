import pygame
import sys
import math
from Rocket import *
from Bullet import *
from Star import *
from Opponent import *
from Score import *
from random import randrange

# Colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

def initialize(size):
    screen = pygame.display.set_mode(size)
    pygame.init()
    return screen

def drawGameScreen(screen, rocket, bullets, opponents, stars, score):
    screen.fill(BLACK)
    for s in stars:
        s.draw(screen)
    for b in bullets:
        b.draw(screen)
    for o in opponents:
        o.draw(screen)
    rocket.draw(screen)
    score.draw(screen)
    
def game():
    size = (900, 910)
    screen = initialize(size)
    rocket = Rocket(size[0]/2, size[1]-100)
    bullets = []
    opponents = [Opponent((i+1)*125,25,size[0],size[1]) for i in range(math.floor(size[0]/125))]
    stars = [Star(randrange(size[0]), randrange(size[1]), size[1]) for i in range(200)]
    score = Score(size[1])
    rocketYSpeed = 3
    rocketXSpeed = 3
    opponentSpeed = 6
    done = False
    bulletSpeed = 5
    noOfMovesSinceLastOpponent = 0
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                score.addScore()

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
            for o in opponents:
                if (o.isHitByBullet(b)):
                    opponents.remove(o)
                    bullets.remove(b)
                    score.addScore()
                    break
            
        for s in stars:
            s.move()

        for o in opponents:
            o.move(opponentSpeed)
        
        noOfMovesSinceLastOpponent += 1
        if (noOfMovesSinceLastOpponent == 15):
            noOfMovesSinceLastOpponent = 0
            opponents.append(Opponent(size[0]-25,25,size[0],size[1]))
        
        # Draw loop
            
        drawGameScreen(screen, rocket, bullets, opponents, stars, score)
        
        pygame.display.flip()
        clock.tick(60)

game()