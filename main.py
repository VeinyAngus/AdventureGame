import pygame
import random
from world_gen import World
from player import Player


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

grass = pygame.image.load('img/grass_tile.png').convert_alpha()
water = pygame.image.load('img/water_tile.png').convert_alpha()
tree = pygame.image.load('img/tree.png').convert_alpha()
apple_tree = pygame.image.load('img/apple_tree.png').convert_alpha()
dead_tree = pygame.image.load('img/dead_tree.png').convert_alpha()
wood = pygame.image.load('img/wood.png').convert_alpha()
wood_house = pygame.image.load('img/wood_house.png').convert_alpha()
wood_chop = pygame.mixer.Sound('audio/wood_chop.ogg')
pygame.mixer.music.load('audio/theme.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
wood_img = pygame.transform.scale(wood, (50, 50))
main_font = pygame.font.SysFont('arial', 40)

player = Player()

levels = dict()

running = True
map_x = 0
map_y = 0
world = World([[random.randint(0, 3) for _ in range(8)] for _ in range(8)])
levels[(map_x, map_y)] = world.tiles
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.x += 100
                if player.x > 700:
                    player.x = 0
                    map_x += 1
                    if (map_x, map_y) not in levels.keys():
                        world = World([[random.randint(0, 3) for _ in range(8)] for _ in range(8)])
                        levels[(map_x, map_y)] = world.tiles
            if event.key == pygame.K_a:
                player.x -= 100
                if player.x < 0:
                    player.x = 700
                    map_x -= 1
                    if (map_x, map_y) not in levels.keys():
                        world = World([[random.randint(0, 3) for _ in range(8)] for _ in range(8)])
                        levels[(map_x, map_y)] = world.tiles
            if event.key == pygame.K_w:
                player.y -= 100
                if player.y < 0:
                    player.y = 700
                    map_y -= 1
                    if (map_x, map_y) not in levels.keys():
                        world = World([[random.randint(0, 3) for _ in range(8)] for _ in range(8)])
                        levels[(map_x, map_y)] = world.tiles
            if event.key == pygame.K_s:
                player.y += 100
                if player.y > 700:
                    player.y = 0
                    map_y += 1
                    if (map_x, map_y) not in levels.keys():
                        world = World([[random.randint(0, 3) for _ in range(8)] for _ in range(8)])
                        levels[(map_x, map_y)] = world.tiles
    for tile in levels[(map_x, map_y)]:
        screen.blit(tile[0], tile[1])
    player.draw(screen)
    pygame.display.update()
