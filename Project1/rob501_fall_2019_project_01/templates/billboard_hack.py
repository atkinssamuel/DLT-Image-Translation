# Billboard hack script file.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from imageio import imread, imwrite

from dlt_homography import dlt_homography
from bilinear_interp import bilinear_interp
from histogram_eq import histogram_eq

def billboard_hack():
    """
    Hack and replace the billboard!

    Parameters:
    ----------- 

    Returns:
    --------
    Ihack  - Hacked RGB intensity image, 8-bit np.array (i.e., uint8).
    """
    bbox = np.array([[404, 490, 404, 490], [38, 38, 354, 354]])

    # Point correspondences.
    Iyd_pts = np.array([[416, 485, 488, 410], [40, 61, 353, 349]])
    Ist_pts = np.array([[2, 218, 218, 2], [2, 2, 409, 409]])

    Iyd = imread('../billboard/yonge_dundas_square.jpg')
    Ist = imread('../billboard/uoft_soldiers_tower_dark.png')

    Ihack = np.asarray(Iyd)
    Ist = np.asarray(Ist)

    # -----------------------------------------------------------------------------------------------------------------#
    # --- FILL ME IN ---
    # Let's do the histogram equalization first.
    Ist_balanced = histogram_eq(Ist)

    # Compute the perspective homography we need...
    H, A = dlt_homography(Iyd_pts, Ist_pts)

    # Main 'for' loop to do the warp and insertion -
    # this could be vectorized to be faster if needed!
    UL = [bbox[0][0], bbox[1][0]]  # Upper Left
    UR = [bbox[0][1], bbox[1][1]]  # Upper Right
    # Updated bounding box definition:
    UR = [488, 59]
    BL = [bbox[0][2], bbox[1][2]]  # Bottom Left
    BR = [bbox[0][3], bbox[1][3]]  # Bottom Right
    Iyd_poly = [UL, UR, BR, BL, UL]
    codes = [
        Path.MOVETO,
        Path.LINETO,
        Path.LINETO,
        Path.LINETO,
        Path.CLOSEPOLY
    ]
    billboard_path = Path(Iyd_poly, codes)
    for v in range(len(Iyd)):
        for u in range(len(Iyd[0])):
            if billboard_path.contains_point([u, v]):
                [x, y, normal] = np.dot(H, np.array([u, v, 1]))
                [x, y, normal] = [x, y, normal] / normal
                if (x < 219 and y < 410):
                    Ihack[v][u] = bilinear_interp(Ist_balanced, np.array([[x, y]]).T)

    Ihack = Ihack.astype(np.uint8)
    #------------------

    return Ihack
