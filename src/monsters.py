import os, sys
from random import randint, choice
from math import sin, cos, radians

import pygame
from pygame.sprite import Sprite

from vec2d import vec2d


class Monster(Sprite):

    def __init__(
            self, screen, img_filename, init_position,
            init_direction, speed):

        self.screen = screen
        self.speed = speed

        self.base_image = pygame.image.load(img_filename).convert_alpha()
        self.image = self.base_image

        self.pos = vec2d(init_position)

        self.direction = vec2d(init_direction).normalized()

        self._counter = 0

    def update(self, time_passed):
        self._change_direction(time_passed)

        self.image = pygame.transform.rotate(
            self.base_image, -self.direction.angle)

        displacement = vec2d(
            self.direction.x * self.speed * time_passed,
            self.direction.y * self.speed * time_passed)

        self.pos += displacement

        self.image_w, self.image_h = self.image.get_size()
        bounds_rect = self.screen.get_rect().inflate(
                        -self.image_w, -self.image_h)

        if self.pos.x < bounds_rect.left:
            self.pos.x = bounds_rect.left
            self.direction.x *= -1
        elif self.pos.x > bounds_rect.right:
            self.pos.x = bounds_rect.right
            self.direction.x *= -1
        elif self.pos.y < bounds_rect.top:
            self.pos.y = bounds_rect.top
            self.direction.y *= -1
        elif self.pos.y > bounds_rect.bottom:
            self.pos.y = bounds_rect.bottom
            self.direction.y *= -1

    def blitme(self):

        draw_pos = self.image.get_rect().move(
            self.pos.x - self.image_w / 2,
            self.pos.y - self.image_h / 2)
        self.screen.blit(self.image, draw_pos)


    def _change_direction(self, time_passed):
        """ Turn by 45 degrees in a random direction once per
            0.4 to 0.5 seconds.
        """
        self._counter += time_passed
        if self._counter > randint(400, 500):
            self.direction.rotate(45 * randint(-1, 1))
            self._counter = 0

