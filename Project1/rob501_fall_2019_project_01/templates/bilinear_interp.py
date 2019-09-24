import numpy as np
from numpy.linalg import inv


def bilinear_interp(I, pt):
    """
    Performs bilinear interpolation for a given image point.

    Given the (x, y) location of a point in an input image, use the surrounding
    4 pixels to conmpute the bilinearly-interpolated output pixel intensity.

    Note that images are (usually) integer-valued functions (in 2D), therefore
    the intensity value you return must be an integer (use round()).

    This function is for a *single* image band only - for RGB images, you will 
    need to call the function once for each colour channel.

    Parameters:
    -----------
    I   - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).
    pt  - 2x1 np.array of point in input image (x, y), with subpixel precision.

    Returns:
    --------
    b  - Interpolated brightness or intensity value (whole number >= 0).
    """
    # --- FILL ME IN ---
    if pt.shape != (2, 1):
        raise ValueError('Point size is incorrect.')
    x = int(pt[0].round())
    y = int(pt[1].round())

    x1 = x - 1
    y1 = y + 1
    x2 = x + 1
    y2 = y - 1

    q_11 = I[y1][x1]
    q_21 = I[y2][x1]
    q_12 = I[y1][x2]
    q_22 = I[y2][x2]

    b = round(((x2 - x) * (y2 - y) * q_11 + (x - x1) * (y2 - y) * q_21 \
         + (x2 - x) * (y - y1) * q_12 + (x - x1) * (y - y1) * q_22) \
        / ((x2 - x1) * (y2 - y1)))

    # ------------------

    return b
