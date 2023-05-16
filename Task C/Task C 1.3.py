# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:34:59 2023

@author: Vinothini S
"""

import numpy as np

############## Translation matrix ##################
def translation_matrix(matrixarray, translation_vector):
    # Define the matrix
    matrix = np.array(matrixarray)
    # Create the translation matrix
    translation_matrix = np.array([[1, 0, translation_vector[0]],
                               [0, 1, translation_vector[1]],
                               [0, 0, 1]])

    # Translate the matrix
    translated_matrix = translation_matrix @ np.vstack((matrix.T, np.ones((1, 2))))
    return translated_matrix

matrix = [[1, 2], [3, 4]]
# Define the translation vector
translation_vector = np.array([2, 3])
translated_matrix = translation_matrix(matrix, translation_vector)
print("Original matrix:")
print(matrix)
print("\nTranslated matrix:")
print(translated_matrix[:2].T)

################## Rotation matrix ####################
def rotation_matrix(matrixarray, theta):
    # Define the matrix
    matrix = np.array(matrixarray)
    # Create the rotation matrix
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])

    # Rotate the matrix
    rotated_matrix = rotation_matrix @ matrix
    return rotated_matrix

matrix = [[1, 2], [3, 4]]
# Define the rotation angle in radians
theta = np.pi/4
rotated_matrix = rotation_matrix(matrix, theta)
print("Original matrix:")
print(matrix)
print("\nRotated matrix:")
print(rotated_matrix)

########## Scaling matrix ################

def scaling_matrix(matrixarray, scaling_factor):
    
    # Define the matrix
    matrix = np.array(matrixarray)
    # Create the scaling matrix
    scaling_matrix = np.array([[scaling_factor, 0],
                           [0, scaling_factor]])

    # Apply the scaling matrix to the matrix
    scaled_matrix = scaling_matrix @ matrix
    return scaled_matrix

matrix  = [[1, 2], [3, 4]]
# Define the scaling factor
scaling_factor = 2
scaled_matrix = scaling_matrix(matrix, scaling_factor)
print("Original matrix:")
print(matrix)
print("\nScaled matrix:")
print(scaled_matrix)





