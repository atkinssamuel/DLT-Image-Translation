import numpy as np
from dlt_homography import dlt_homography

# Test Function:
def test_point_translation(point, H):
    point = np.append(point, 1)
    result_vector = np.dot(H, np.array(point)).astype(float)
    print(result_vector/result_vector[2])

if __name__ == "__main__":
    # Input point correspondences (4 points).
    I1pts = np.array([[5, 220, 220,   5], \
                      [1,   1, 411, 411]])
    I2pts = np.array([[375, 420, 420, 450], \
                      [ 20,  20, 300, 290]])
    (H, A) = dlt_homography(I1pts, I2pts)

    print(H.astype(float))

    test_point_translation([5, 1], H)
    test_point_translation([220, 1], H)
    test_point_translation([220, 411], H)
    test_point_translation([5, 411], H)


