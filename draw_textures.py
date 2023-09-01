import pygame
import os
import random
from constants import *

grass_array = []
stone_array = []
grass_angles = [0, 180]
stone_angles = [0, 90, 180, 270]

for filename in os.listdir('./img/textures'):
    if filename.startswith('grass'):
        img = pygame.image.load(os.path.join('./img/textures', filename))
        grass_array.append(img)
    if filename.startswith('stone'):
        img = pygame.image.load(os.path.join('./img/textures', filename))
        stone_array.append(img)

def load_tiles():
    tiles = []
    # Randomly tile the screen with images from grass_array
    for y in range(0, SCREEN_HEIGHT, 64):
        for x in range(0, SCREEN_WIDTH, 64):
            random_img = random.choice(grass_array)
            texture_angle = random.choice(grass_angles)
            rotated_img = pygame.transform.rotate(random_img, texture_angle)
            tiles.append([rotated_img, (x,y)])

    # Add stone paths
    for y in range(0, 128, 64):
        for x in range(0, SCREEN_WIDTH, 64):
            random_img = random.choice(stone_array)
            texture_angle = random.choice(stone_angles)
            rotated_img = pygame.transform.rotate(random_img, texture_angle)
            tiles.append([rotated_img, (x,y)])

    for y in range(352, 480, 64):
        for x in range(0, SCREEN_WIDTH, 64):
            random_img = random.choice(stone_array)
            texture_angle = random.choice(stone_angles)
            rotated_img = pygame.transform.rotate(random_img, texture_angle)
            tiles.append([rotated_img, (x,y)])

    for y in range(128, 352, 64):
        for x in range(SCREEN_WIDTH - 128, SCREEN_WIDTH, 64):
            random_img = random.choice(stone_array)
            texture_angle = random.choice(stone_angles)
            rotated_img = pygame.transform.rotate(random_img, texture_angle)
            tiles.append([rotated_img, (x,y)])
    
    return tiles