import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from PIL import Image


def getPoints(im1, im2, N):
    fig = plt.figure(figsize=(15, 15))
    fig.add_subplot(1, 2, 1)
    plt.imshow(im1)
    fig.add_subplot(1, 2, 2)
    plt.imshow(im2)
    print("Please click left img and then right img, point by point")
    x = plt.ginput(2 * N)
    p1 = np.asarray(x[0:][::2])
    p2 = np.asarray(x[1:][::2])
    plt.show()
    return p1.T, p2.T


def compute_p_size(im_pro, im_base, H):
    X, Y = get_min_maxXY(im_pro, H)
    maxY = max(Y[1], im_base.shape[0])
    maxX = max(X[1], im_base.shape[1])
    print(Y)
    print(Y[1])
    print(Y[0])
    minY = min(Y[0], 0)
    minX = min(X[0], 0)
    new_size = (int(maxY - minY), int(maxX - minX))
    return new_size


def computeH(p1, p2):
    assert (p1.shape[1] == p2.shape[1])
    assert (p1.shape[0] == 2)
    matA = np.zeros((p1.shape[1] * 2, 9), np.double)

    for i in range(p1.shape[1]):
        u = p2[0][i]
        v = p2[1][i]
        x = p1[0][i]
        y = p1[1][i]
        matA[i * 2] = np.array([u, v, 1, 0, 0, 0, -1 * u * x, -1 * v * x, -1 * x], np.double)
        matA[i * 2 + 1] = np.array([0, 0, 0, u, v, 1, -1 * u * y, -1 * v * y, -1 * y], np.double)

    matAA = matA.T @ matA
    Eval, Evec = np.linalg.eig(matAA)
    index = np.argmin(Eval)
    h = (Evec[:, index])
    H2to1 = h.reshape((3, 3))
    return H2to1


def get_min_maxXY(im_pro, H):
    vec1 = np.array([0, im_pro.shape[0], 1])
    vec2 = np.array([im_pro.shape[1], im_pro.shape[0], 1])
    vec3 = np.array([im_pro.shape[1], 0, 1])
    vec4 = np.array([0, 0, 1])
    point1_in_im1_space = H @ vec1
    point2_in_im1_space = H @ vec2
    point3_in_im1_space = H @ vec3
    point4_in_im1_space = H @ vec4
    point1_in_im1_space = point1_in_im1_space / point1_in_im1_space[2]
    point2_in_im1_space = point2_in_im1_space / point2_in_im1_space[2]
    point3_in_im1_space = point3_in_im1_space / point3_in_im1_space[2]
    point4_in_im1_space = point4_in_im1_space / point4_in_im1_space[2]
    print("tomerer")
    print(point4_in_im1_space)

    maxY = int(max(point2_in_im1_space[1], point1_in_im1_space[1]))
    maxX = int(max(point2_in_im1_space[0], point3_in_im1_space[0]))
    minY = int(min(point4_in_im1_space[1], point3_in_im1_space[1]))
    minX = int(min(point1_in_im1_space[0], point4_in_im1_space[0]))
    return np.array([minX, maxX]), np.array([minY, maxY]),


