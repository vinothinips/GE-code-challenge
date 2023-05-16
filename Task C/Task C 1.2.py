# -*- coding: utf-8 -*-
"""
Created on Fri May 12 17:35:24 2023

@author: Vinothini S
"""

class Matrix3x3:
    def __init__(self, elements):
        self.elements = elements

    def __mul__(self, other):
        result = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.elements[i][k] * other.elements[k][j]
        return Matrix3x3(result)

    def inverse(self):
        det = self.determinant()
        if det == 0:
            raise ValueError("Matrix is not invertible")
        a = self.elements
        b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        b[0][0] = (a[1][1]*a[2][2] - a[1][2]*a[2][1])/det
        b[0][1] = (a[0][2]*a[2][1] - a[0][1]*a[2][2])/det
        b[0][2] = (a[0][1]*a[1][2] - a[0][2]*a[1][1])/det
        b[1][0] = (a[1][2]*a[2][0] - a[1][0]*a[2][2])/det
        b[1][1] = (a[0][0]*a[2][2] - a[0][2]*a[2][0])/det
        b[1][2] = (a[0][2]*a[1][0] - a[0][0]*a[1][2])/det
        b[2][0] = (a[1][0]*a[2][1] - a[1][1]*a[2][0])/det
        b[2][1] = (a[0][1]*a[2][0] - a[0][0]*a[2][1])/det
        b[2][2] = (a[0][0]*a[1][1] - a[0][1]*a[1][0])/det
        return Matrix3x3(b)

    def determinant(self):
        a = self.elements
        return a[0][0] * (a[1][1]*a[2][2] - a[1][2]*a[2][1]) \
             - a[0][1] * (a[1][0]*a[2][2] - a[1][2]*a[2][0]) \
             + a[0][2] * (a[1][0]*a[2][1] - a[1][1]*a[2][0])

    def transform_point(self, point):
        x, y, z = point
        a = self.elements
        xp = a[0][0]*x + a[0][1]*y + a[0][2]*z
        yp = a[1][0]*x + a[1][1]*y + a[1][2]*z
        zp = a[2][0]*x + a[2][1]*y + a[2][2]*z
        return xp, yp, zp

    def transform_vector(self, vector):
        x, y, z = vector
        a = self.elements
        xp = a[0][0]*x + a[0][1]*y + a[0][2]*z
        yp = a[1][0]*x + a[1][1]*y + a[1][2]*z
        zp = a[2][0]*x + a[2][1]*y + a[2][2]*z
        return xp, yp, zp

