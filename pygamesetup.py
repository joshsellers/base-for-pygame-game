import sys
import pygame
from pygame.locals import *

FRAME_RATE = 30
SCREEN_SIZE = (500, 500)
WORLD_SIZE = (100, 100)

def rgba_tuple_to_rgb_int(rgba):
    rgb = tuple(rgba[:-1])
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    return (r << 16) + (g << 8) + b

def pygame_modules_have_loaded():
    success = pygame.display.get_init() and pygame.font.get_init() and pygame.mixer.get_init()
    return success

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.font.init()

if pygame_modules_have_loaded():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    game_screen = pygame.Surface(WORLD_SIZE)
    pygame.display.set_caption("test")
    clock = pygame.time.Clock()
    pygame.show_fps = False

    def prep():
        pass

    def handle_input(key_name):
        if key_name == "escape":
            pygame.quit()
            sys.exit()
        elif key_name == "f3":
            pygame.show_fps = not pygame.show_fps

    def update(game_screen, time):

        pygame.display.update()

    def main():
        prep()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    handle_input(key_name)

            milliseconds = clock.tick(FRAME_RATE)
            seconds = milliseconds / 1000.0
            update(game_screen, seconds)
            pygame.transform.scale(game_screen, SCREEN_SIZE, screen)

            if pygame.show_fps:
                fps_font = pygame.font.SysFont('Courier New', 12)
                fps_label = fps_font.render(f'{int(clock.get_fps())} fps', False, (0xff, 0xff, 0xff), (0, 0, 0))
                screen.blit(fps_label, (0, 0))
                pygame.display.update()

            sleep_time = (1000.0 / FRAME_RATE) - milliseconds
            if sleep_time > 0.0:
                pygame.time.wait((int(sleep_time)))
            else:
                pygame.time.wait(1)

    if __name__ == '__main__':
        main()
