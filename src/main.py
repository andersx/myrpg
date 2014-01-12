import sys

try:
    import pygame
except:
    print "sudo apt-get install python-pygame"

from worlds import World
from settings import *



def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()

    world = World(screen)

    mouse_pressed = False

    pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

    while True:
        time_passed = clock.tick(50)

        for event in pygame.event.get():

            # quit events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game()
                else:
                    key = pygame.key.get_pressed()
                    world.react_keyboard(key)

            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pressed = True

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pressed = False

        if mouse_pressed:
            pos = pygame.mouse.get_pos()

            print_msg(pos)

        world.react_mouse(pos)

        world.update(time_passed)
        world.redraw(screen)

        pygame.display.flip()

def exit_game():
    print_msg("Exiting")
    pygame.quit()
    sys.exit()



if __name__ == "__main__":
    run_game()

