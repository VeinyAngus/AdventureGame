import pygame
import random


class World:
    def __init__(self, data):
        self.tiles = []
        self.tile_size = 100
        grass_raw = pygame.image.load('img/grass3.png').convert_alpha()
        grass = pygame.transform.scale(grass_raw, (100, 100))
        water_raw = pygame.image.load('img/water_tile.png').convert_alpha()
        water = pygame.transform.scale(water_raw, (100, 100))
        apple_tree_raw = pygame.image.load('img/apple_tree.png').convert_alpha()
        apple_tree = pygame.transform.scale(apple_tree_raw, (100, 100))
        house_raw = pygame.image.load('img/wood_house.png').convert_alpha()
        house = pygame.transform.scale(house_raw, (100, 100))
        apple_bare_raw = pygame.image.load('img/apple_bare.png').convert_alpha()
        apple_bare = pygame.transform.scale(apple_bare_raw, (100, 100))
        fall_tree_raw = pygame.image.load('img/fall_tree.png').convert_alpha()
        fall_tree = pygame.transform.scale(fall_tree_raw, (100, 100))
        flower_tree_raw = pygame.image.load('img/flower_tree.png').convert_alpha()
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1 or tile == 3 or tile == 4:
                    img = pygame.transform.scale(grass, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'grass']
                    self.tiles.append(tile)
                if tile == 2:
                    tree_type = random.choice(['apple_tree', 'fall_tree', 'flower_tree'])
                    if tree_type == 'apple_tree':
                        img = pygame.transform.scale(apple_tree, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * self.tile_size
                        img_rect.y = row_count * self.tile_size
                        tile = [img, img_rect, 'apple_tree']
                        self.tiles.append(tile)
                    if tree_type == 'fall_tree':
                        img = pygame.transform.scale(fall_tree, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * self.tile_size
                        img_rect.y = row_count * self.tile_size
                        tile = [img, img_rect, 'fall_tree']
                        self.tiles.append(tile)
                    if tree_type == 'flower_tree':
                        img = pygame.transform.scale(flower_tree_raw, (self.tile_size, self.tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * self.tile_size
                        img_rect.y = row_count * self.tile_size
                        tile = [img, img_rect, 'flower_tree']
                        self.tiles.append(tile)
                if tile == 0:
                    img = pygame.transform.scale(water, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'water']
                    self.tiles.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(house, (100, 100))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'house']
                    self.tiles.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(apple_bare, (100, 100))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'apple_bare']
                    self.tiles.append(tile)
                col_count += 1
            row_count += 1

    def draw(self, s):
        for tile in self.tiles:
            s.blit(tile[0], tile[1])


class House:
    def __init__(self):
        self.house_map = [[0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 2],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0]]
        self.tiles = []
        self.tile_size = 100
        floor_raw = pygame.image.load('img/floor_tile.png').convert_alpha()
        floor = pygame.transform.scale(floor_raw, (100, 100))
        door_raw = pygame.image.load('img/door_tile.png').convert_alpha()
        door = pygame.transform.scale(door_raw, (100, 100))
        chest_raw = pygame.image.load('img/chest.png').convert_alpha()
        row_count = 0
        for row in self.house_map:
            col_count = 0
            for tile in row:
                if tile == 0:
                    img = pygame.transform.scale(floor, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'floor']
                    self.tiles.append(tile)
                if tile == 1:
                    img = pygame.transform.scale(door, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'door']
                    self.tiles.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(chest_raw, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = row_count * self.tile_size
                    tile = [img, img_rect, 'chest']
                    self.tiles.append(tile)
                col_count += 1
            row_count += 1

    def draw(self, s):
        for tile in self.tiles:
            s.blit(tile[0], tile[1])
