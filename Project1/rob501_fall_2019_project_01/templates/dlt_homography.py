import numpy as np
from numpy.linalg import inv, norm
from scipy.linalg import null_space
from sympy import Matrix


def dlt_homography(I1pts, I2pts):
    """
    Find perspective Homography between two images.

    Given 4 points from 2 separate images, compute the perspective homography
    (warp) between these points using the DLT algorithm.

    Parameters:
    ----------- 
    I1pts  - 2x4 np.array of points from Image 1 (each column is x, y).
    I2pts  - 2x4 np.array of points from Image 2 (in 1-to-1 correspondence).

    Returns:
    --------
    H  - 3x3 np.array of perspective homography (matrix map) between image coordinates.
    A  - 8x9 np.array of DLT matrix used to determine homography.
    """
    # --- FILL ME IN ---
    # Construct DLT Matrix A:
    # First Iteration to Construct Base Ai:
    A = np.array([-I1pts[0][0], -I1pts[0][1], -1, 0, 0, 0, I1pts[0][0] * I2pts[0][0],
                  I1pts[0][1] * I2pts[0][0], I2pts[0][0]])
    A = np.vstack([A, [0, 0, 0, -I1pts[0][0], -I1pts[0][1], -1, I1pts[0][0] * I2pts[0][1],
                       I1pts[0][1] * I2pts[0][1], I2pts[0][1]]])
    A = np.vstack([A, [-I1pts[0][2], -I1pts[0][3], -1, 0, 0, 0, I1pts[0][2] * I2pts[0][2],
                       I1pts[0][3] * I2pts[0][2], I2pts[0][2]]])
    A = np.vstack([A, [0, 0, 0, -I1pts[0][2], -I1pts[0][3], -1, I1pts[0][2] * I2pts[0][3],
                       I1pts[0][3] * I2pts[0][3], I2pts[0][3]]])

    # Iterating through all of the provided points:
    for i in range(1, len(I1pts)):
        for j in range(0, len(I1pts[0]), 2):
            A = np.vstack([A, [-I1pts[i][j], -I1pts[i][j + 1], -1, 0, 0, 0, I1pts[i][j] * I2pts[i][j],
                               I1pts[i][j + 1] * I2pts[i][j], I2pts[i][j]]])
            A = np.vstack([A, [0, 0, 0, -I1pts[i][j], -I1pts[i][j + 1], -1, I1pts[i][j] * I2pts[i][j + 1],
                               I1pts[i][j + 1] * I2pts[i][j + 1], I2pts[i][j + 1]]])
    # The H matrix is made up of the h_vector that is the null-space of the A matrix:
    h_vector = np.array(Matrix(A).nullspace())
    H = h_vector.reshape(3, 3)
    # ------------------



    return H, A
