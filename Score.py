import pygame
import sys

class Score():
    # Colors
    WHITE    = ( 255, 255, 255)
    
    def __init__ (self, maxY):
        self.score = 0
        self.maxY = maxY
        
    def addScore(self, by=1):
        self.score += by 
        
    def draw(self, screen):
        font = pygame.font.SysFont('Calibri', 35, True, False)
        text = font.render("Score: " + str(self.score), True, Score.WHITE)
        screen.blit(text, [10, self.maxY-35])