def warpH(im1, H, out_size):
    # print(out_size)
    pic_frec = np.zeros((out_size[0], out_size[1], 3))
    X_to_check, Y_to_check = get_min_maxXY(im1, H)

    H = np.linalg.inv(H)
    x_new_vec = []
    y_new_vec = []
    x_orig = np.arange(im1.shape[1])
    y_orig = np.arange(im1.shape[0])
    shiftX = min(X_to_check[0], 0)

    shiftY = min(Y_to_check[0], 0)
    print(shiftX)
    print(shiftY)
    print(out_size[1])
    print(out_size[0])
    print(X_to_check[1])
    print(X_to_check[0])
    from skimage import color
    im1 = color.rgb2lab(im1)
    for channel in range(3):
        zmax = -100
        zmin = 255
        z_orig = im1[:, :, channel]
        f = scipy.interpolate.interp2d(x_orig, y_orig, z_orig, kind='cubic')
        for i in range(Y_to_check[0], Y_to_check[1] - 1):
            for j in range(X_to_check[0], X_to_check[1] - 1):
                vec1 = np.array([j, i, 1])
                point_in_im1_space = H @ vec1.T
                # print(point_in_im1_space)
                point_in_im1_space = point_in_im1_space / point_in_im1_space[2]
                #                 x_new_vec.append(point_in_im1_space[0])
                #                 y_new_vec.append(point_in_im1_space[1])

                znew = f(point_in_im1_space[0], point_in_im1_space[1])
                #                 znew =znew/255

                if znew > zmax:
                    zmax = znew
                if znew < zmin:
                    zmin = znew
                if channel == 0:
                    if znew > 100:
                        znew = 100
                    if znew < 0:
                        znew = 0
                if channel != 0:
                    if znew > 127:
                        znew = 127
                    if znew < -128:
                        znew = -128
                #                 pic_frec[i][j][2-channel]=znew
                # print(i-shiftY,j-shiftX)
                pic_frec[i - shiftY][j - shiftX][channel] = znew

                if point_in_im1_space[0] >= im1.shape[1] or point_in_im1_space[1] >= im1.shape[0] or point_in_im1_space[
                    0] < 0 or point_in_im1_space[1] < 0:
                    pic_frec[i - shiftY][j - shiftX][channel] = 0
    #                     pic_frec[i][j][2-channel]=0

    # print(zmax, zmin)
    #     print(x_new_vec)
    #     print(y_new_vec)

    """
    Your code here
    """
    warp_im1 = pic_frec
    warp_im1 = color.lab2rgb(warp_im1)

    # print(zmax,zmin)
    return warp_im1


def imageStitching(img1, wrap_img2):
    print(img1.shape[0], wrap_img2.shape[0])
    max_x = max(img1.shape[0], wrap_img2.shape[0])
    max_y = max(img1.shape[1], wrap_img2.shape[1])
    panoImg = np.zeros((max_x, max_y, 3))
    for channel in range(3):
        for i in range(max_x):
            for j in range(max_y):
                if wrap_img2[i][j][channel] > 0:
                    panoImg[i][j][channel] = wrap_img2[i][j][channel]
                elif i < img1.shape[0] and j < img1.shape[1]:
                    panoImg[i][j][channel] = img1[i][j][channel]
                else:
                    panoImg[i][j][channel] = 0
    return panoImg


"""
im1 = Image.open("pf_scan_scaled.jpg")
im2 = Image.open("pf_scan_scaled.jpg")
p1, p2 = getPoints(im1, im2, 3)

H2to1 = computeH(np.array([[1, 2, 3], [1, 2, 3]]), np.array([[1, 2, 3], [1, 2, 3]]))
im1 = Image.open("pf_scan_scaled.jpg").convert('L')
im1 = cv2.imread("pf_scan_scaled.jpg")
H = np.array([[0.86, -1/2, 0], [1/2, 0.86, 0], [0, 0, 1]])
# H = np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]])
out_size = compute_p_size(im1, im2, H)
warp_im1 = warpH(im1, H, out_size)
plt.imshow(warp_im1)
plt.show()
"""

im1 = cv2.imread("incline_L.png")
#im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
im2 = cv2.imread("incline_R.png")
#im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)

# H = np.array([[0.86, -1 / 2, 0], [1 / 2, 0.86, 0], [0, 0, 1]])
"""
p1, p2 = getPoints(im1, im2, 8)
print(p1)
print(p2)
"""
p1 = np.array([[448.94314516, 509.14892473, 583.35604839, 623.95994624, 702.36747312,
                859.18252688, 628.16034946, 702.36747312],
               [111.53110753, 108.73083871, 219.34145699, 216.54118817, 355.15449462,
                356.55462903, 481.1665914, 482.56672581]])
p2 = np.array([[114.90967742, 187.27311828, 259.63655914, 309.97634409, 390.20537634,
                516.05483871, 320.98817204, 398.07096774],
               [154.28834409, 152.71522581, 270.69909677, 267.55286022, 401.26791398,
                399.6947957, 534.98296774, 528.69049462]])
H = computeH(p1, p2)

out_size = compute_p_size(im1, im2, H)
warp_im1 = warpH(im1, H, out_size)

# pano = imageStitching(im2, warp_img1)

plt.subplot(221)
plt.imshow(im1)
plt.show()
plt.subplot(222)
plt.imshow(im2)
plt.show()
plt.subplot(223)
plt.imshow(warp_im1)
plt.show()
