# Billboard hack script file.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.path import Path
from imageio import imread, imwrite

from dlt_homography import dlt_homography
from bilinear_interp import bilinear_interp
from histogram_eq import histogram_eq

def show_rectangle(I, coord):
    plt.imshow(I)
    xs, ys = zip(*coord)
    plt.plot(xs, ys)
    plt.show()

def billboard_hack():
    """
    Hack and replace the billboard!

    Parameters:
    ----------- 

    Returns:
    --------
    Ihack  - Hacked RGB intensity image, 8-bit np.array (i.e., uint8).
    """
    # Bounding box in Y & D Square image.
    bbox = np.array([[404, 490, 404, 490], [38,  38, 354, 354]])

    # Point correspondences.
    Iyd_pts = np.array([[416, 485, 488, 410], [40,  61, 353, 349]])
    Ist_pts = np.array([[2, 219, 219, 2], [2, 2, 410, 410]])

    Iyd = imread('../billboard/yonge_dundas_square.jpg')
    Ist = imread('../billboard/uoft_soldiers_tower_dark.png')

    Ihack = np.asarray(Iyd)
    Ist = np.asarray(Ist)

    #--- FILL ME IN ---
    Iyd = np.asarray(Iyd)
    Ist_poly = [[70, 80], [115, 70], [153, 80], [152, 355], [63, 355], [70, 80]]
    Iyd_poly = [[404, 38], [490, 38], [490, 354], [404, 354], [404, 38]]

    # show_rectangle(Ist, Ist_poly)

    # Let's do the histogram equalization first.
    Ist = histogram_eq(Ist)

    # Compute the perspective homography we need...
    H, A = dlt_homography(Ist_pts, Iyd_pts)

    # Main 'for' loop to do the warp and insertion - 
    # this could be vectorized to be faster if needed!
    path = matplotlib.path.Path(Ist_poly)
    for i in range(len(Ist)): # i -> 411
        for j in range(len(Ist[0])): # j -> 220
            if path.contains_point([i, j]):
                [u, v, normal] = np.dot(H, np.array([i, j, 1]))
                [u, v, normal] = [u, v, normal]/normal
                u = int(u.round())
                v = int(v.round())
                Ihack[v][u] = Ist[j][i]

    Iyd_shape = (601, 900, 3) # = Ihack_shape - 600 down, 900 across, 3 color channels
    Ist_shape = (411, 220) # 411 down, 220 across, 1 color channel


    # You may wish to make use of the contains_points() method
    # available in the matplotlib.path.Path class!

    #------------------

    plt.imshow(Ihack)
    plt.show()
    plt.imshow(Iyd)
    plt.show()
    # imwrite(Ihack, 'billboard_hacked.png');

    return Ihack