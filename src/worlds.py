import math
from random import randint, choice

from settings import *

from monsters import Monster
from characters import Character


class World():

    def __init__(self, screen):
        self.monsters = self._init_monsters(10, screen)
        self.char = self._init_char(color="green")


    def _init_monsters(self, number, screen):
        monsters = []

        for i in range(number):
            monsters.append(Monster(screen,"src/graphics/badguy1.png",
                            (   randint(0, SCREEN_WIDTH),
                                randint(0, SCREEN_HEIGHT)),
                            (   choice([-1, 1]),
                                choice([-1, 1])), 0.1))
        return monsters

    def _init_char(self, color="red"):

        return Character(color=color)


    def _update_char(self, time_passed):
        self.char.update(time_passed)

    def _redraw_char(self, screen):
        draw_pos = self.char.image.get_rect().move(
              self.char.pos.x - self.char.image_w / 2,
              self.char.pos.y - self.char.image_h / 2)
        screen.blit(self.char.image, draw_pos)

    def _update_monsters(self, time_passed):
        for monster in self.monsters:
            monster.update(time_passed)

    def _redraw_monsters(self):
        for monster in self.monsters:
            #monster.update(time_passed)
            monster.blitme()

    def react_mouse(self, pos):
        self.char.react_mouse(pos)
        #self._update_char(time_passed)

    def react_keyboard(self, key):
        self.char.react_keyboard(key)
        #self._update_char(time_passed)

    def update(self, time_passed):
        self._update_monsters(time_passed)
        #self._update_char(time_passed)

    def redraw(self, screen):
        screen.fill(BG_COLOR)

        self._redraw_monsters()
        self._redraw_char(screen)

