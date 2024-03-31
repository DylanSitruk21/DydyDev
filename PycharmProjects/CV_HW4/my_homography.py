import numpy as np
import matplotlib.pyplot as plt
import cv2
import scipy

# Add imports if needed:
from tqdm import tqdm
from scipy import interpolate
from PIL import Image
from skimage import color


# end imports

# Add extra functions here:
def makePixelList(W, H):
    count = 0
    pixel = np.zeros((W * H, 3))
    for i in range(W):
        for j in range(H):
            pixel[count, 0] = i
            pixel[count, 1] = j
            pixel[count, 2] = 1
            count = count + 1
    return pixel


# Extra functions end

# HW functions:
def getPoints(im1, im2, N):
    plt.subplot(121)
    plt.imshow(im1)
    plt.subplot(122)
    plt.imshow(im2)
    points = plt.ginput(2 * N)
    p1 = np.array(points[:N]).T
    p2 = np.array(points[N:]).T
    return p1, p2


def computeH(p1, p2):
    assert (p1.shape[1] == p2.shape[1])
    assert (p1.shape[0] == 2)

    fp = p1
    tp = p2
    nbr_correspondences = fp.shape[1]
    A = np.zeros((2 * nbr_correspondences, 9))
    for i in range(nbr_correspondences):
        A[2 * i] = [fp[0][i], fp[1][i], 1, 0, 0, 0,
                    -tp[0][i] * fp[0][i], -tp[0][i] * fp[1][i], -tp[0][i]]

        A[2 * i + 1] = [0, 0, 0, fp[0][i], fp[1][i], 1,
                        -tp[1][i] * fp[0][i], -tp[1][i] * fp[1][i], -tp[1][i]]

    eig_val, eig_vec = np.linalg.eig(A.T @ A)
    index = np.argmin(eig_val)
    h = (eig_vec[:, index])
    H2to1 = h.reshape((3, 3))
    return H2to1


def warpH(im1, H):  # outsize
    im1 = color.rgb2lab(im1)
    width_in = im1.shape[1]
    height_in = im1.shape[0]
    pixel_in = makePixelList(width_in, height_in)
    pixel_relevant_out = (H @ pixel_in.T).T
    pixel_relevant_out[:, 0] = (pixel_relevant_out[:, 0] / pixel_relevant_out[:, 2])
    pixel_relevant_out[:, 1] = (pixel_relevant_out[:, 1] / pixel_relevant_out[:, 2])
    pixel_relevant_out[:, 2] = (pixel_relevant_out[:, 2] / pixel_relevant_out[:, 2])

    x1 = np.max(pixel_in[:, 0])
    x2 = np.max(pixel_in[:, 1])

    X_min = np.minimum(np.min(pixel_relevant_out[:, 0]), 0).astype(int)
    X_max = np.maximum(np.max(pixel_relevant_out[:, 0]), x1).astype(int)
    Y_min = np.minimum(np.min(pixel_relevant_out[:, 1]), 0).astype(int)
    Y_max = np.maximum(np.max(pixel_relevant_out[:, 1]), x2).astype(int)

    x = np.linspace(0, width_in - 1, width_in)
    y = np.linspace(0, height_in - 1, height_in)

    out_size = (X_max - X_min + 1, Y_max - Y_min + 1)
    warp_im1 = np.zeros((out_size[1], out_size[0], 3))
    print(np.shape(warp_im1))

    H_inv = np.linalg.inv(H)
    for chanel in range(3):
        f = scipy.interpolate.interp2d(x, y, im1[:, :, chanel], kind="cubic", fill_value=0)
        for i in tqdm(range(out_size[0] - 1)):
            for j in range(out_size[1] - 1):
                p_im2 = np.array([i, j, 1])
                p_im2_clone = p_im2 + (X_min, Y_min, 0)
                p_im1 = (H_inv @ p_im2_clone.T).T
                p_im1 = p_im1 / p_im1[2]  # normalize
                warp_im1[(p_im2[1]).astype(int), (p_im2[0]).astype(int), chanel] = f((p_im1[0]).astype(int),
                                                                                     (p_im1[1]).astype(int))
    # warp_im1 = warp_im1.astype(int)
    warp_im1 = color.lab2rgb(warp_im1)
    return warp_im1, X_min, Y_min


