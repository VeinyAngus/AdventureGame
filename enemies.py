import pygame
import random


class Bear:
    def __init__(self):
        self.img = pygame.image.load('img/bear.png').convert_alpha()
        self.x = random.randrange(0, 800, 100)
        self.y = random.randrange(0, 800, 100)
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))