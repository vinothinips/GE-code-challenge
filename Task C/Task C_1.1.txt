# -*- coding: utf-8 -*-
"""
Created on Fri May 12 17:31:14 2023

@author: Vinothini S
"""

import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return Vector2D(self.x / scalar, self.y / scalar)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        mag = self.magnitude()
        if mag != 0:
            self.x /= mag
            self.y /= mag

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return Point2D(self.x + vector.x, self.y + vector.y)

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Point2D(self.x - other.x, self.y - other.y)
        elif isinstance(other, Point2D):
            return Vector2D(self.x - other.x, self.y - other.y)

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

