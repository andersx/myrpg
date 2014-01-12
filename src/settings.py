# Game parameters
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_WIDTH, SCREEN_HEIGHT = 1366, 768
BG_COLOR = 150, 150, 80

CREEP_FILENAMES = [
    'src/graphics/bluecreep.png',
    'src/graphics/pinkcreep.png',
    'src/graphics/graycreep.png']

N_CREEPS = 20

DEBUG = True


def print_msg(message_string):
    if DEBUG:
        print message_string


