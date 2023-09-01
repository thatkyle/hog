import pygame
from animate_spritesheet import load_spritesheet, load_sprite_animation_list, draw_sprite_animation

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

# sprite_sheet_image = pygame.image.load('./img/spr_WarriorAttack_strip33.png').convert_alpha()

BG = (50, 50, 50)
BLACK = (0, 0, 0)

sprite_sheet = load_spritesheet('./img/spr_WarriorIdle_strip21.png')
sprite_animation_list = load_sprite_animation_list(sprite_sheet, [21])

run = True
while run:
    screen.fill(BG)
    
    draw_sprite_animation(screen, sprite_animation_list, 30, 0, (100, 100))

    for event in pygame.event.get():	
        if event.type == pygame.QUIT:
                run = False

    pygame.display.update()

pygame.quit()