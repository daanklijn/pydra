import numpy as np
import pygame
from scipy.ndimage.interpolation import rotate


class Output:
    def out(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.update()
            self.matrix = self.matrix[Output._x_margin:Output._x_margin + Output._width,
                          Output._y_margin:Output._y_margin + Output._height]
            self.matrix -= self.matrix.min()
            self.matrix *= 1 / self.matrix.max()  #
            colors = np.array([255, 255, 255])
            colored = np.outer(self.matrix, colors).reshape(self.matrix.shape[0], -1, len(colors))
            surf = pygame.surfarray.make_surface(colored)
            Output._display.blit(surf, (0, 0))
            pygame.display.update()

    def add(self, other):
        return Add(self, other)

    def mult(self, other):
        return Mult(self, other)

    def diff(self, other):
        return Diff(self, other)

    def rotate(self, degrees=45):
        return Rotation(self, degrees)

    def highpass(self):
        return HighPass(self)

    def lowpass(self):
        return LowPass(self)

    def modulate(self, other, amount=10):
        return Modulate(self, other, amount)

    @staticmethod
    def _init(width, height):
        pygame.init()
        Output._display = pygame.display.set_mode((width, height))
        Output._width = width
        Output._height = height
        Output._x_bound = int(width * 1.5)
        Output._y_bound = int(height * 1.5)
        Output._x_margin = int((Output._x_bound - width) / 2)
        Output._y_margin = int((Output._y_bound - height) / 2)


class Oscillator(Output):
    def __init__(self, speed, period, offset):
        self.speed = speed
        self.offset = offset
        self.period = period

    def update(self):
        self.offset += self.speed
        row = 0.5 * (np.sin(np.linspace(self.offset, self.offset + self.period, num=Output._y_bound)) + 1)
        self.matrix = np.tile(row, (Output._x_bound, 1))


class Add(Output):
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def update(self):
        self.one.update()
        self.two.update()
        self.matrix = self.one.matrix + self.two.matrix


class Diff(Output):
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def update(self):
        self.one.update()
        self.two.update()
        self.matrix = self.one.matrix - self.two.matrix


class Mult(Output):
    def __init__(self, one, two):
        self.one = one
        self.two = two

    def update(self):
        self.one.update()
        self.two.update()
        self.matrix = np.multiply(self.one.matrix, self.two.matrix)


class Rotation(Output):
    def __init__(self, one, degrees):
        self.degrees = degrees
        self.one = one

    def update(self):
        self.one.update()
        self.matrix = rotate(self.one.matrix, angle=self.degrees, reshape=False)


class LowPass(Output):
    def __init__(self, one):
        self.one = one

    def update(self):
        self.one.update()
        matrix = self.one.matrix
        mean = matrix.mean()
        filter = matrix > mean
        matrix[filter] = mean
        self.matrix = matrix


class HighPass(Output):
    def __init__(self, one):
        self.one = one

    def update(self):
        self.one.update()
        matrix = self.one.matrix
        mean = matrix.mean()
        filter = matrix < mean
        matrix[filter] = mean
        self.matrix = matrix


class Modulate(Output):
    def __init__(self, one, two, amount):
        self.one = one
        self.two = two
        self.amount = amount

    def update(self):
        self.one.update()
        self.two.update()

        indexes = np.indices(self.one.matrix.shape)
        indexes = (indexes + self.amount * np.array(self.two.matrix)).astype(int)
        indexes = np.clip(indexes, 0, self.one.matrix.shape[0] - 1)

        self.matrix = self.one.matrix[tuple(indexes)]


def osc(speed=0.1, period=100, offset=0):
    return Oscillator(speed, period, offset)


def init(height=200, width=200):
    Output._init(width, height)
