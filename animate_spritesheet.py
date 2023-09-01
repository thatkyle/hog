import pygame
import spritesheet

def load_spritesheet(sprite_sheet_image_path):
    sprite_sheet_image = pygame.image.load(sprite_sheet_image_path).convert_alpha()
    sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)
    return sprite_sheet

def load_sprite_animation_list(sprite_sheet, animation_steps, frame_height, frame_width, scaling, bg_color=(0,0,0)):
    step_counter = 0
    sprite_animation_list = []
    for animation in animation_steps:
        temp_img_list = []
        for _ in range(animation):
            temp_img_list.append(sprite_sheet.get_image(step_counter, frame_height, frame_width, scaling, bg_color))
            step_counter += 1
        sprite_animation_list.append(temp_img_list)
    return sprite_animation_list

def draw_sprite_animation(screen, sprite_animation_list, animation_cooldown, action, position, frame, last_update, angle=0, has_health_bar=False, health=100, max_health=100):
    # Existing animation code
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(sprite_animation_list[action]):
            frame = 0
    image = sprite_animation_list[action][frame]
    if angle != 0:
        image = pygame.transform.rotate(image, angle)
        image = pygame.transform.flip(image, True, False)
        image.set_colorkey((0,0,0))
    if angle == 180:
        image = pygame.transform.flip(image, True, True)
        image.set_colorkey((0,0,0))
    screen.blit(image, position)

    if has_health_bar:
        health_bar_length = 50
        health_bar_height = 5
        health_bar_color = (0, 255, 0)
        health_bar_bg_color = (255, 0, 0)
        health_bar_surface = pygame.Surface((health_bar_length, health_bar_height), pygame.SRCALPHA)
        pygame.draw.rect(health_bar_surface, health_bar_bg_color, (0, 0, health_bar_length, health_bar_height))
        current_health_length = int((health / max_health) * health_bar_length)
        pygame.draw.rect(health_bar_surface, health_bar_color, (0, 0, current_health_length, health_bar_height))
        rotated_health_bar = pygame.transform.rotate(health_bar_surface, angle)
        if angle == 270:
            health_bar_position = (position[0] + 130, position[1] + 120)
        else:
            health_bar_position = (position[0] + 120, position[1] + 130)
        screen.blit(rotated_health_bar, health_bar_position)

    return frame, last_update