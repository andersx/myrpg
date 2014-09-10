import os, sys
from random import randint, choice
from math import sin, cos, radians

import pygame
from pygame.sprite import Sprite

from sprite_sheet import spritesheet
from settings import *
from vec2d import vec2d



class Character(Sprite):

    # Whether berserker mode 
    berserk = False

    color_key = 7

    def __init__(self, color="red"):

        if color == "red":
            self.color_key = 4
        elif color == "blue":
            self.color_key = 2
        else:
            self.color_key = 7


        Sprite.__init__(self)

        self.char_sprites = spritesheet("src/graphics/sheets/demons.png")


        self.image_down  = self.char_sprites.get_img(self.color_key, 4)
        self.image_left  = self.char_sprites.get_img(self.color_key, 5)
        self.image_right = self.char_sprites.get_img(self.color_key, 6)
        self.image_up    = self.char_sprites.get_img(self.color_key, 7)

        self.image = self.image_up

        self.pos = vec2d((SCREEN_WIDTH//2, SCREEN_HEIGHT//2))

        self.image_w, self.image_h = self.image.get_size()

    def update(self, time_passed):
        return

    
    def _toggle_berserk(self):

        if not self.berserk:
            self.image_down  = self.char_sprites.get_img(1, 0)
            self.image_left  = self.char_sprites.get_img(1, 1)
            self.image_right = self.char_sprites.get_img(1, 2)
            self.image_up    = self.char_sprites.get_img(1, 3)

            self.berserk = True

        else:
            self.image_down  = self.char_sprites.get_img(self.color_key, 4)
            self.image_left  = self.char_sprites.get_img(self.color_key, 5)
            self.image_right = self.char_sprites.get_img(self.color_key, 6)
            self.image_up    = self.char_sprites.get_img(self.color_key, 7)

            self.berserk = False

        return

    def react_keyboard(self, key):
        if key[pygame.K_1]:
            self._toggle_berserk()

    def react_mouse(self, mouse_pos):

        rel = self.pos - mouse_pos

        if abs(rel.y) > abs(rel.x):
            if rel.y > 0:
                self.image = self.image_up
            else:
                self.image = self.image_down
        else:
            if rel.x > 0:
                self.image = self.image_left
            else:
                self.image = self.image_right

        return






