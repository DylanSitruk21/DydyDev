import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
# from my_homography import getPoints_shalev
from my_homography import computeH, ransacH
import my_homography
# from my_homography import ransacH
from numpy import *
import scipy.interpolate
import cv2
from tqdm import tqdm


def computeEdges(im1, H):
    left_top_old = [0, 0, 1]
    right_top_old = [im1.shape[0], 0, 1]
    left_bottom_old = [0, im1.shape[1], 1]
    right_bottom_old = [im1.shape[0], im1.shape[1], 1]

    left_top_new = (H @ left_top_old.T).T.astype(int)
    right_top_new = (H @ right_top_old.T).T.astype(int)
    left_bottom_new = (H @ left_bottom_old.T).T.astype(int)
    right_bottom_new = (H @ right_bottom_old.T).T.astype(int)

    return left_top_new, right_top_new, left_bottom_new, right_bottom_new


"""
im1 = cv2.imread("beach1.jpg")
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
im2 = cv2.imread("beach2.jpg")
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)

p1, p2 = getPoints_SIFT(im1, im2)
# H = np.array([[0.86, -1 / 2, 0], [1 / 2, 0.86, 0], [0, 0, 1]])

p1, p2 = getPoints1(im1, im2, 8)
print(p1)
print(p2)


Point for incline images
p1 = np.array([[448.94314516, 509.14892473, 583.35604839, 623.95994624, 702.36747312,
                859.18252688, 628.16034946, 702.36747312],
               [111.53110753, 108.73083871, 219.34145699, 216.54118817, 355.15449462,
                356.55462903, 481.1665914, 482.56672581]]) 
p2 = np.array([[114.90967742, 187.27311828, 259.63655914, 309.97634409, 390.20537634,
                516.05483871, 320.98817204, 398.07096774],
               [154.28834409, 152.71522581, 270.69909677, 267.55286022, 401.26791398,
                399.6947957, 534.98296774, 528.69049462]])
                
Points for beach
p1
[[ 809.47849462  745.89139785  691.38817204  857.92580645  800.39462366
   788.2827957   558.15806452 1115.30215054]
 [ 367.75531183  443.45423656  522.18111828   83.12735484  192.13380645
   279.94455914  270.86068817  628.1596129 ]]

p2
[[ 791.03548387  745.61612903  682.02903226  812.2311828   769.83978495
   754.7         506.40752688 1081.71935484]
 [ 855.2563871   909.7596129   976.37466667  579.71230108  670.55101075
   788.64133333  761.38972043 1103.54886022]]
"""

# H = computeH(p1, p2)
'''
H_incline_LR = np.array([[1.69424090E-03, 1.92939042E-05, 9.98620205E-01],
              [-2.63154587E-04, 2.48851693E-03, -5.23534795E-02],
              [-1.14541269E-06, 1.20477243E-07, 2.76877412E-03]])
H_incline_LR = np.linalg.inv(H_incline_LR)

H_beach = np.array([[1.18761649e-03, 6.91582245e-04, 7.21939134e-02],
                    [-4.35907953e-04, 2.10177052e-03, 9.97385631e-01],
                    [-6.02151170e-07, 7.70191113e-07, 1.85649684e-03]])
#warp_img1, X_min, Y_min = warpH(im1, H_beach)
# cv2.imwrite('warp_img1.jpg', warp_img1)
warp_img1 = cv2.imread('warp_img1_beach.jpg')
# X_min = -598 for incline
# Y_min = -41
X_min = Y_min = 0
pano = imageStitching(im2, warp_img1, X_min, Y_min)

plt.figure(2)
plt.subplot(221)
plt.imshow(im1, cmap='gray')
plt.show()
plt.subplot(222)
plt.imshow(im2, cmap='gray')
plt.show()
plt.subplot(223)
plt.imshow(warp_img1, cmap='gray')
plt.show()
plt.subplot(224)
plt.imshow(pano, cmap='gray')
plt.show()

write = 1
im1 = cv2.imread("beach1.jpg")
im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2 = cv2.imread("beach2.jpg")
im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)


best_H_incline_to_apply_to_im1 = np.array([[2.73155501e-03, 1.13563036e-04, -9.98320404e-01],
                                           [2.68201234e-04, 2.44188071e-03, -5.77904159e-02],
                                           [9.73692431e-07, 7.85909653e-08, 1.76934077e-03]])

p1, p2 = getPoints_SIFT(im1, im2)
best_H_beach = ransacH(p1, p2, 10, 3)
if write == 1:
    im1_mul_H, X_min, Y_min = warpH(im1, best_H_beach)
    cv2.imwrite("im1_mul_H.jpg", im1_mul_H)
    print(X_min)
    print(Y_min)
else:
    im1_mul_H = cv2.imread("im1_mul_H.jpg")
    X_min = -161
    Y_min = 0
panorama = imageStitching(im2, im1_mul_H, X_min, Y_min, write)
plt.imshow(panorama, cmap="gray")
plt.show()
'''


im = cv2.imread("beach1.jpg")
H_unit = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
res, _, _ = warpH(im, H_unit)
plt.imshow(res)
plt.show()
