from enum import Enum


class Game(Enum):
    SCREEN_SIZE = 500
    PLAYERS = ('x', 'o')
    TOKEN_POSITION = [
        [(50, 50), (200, 50), (350, 50)],
        [(50, 200), (200, 200), (350, 200)],
        [(50, 350), (200, 350), (350, 350)]
    ]
    TOKEN_IMAGE = ['./assets/cross.png', './assets/circle.png']


class Color(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (198, 40, 40)  # C62828
    BLUE = (48, 63, 159)  # 303F9F
