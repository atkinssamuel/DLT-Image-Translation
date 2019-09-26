import numpy as np
import matplotlib.pyplot as plt

def histogram_eq(I):
    """
    Histogram equalization for greyscale image.

    Perform histogram equalization on the 8-bit greyscale intensity image I
    to produce a contrast-enhanced image J. Full details of the algorithm are
    provided in the Szeliski text.

    Parameters:
    -----------
    I  - Single-band (greyscale) intensity image, 8-bit np.array (i.e., uint8).

    Returns:
    --------
    J  - Contrast-enhanced greyscale intensity image, 8-bit np.array (i.e., uint8).
    """
    # --- FILL ME IN ---

    # Verify I is grayscale.
    if I.dtype != np.uint8:
        raise ValueError('Incorrect image format!')

    # histogram formation
    histogram, bins = np.histogram(I.flatten(), 256, [0, 256])

    # creating an array of the cdf
    cdf = histogram.cumsum()

    # normalizing
    cdf_normalized = cdf * histogram.max() / cdf.max()

    # histogram equalization:
    cdf_masked = np.ma.masked_equal(cdf_normalized, 0)
    cdf_masked = (cdf_masked - cdf_masked.min()) * 255 / (cdf_masked.max() - cdf_masked.min())
    J = cdf_masked[I]
    # ------------------

    return J
