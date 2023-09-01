import pygame
from draw_textures import load_tiles
from constants import *
from animate_spritesheet import load_spritesheet, load_sprite_animation_list, draw_sprite_animation

# Initialize Pygame
pygame.init()

# Create a 480x640 screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('TD')

w_frame = 0
w_last_update = pygame.time.get_ticks()
n_frame = 0
n_last_update = pygame.time.get_ticks()
a_frame = 0
a_last_update = pygame.time.get_ticks()
c_frame = 0
c_last_update = pygame.time.get_ticks()

w_sprite_sheet = load_spritesheet('img/sprites/spr_WarriorAttack_strip33.png')
w_sprite_animation_list = load_sprite_animation_list(w_sprite_sheet, [33], 96, 96, 3)
n_sprite_sheet = load_spritesheet('img/sprites/spr_NecromancerAttackWithEffect_strip47.png')
n_sprite_animation_list = load_sprite_animation_list(n_sprite_sheet, [32], 128, 128, 2.25)
a_sprite_sheet = load_spritesheet('img/sprites/spr_SkeletonArcherAttack_strip34.png')
a_sprite_animation_list = load_sprite_animation_list(a_sprite_sheet, [32], 96, 96, 3)
c_sprite_sheet = load_spritesheet('img/sprites/spr_SkeletonCatRun_strip8.png')
c_sprite_animation_list = load_sprite_animation_list(c_sprite_sheet, [8], 96, 96, 3)

tiles = load_tiles()
# Main loop
running = True
dx = -200
dy = -120
c_angle = 0
c_health = 100
while running:
    for tile in tiles:
        screen.blit(tile[0], tile[1])

    c_frame, c_last_update = draw_sprite_animation(screen, c_sprite_animation_list, 60, 0, (dx, dy), c_frame, c_last_update, c_angle, True, c_health)
    c_health -= 0.1
    if dx < 400 and dy < 250:
        dx += 2
    elif dx > 399 and dy < 250:
        dy += 2
        c_angle = 270
    else:
        c_angle = 180
        dx -= 2

    if c_health < 0 or (dx < -300 and dy > 0):
        c_health = 100
        dx = -200
        dy = -120
        c_angle = 0
    
    w_frame, w_last_update = draw_sprite_animation(screen, w_sprite_animation_list, 60, 0, (-64, 32), w_frame, w_last_update)
    n_frame, n_last_update = draw_sprite_animation(screen, n_sprite_animation_list, 60, 0, (64, 160), n_frame, n_last_update)
    a_frame, a_last_update = draw_sprite_animation(screen, a_sprite_animation_list, 60, 0, (192, 32), a_frame, a_last_update)
    w_frame, w_last_update = draw_sprite_animation(screen, w_sprite_animation_list, 60, 0, (320, 160), w_frame, w_last_update)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
