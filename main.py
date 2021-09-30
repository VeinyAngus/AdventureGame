import pygame
import random
from world_gen import World, House
from player import Player


pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

grass_raw = pygame.image.load('img/grass3.png').convert_alpha()
grass = pygame.transform.scale(grass_raw, (100, 100))
water_raw = pygame.image.load('img/water_tile.png').convert_alpha()
water = pygame.transform.scale(water_raw, (100, 100))
tree = pygame.image.load('img/tree.png').convert_alpha()
apple_tree_raw = pygame.image.load('img/apple_tree.png').convert_alpha()
apple_tree = pygame.transform.scale(apple_tree_raw, (100, 100))
wood = pygame.image.load('img/wood.png').convert_alpha()
apple_bare_raw = pygame.image.load('img/apple_bare.png').convert_alpha()
apple_bare = pygame.transform.scale(apple_bare_raw, (100, 100))
house_raw = pygame.image.load('img/wood_house.png').convert_alpha()
wood_house = pygame.transform.scale(house_raw, (100, 100))
apple = pygame.image.load('img/apple.png').convert_alpha()
stump_raw = pygame.image.load('img/stump.png').convert_alpha()
fall_stump_raw = pygame.image.load('img/fall_tree_stump.png').convert_alpha()
fall_stump = pygame.transform.scale(fall_stump_raw, (100, 100))
flower_tree_raw = pygame.image.load('img/flower_tree.png').convert_alpha()
flower_tree = pygame.transform.scale(flower_tree_raw, (100, 100))
stump = pygame.transform.scale(stump_raw, (100, 100))
flower_tree_stump_raw = pygame.image.load('img/flower_tree_stump.png').convert_alpha()
flower_tree_stump = pygame.transform.scale(flower_tree_stump_raw, (100, 100))
wood_chop = pygame.mixer.Sound('audio/wood_chop.ogg')
apple_pick = pygame.mixer.Sound('audio/apple_pick.ogg')
door_open = pygame.mixer.Sound('audio/door_open.ogg')
door_close = pygame.mixer.Sound('audio/door_close.ogg')
house_build = pygame.mixer.Sound('audio/house_build.ogg')
pygame.mixer.music.load('audio/theme.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
wood_img = pygame.transform.scale(wood, (50, 50))
apple_img = pygame.transform.scale(apple, (40, 40))
main_font = pygame.font.SysFont('arial', 40)

player = Player()

levels = dict()

running = True
map_x = 0
map_y = 0
world = World([[random.randint(0, 4) for _ in range(8)] for _ in range(8)])
levels[(map_x, map_y)] = world.tiles
house = House()
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                if not player.in_house:
                    player.x += 100
                    if player.x > 700:
                        player.x = 0
                        map_x += 1
                        if (map_x, map_y) not in levels.keys():
                            world = World([[random.randint(0, 4) for _ in range(8)] for _ in range(8)])
                            levels[(map_x, map_y)] = world.tiles
                else:
                    if player.x + 100 > 700:
                        pass
                    else:
                        player.x += 100
            if event.key == pygame.K_a:
                if not player.in_house:
                    player.x -= 100
                    if player.x < 0:
                        player.x = 700
                        map_x -= 1
                        if (map_x, map_y) not in levels.keys():
                            world = World([[random.randint(0, 4) for _ in range(8)] for _ in range(8)])
                            levels[(map_x, map_y)] = world.tiles
                else:
                    if player.x - 100 < 0:
                        pass
                    else:
                        player.x -= 100
            if event.key == pygame.K_w:
                if not player.in_house:
                    player.y -= 100
                    if player.y < 0:
                        player.y = 700
                        map_y -= 1
                        if (map_x, map_y) not in levels.keys():
                            world = World([[random.randint(0, 4) for _ in range(8)] for _ in range(8)])
                            levels[(map_x, map_y)] = world.tiles
                else:
                    if player.y - 100 < 0:
                        pass
                    else:
                        player.y -= 100
            if event.key == pygame.K_s:
                if not player.in_house:
                    player.y += 100
                    if player.y > 700:
                        player.y = 0
                        map_y += 1
                        if (map_x, map_y) not in levels.keys():
                            world = World([[random.randint(0, 4) for _ in range(8)] for _ in range(8)])
                            levels[(map_x, map_y)] = world.tiles
                else:
                    if player.y + 100 > 700:
                        pass
                    else:
                        player.y += 100
            if event.key == pygame.K_SPACE:
                if not player.in_house:
                    for tile in levels[(map_x, map_y)][:]:
                        if tile[2] == 'apple_tree' or tile[2] == 'apple_bare':
                            if player.rect.colliderect(tile[1]):
                                player.wood += 1
                                tile[0] = pygame.transform.scale(stump, (100, 100))
                                tile[2] = 'stump'
                                wood_chop.play()
                        if tile[2] == 'fall_tree':
                            if player.rect.colliderect(tile[1]):
                                player.wood += 1
                                tile[0] = pygame.transform.scale(fall_stump, (100, 100))
                                tile[2] = 'fall_stump'
                                wood_chop.play()
                        if tile[2] == 'flower_tree':
                            if player.rect.colliderect(tile[1]):
                                player.wood += 1
                                tile[0] = pygame.transform.scale(flower_tree_stump, (100, 100))
                                tile[2] = 'flower_tree_stump'
                                wood_chop.play()
                        if tile[2] == 'house':
                            if player.rect.colliderect(tile[1]):
                                player.in_house = True
                                door_open.play()
                                player.last_known = (player.x, player.y)
                                player.x, player.y = 300, 700
                if player.in_house:
                    for tile in house.tiles:
                        if tile[2] == 'door':
                            if player.rect.colliderect(tile[1]):
                                player.in_house = False
                                door_close.play()
                                player.x, player.y = player.last_known[0], player.last_known[1]
                                player.last_known = None
            if event.key == pygame.K_h:
                if not player.in_house:
                    for tile in levels[(map_x, map_y)][:]:
                        if tile[2] == 'apple_tree':
                            if player.rect.colliderect(tile[1]):
                                player.food += 1
                                tile[0] = pygame.transform.scale(apple_bare, (100, 100))
                                tile[2] = 'apple_bare'
                                apple_pick.play()
            if event.key == pygame.K_m:
                if not player.in_house:
                    for tile in levels[(map_x, map_y)][:]:
                        if tile[2] == 'grass':
                            if player.rect.colliderect(tile[1]):
                                if player.wood >= 25:
                                    player.wood -= 25
                                    tile[0] = pygame.transform.scale(wood_house, (100, 100))
                                    tile[2] = 'house'
                                    house_build.play()
    if not player.in_house:
        for tile in levels[(map_x, map_y)]:
            screen.blit(tile[0], tile[1])
    else:
        for tile in house.tiles:
            screen.blit(tile[0], tile[1])
    player.draw(screen)
    screen.blit(wood_img, (0, 0))
    screen.blit(apple_img, (120, 0))
    wood_label = main_font.render(f'{player.wood}', True, (255, 255, 255))
    food_label = main_font.render(f'{player.food}', True, (255, 255, 255))
    screen.blit(wood_label, (65, 0))
    screen.blit(food_label, (175, 0))
    pygame.display.update()
