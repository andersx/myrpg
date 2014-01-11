try:
    import pygame
except:
    print "sudo apt-get install python-pygame"

import sys
import math
from random import randint, choice

from settings import *

from monsters import Creep


def quit_game():
    pygame.quit()
    sys.exit()

class World():

    def __init__(self, screen):
        self.monsters = self.init_monsters(10, screen)
        self.char = self.init_char(screen)


    def init_monsters(self, number, screen):
        monsters = []

        for i in range(number):
            monsters.append(Creep(screen,"src/graphics/badguy1.png",
                            (   randint(0, SCREEN_WIDTH),
                                randint(0, SCREEN_HEIGHT)),
                            (   choice([-1, 1]),
                                choice([-1, 1])), 0.1))
        return monsters

    def init_char(self, screen):

        return Creep(screen,"src/graphics/goodguy.png",
                            (   int(SCREEN_WIDTH/2),
                                int(SCREEN_HEIGHT/2)),
                            (   choice([-1, 1]),
                                choice([-1, 1])), 0.1)



    def update_char(self, time_passed):
        self.char.update(time_passed)

    def redraw_char(self):
        self.char.blitme()

    def update_monsters(self, time_passed):
        for monster in self.monsters:
            monster.update(time_passed)

    def redraw_monsters(self):
        for monster in self.monsters:
            #monster.update(time_passed)
            monster.blitme()


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()

    world = World(screen)


    # Create N_CREEPS random creeps.
    while True:
        time_passed = clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit_game()
            elif event.type == pygame.QUIT:
                exit_game()
        # Redraw the background

        screen.fill(BG_COLOR)


        world.update_monsters(time_passed)
        world.redraw_monsters()
        world.update_char(time_passed)
        world.redraw_char()


        ## Update and redraw all creeps
        #for creep in world.monsters:
        #    creep.update(time_passed)
        #    creep.blitme()

        pygame.display.flip()


def exit_game():
   pygame.quit()
   sys.exit()



if __name__ == "__main__":
    run_game()