# def imageStitching(img1, wrap_img2):
def imageStitching(img1, wrap_img2, X_min, Y_min, write):  # img1 = im2  wrap_img2 = im1@H
    """
    if write == 1:
        H_translate = np.array([[1, 0, -X_min], [0, 1, -Y_min], [0, 0, 1]])
        img1_translate, _, _ = warpH(img1, H_translate)
        cv2.imwrite("img1_translate.jpg", img1_translate)
    else:
        img1_translate = cv2.imread("img1_translate.jpg")
        img1_translate = cv2.cvtColor(img1_translate, cv2.COLOR_BGR2GRAY)
    """
    X_max = np.maximum(img1.shape[1] + np.abs(X_min), wrap_img2.shape[1])
    Y_max = np.maximum(img1.shape[0] + np.abs(Y_min), wrap_img2.shape[0])
    panoImg = np.zeros((Y_max, X_max, 3))

    img1 = Image.fromarray(img1)
    panoImg = Image.fromarray((panoImg * 255).astype(np.uint8))
    wrap_img2 = Image.fromarray((255 * wrap_img2).astype(np.uint8))

    panoImg.paste(wrap_img2, (0, 0))
    panoImg.paste(img1, (-X_min, -Y_min))
    panoImg.show()
    panoImg = np.asarray(panoImg)
    return panoImg


def help_stitch_dydy(img1, X_min, Y_min, write):
    if write == 1:
        H_translate = np.array([[1, 0, -X_min], [0, 1, -Y_min], [0, 0, 1]])
        img1_translate, _, _ = warpH(img1, H_translate)
        cv2.imwrite("img1_translate.jpg", img1_translate)
    else:
        img1_translate = cv2.imread("img1_translate.jpg")
        img1_translate = cv2.cvtColor(img1_translate, cv2.COLOR_BGR2GRAY)
    return img1_translate


def imageStitching_dydy(img1_translate, wrap_img2):  # img1_translate = im2@H_translate  wrap_img2 = im1@H
    X_max = np.maximum(img1_translate.shape[1], wrap_img2.shape[1])
    Y_max = np.maximum(img1_translate.shape[0], wrap_img2.shape[0])
    panoImg = np.zeros((Y_max, X_max))

    panoImg = Image.fromarray(panoImg)
    img1_translate = Image.fromarray(img1_translate)
    wrap_img2 = Image.fromarray(wrap_img2)

    plt.figure(8)
    plt.imshow(img1_translate)
    plt.figure(9)
    plt.imshow(wrap_img2)
    panoImg.paste(img1_translate, (0, 0))
    panoImg = np.maximum(panoImg, wrap_img2)
    return panoImg


def ransacH(locs1, locs2, nIter, tol):
    ones = np.ones((np.shape(locs1.T)[0], 1))
    locs1_ones = np.concatenate((locs1.T, ones), axis=1)
    ones = np.ones((np.shape(locs2.T)[0], 1))
    locs2_ones = np.concatenate((locs2.T, ones), axis=1)
    for i in tqdm(range(nIter)):
        H = computeH(locs1, locs2)
        locs1_H = (H @ locs1_ones.T).T
        locs1_H[:, 0] = locs1_H[:, 0] / locs1_H[:, 2]
        locs1_H[:, 1] = locs1_H[:, 1] / locs1_H[:, 2]
        locs1_H[:, 2] = locs1_H[:, 2] / locs1_H[:, 2]
        point = 0
        while point < np.shape(locs1)[1]:
            dist = np.sum((locs1_H[point] - locs2_ones[point]) ** 2) ** 0.5
            if dist > tol:
                locs1 = np.delete(locs1, point, axis=1)
                locs2 = np.delete(locs2, point, axis=1)
                locs1_H = np.delete(locs1_H, point, axis=0)
                locs1_ones = np.delete(locs1_ones, point, axis=0)
                locs2_ones = np.delete(locs2_ones, point, axis=0)
                print("num of points = ", np.shape(locs1)[1])
            else:
                point = point + 1
    bestH = H
    return bestH


def getPoints_SIFT(im1, im2):
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(im1, None)
    kp2, des2 = sift.detectAndCompute(im2, None)
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1, des2, k=2)
    goods = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            goods.append([m])
    matchesMask = [[0, 0] for i in range(len(matches))]
    p1, p2 = [], []
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.60 * n.distance:
            matchesMask[i] = [1, 0]
            p1.append(kp1[m.queryIdx].pt)
            p2.append(kp2[m.trainIdx].pt)

    draw_params = dict(matchColor=(0, 255, 0),
                       singlePointColor=(255, 0, 0),
                       matchesMask=matchesMask,
                       flags=0)

    im3 = cv2.drawMatchesKnn(im1, kp1, im2, kp2, matches, None, **draw_params)
    plt.imshow(im3, cmap=plt.cm.gray)
    plt.axis('off')
    plt.show()
    return np.array(p1).T, np.array(p2).T


def ransacH_mik(locs1, locs2, nIter, tol):
    num_points = locs2.shape[1]
    max_p = -1
    bestH = np.zeros((3, 3))
    for i in tqdm(range(nIter)):
        indices = np.random.randint(low=0, high=num_points, size=4)
        points1 = locs1[:, indices]
        points2 = locs2[:, indices]
        H = computeH(points1, points2)
        hp2 = np.dot(H, np.vstack((locs2, np.ones((1, num_points)))))
        hp2 /= hp2[-1, :]
        hp2 = hp2[:-1, :]

        dist = np.sum((hp2 - locs1) ** 2, axis=0) ** 0.5
        num = dist[dist <= tol].shape[0]

        if num > max_p:
            bestH = H
            max_p = num

    return bestH


