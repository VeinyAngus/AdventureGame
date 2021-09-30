import pygame
import random


class Player:
    def __init__(self):
        self.img_raw = pygame.image.load('img/player.png').convert_alpha()
        self.img = pygame.transform.scale(self.img_raw, (100, 100))
        self.last_known = None
        self.x = 100
        self.y = 100
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        self.wood = 100
        self.food = 100
        self.in_house = False

    def update_rect(self):
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, s):
        self.update_rect()
        s.blit(self.img, (self.x, self.y))
