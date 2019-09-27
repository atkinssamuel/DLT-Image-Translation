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

    # Iterating through all of the provided points:
    for i in range(0, len(I1pts[0])):
        if i == 0:
            A = np.array([-I1pts[0][i], -I1pts[1][i], -1, 0, 0, 0,
                          I1pts[0][i] * I2pts[0][i], I1pts[1][i] * I2pts[0][i], I2pts[0][i]])
            A = np.vstack([A, [0, 0, 0, -I1pts[0][i], -I1pts[1][i], -1,
                               I1pts[0][i] * I2pts[1][i], I1pts[1][i] * I2pts[1][i], I2pts[1][i]]])
            continue
        A = np.vstack([A, [-I1pts[0][i], -I1pts[1][i], -1, 0, 0, 0,
                           I1pts[0][i] * I2pts[0][i], I1pts[1][i] * I2pts[0][i], I2pts[0][i]]])
        A = np.vstack([A, [0, 0, 0, -I1pts[0][i], -I1pts[1][i], -1,
                           I1pts[0][i] * I2pts[1][i], I1pts[1][i] * I2pts[1][i], I2pts[1][i]]])

    # The H matrix is made up of the h_vector that is the null-space of the A matrix:
    h_vector = null_space(A)
    # Normalizing such that the lower right entry in the matrix is 1:
    h_vector = h_vector/h_vector[len(h_vector) - 1]
    H = h_vector.reshape(3, 3)
    # ------------------

    return H, A
