import numpy as np
import matplotlib.pyplot as plt


class Quaternion:
    """
    A simple class to represent a quaternion.
    """

    def __init__(self, real, i, j, k):
        self.real = real
        self.i = i
        self.j = j
        self.k = k

    def __mul__(self, other):
        """
        Multiply two quaternions.
        """
        return multiply_quaternion(self, other)

    def norm(self):
        """
        Compute the norm of the quaternion.
        """
        return np.sqrt(self.real ** 2 + self.i ** 2 + self.j ** 2 + self.k ** 2)

    def __add__(self, other):
        """
        Add two quaternions.
        """
        return add_quaternion(self, other)

    def __repr__(self):
        return f"Quaternion({self.real}, {self.i}, {self.j}, {self.k})"

    def __str__(self):
        return f"({self.real}, {self.i}, {self.j}, {self.k})"


def map_color(value, palette):
    """
    Map a fractal value to a color from the palette.

    :param value:
    :param palette:
    :return:
    """
    return palette[int(value) % len(palette)]


def pattern(resolution, color_palette):
    """
    Generate a 2D projection of the 4D fractal pattern.
    :param resolution:
    :param color_palette:
    :return:
    """
    pattern = np.zeros((resolution, resolution, 3), dtype=np.uint8)
    for x in range(resolution):
        for y in range(resolution):
            fractal_x = (x - resolution / 2) / (resolution / 4)
            fractal_y = (y - resolution / 2) / (resolution / 4)
            fractal_value = compute_4d_fractal(fractal_x, fractal_y)
            color = map_color(fractal_value, color_palette)
            pattern[x, y] = color
    return pattern


def add_quaternion(q1, q2):
    """
    Add two quaternions.
    """
    return Quaternion(q1.real + q2.real, q1.i + q2.i, q1.j + q2.j, q1.k + q2.k)


def multiply_quaternion(q1, q2):
    """
    Multiply two quaternions.
    """
    return Quaternion(q1.real * q2.real - q1.i * q2.i - q1.j * q2.j - q1.k * q2.k,
                      q1.real * q2.i + q1.i * q2.real + q1.j * q2.k - q1.k * q2.j,
                      q1.real * q2.j - q1.i * q2.k + q1.j * q2.real + q1.k * q2.i,
                      q1.real * q2.k + q1.i * q2.j - q1.j * q2.i + q1.k * q2.real)


def compute_4d_fractal(x, y, max_iter=100, escape_radius=2):
    """
    Compute the 4D fractal value for a given x and y position.
    """
    z = Quaternion(0, 0, 0, 0)
    c = Quaternion(0, x, y, 0)
    for i in range(max_iter):
        z = z * z + c
        if z.norm() > escape_radius:
            return i
    return max_iter


def generate_fractal_pattern(resolution, color_palette):
    """
    Generate a 2D projection of the 4D fractal pattern.
    """
    pattern = np.zeros((resolution, resolution, 3), dtype=np.uint8)
    for x in range(resolution):
        for y in range(resolution):
            fractal_x = (x - resolution / 2) / (resolution / 4)
            fractal_y = (y - resolution / 2) / (resolution / 4)
            fractal_value = compute_4d_fractal(fractal_x, fractal_y)
            color = map_color(fractal_value, color_palette)
            pattern[x, y] = color
    return pattern


def visualize_pattern(pattern): plt.imshow(pattern)


plt.axis('off')
plt.show()

resolution = 500
color_palette = [[255, 0, 0], [0, 255, 0], [0, 0, 255]]
palettepattern = generate_fractal_pattern(resolution, color_palette)
visualize_pattern(pattern)
