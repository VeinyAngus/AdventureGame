import pygame
import random


class Player:
    def __init__(self):
        self.img = pygame.image.load('img/player.png').convert_alpha()
        self.x = 100
        self.y = 100
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        self.wood = 0

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))
