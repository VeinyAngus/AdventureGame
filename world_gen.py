import pygame
import random


class World:
    def __init__(self, data):
        self.tiles = []
        self.tile_size = 100
        grass = pygame.image.load('img/grass_tile.png').convert_alpha()
        water = pygame.image.load('img/water_tile.png').convert_alpha()
        tree = pygame.image.load('img/tree.png').convert_alpha()
        apple_tree = pygame.image.load('img/apple_tree.png').convert_alpha()
        dead_tree = pygame.image.load('img/dead_tree.png').convert_alpha()
        house = pygame.image.load('img/wood_house.png').convert_alpha()
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1 or tile == 3:
                    img = pygame.transform.scale(grass, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'grass']
                    self.tiles.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(random.choice([apple_tree, tree, dead_tree]),
                                                 (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'tree']
                    self.tiles.append(tile)
                if tile == 0:
                    img = pygame.transform.scale(water, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'water']
                    self.tiles.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(house, (100, 100))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'house']
                    self.tiles.append(tile)
                col_count += 1
            row_count += 1

    def draw(self, s):
        for tile in self.tiles:
            s.blit(tile[0], tile[1])