if __name__ == '__main__':
    print('my_homography')
    im1 = cv2.imread('data/incline_L.png')
    im2 = cv2.imread('data/incline_R.png')

    """
    Your code here
    """
    # im1 = cv2.resize(im1, (600, 400))
    # im2 = cv2.resize(im2, (600, 400))
    im1 = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
    im2 = cv2.cvtColor(im2, cv2.COLOR_BGR2RGB)

    section = 1
    print("SECTION :", section)
    if section == 1:
        p1, p2 = getPoints_SIFT(im1, im2)
        H_beach_12 = ransacH_mik(p1, p2, 5, 10)
        im1_warped, X_min, Y_min = warpH(im1, H_beach_12)
        panorama_incline_sift = imageStitching(im2, im1_warped, X_min, Y_min, 1)
        plt.imshow(panorama_incline_sift)
        plt.show()


    elif section == 2.2:
        p1, p2 = getPoints(im1, im2, 5)
        H = computeH(p1, p2)
        point_L = np.array([622, 482, 1])

        cv2.putText(im1, '.', (point_L[0], point_L[1]), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 5, cv2.LINE_AA)
        plt.subplot(121)
        plt.imshow(im1)
        plt.show()

        point_R = (H @ point_L.T).T
        point_R = point_R / point_R[2]
        cv2.putText(im2, '.', (int(point_R[0]), int(point_R[1])), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 0, 255), 5,
                    cv2.LINE_AA)
        plt.subplot(122)
        plt.imshow(im2)
        plt.show()

    elif section == 2.3:
        H_incline_manual_pas_top = np.array([[-2.60135356e-03, 2.38088978e-05, 9.81109000e-01],
                                             [-5.40385871e-04, -1.87228264e-03, 1.93427045e-01],
                                             [-2.27030448e-06, 3.78062786e-07, -7.37464179e-04]])

        H_incline_FromFB = np.array([[1.69424090E-03, 1.92939042E-05, 9.98620205E-01],
                                     [-2.63154587E-04, 2.48851693E-03, -5.23534795E-02],
                                     [-1.14541269E-06, 1.20477243E-07, 2.76877412E-03]])
        H_incline_FromFB = np.linalg.inv(H_incline_FromFB)

        im1_warped, X_min, Y_min = warpH(im1, H_incline_FromFB)
        plt.imshow(im1_warped)
        plt.show()

    elif section == 2.4:
        X_min = -598
        Y_min = -41
        im1_warped = cv2.imread("section2-3_CubLab.jpg")
        im1_warped = cv2.cvtColor(im1_warped, cv2.COLOR_BGR2RGB)
        panorama_incline = imageStitching(im2, im1_warped, X_min, Y_min, 1)
        plt.imshow(panorama_incline)
        plt.show()

    elif section == 2.5:
        p1, p2 = getPoints_SIFT(im1, im2)
        H_incline_sift = computeH(p1, p2)
        im1_warped, X_min, Y_min = warpH(im1, H_incline_sift)
        panorama_incline_sift = imageStitching(im2, im1_warped, X_min, Y_min, 1)
        plt.imshow(panorama_incline_sift)
        plt.show()

    # elif section == 2.7:
    # beach manual
    # beach sift
    # portugal manual
    # portugal sift

    # elif section == 2.8:
    # same with ransacH

    """
    best_H_incline_to_apply_to_im1 = np.array([[2.73155501e-03, 1.13563036e-04, -9.98320404e-01],
                                               [2.68201234e-04, 2.44188071e-03, -5.77904159e-02],
                                               [9.73692431e-07, 7.85909653e-08, 1.76934077e-03]])
    
    p1, p2 = getPoints_SIFT(im1, im2)
    best_H_beach = ransacH(p1, p2, 3, 1)
    if write == 1:
        im1_mul_H, X_min, Y_min = warpH(im1, best_H_beach)
        cv2.imwrite("im1_mul_H.jpg", im1_mul_H)
        print(X_min)
        print(Y_min)
    else:
        im1_mul_H = cv2.imread("im1_mul_H.jpg")
        im1_mul_H = cv2.cvtColor(im1_mul_H, cv2.COLOR_BGR2GRAY)
        X_min = -161
        Y_min = 0

    im2_translate = help_stitch_dydy(im2, X_min, Y_min, write)
    panorama = imageStitching_dydy(im2_translate, im1_mul_H)

    # panorama = imageStitching(im2, im1_mul_H, X_min, Y_min, write)
    plt.figure(10)
    plt.imshow(panorama, cmap="gray")
    plt.show()
    
    H_div2 = np.array([[1 / 2, 0, 0], [0, 1 / 2, 0], [0, 0, 1]])
    res, _, _ = warpH(im1, H_div2)
    plt.imshow(res)
    plt.show()
"""
