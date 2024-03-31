from matplotlib import pyplot as plt
import my_homography

# Add imports if needed:
from tqdm import tqdm
import numpy as np
import imutils
import cv2
from PIL import Image
import glob
import os

# end imports

# Add functions here:
def image_seq_to_video(imgs_path, output_path='./video.mp4', fps=15.0):
    output = output_path
    img_array = []
    for filename in glob.glob(os.path.join(imgs_path, '*.jpg')):
        img = cv2.imread(filename)
        height, width, layers = img.shape
        # img = cv2.resize(img, (width // 2, height // 2))
        img = cv2.resize(img, (width, height))
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    print(size)
    print("writing video...")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use lower case
    out = cv2.VideoWriter(output, fourcc, fps, size)
    # out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()
    print("saved video @ ", output)


def video_to_image_seq(vid_path, output_path='./datasets/OTB/img/Custom/'):
    os.makedirs(output_path, exist_ok=True)
    vidcap = cv2.VideoCapture(vid_path)
    success, image = vidcap.read()
    count = 0
    print("converting video to frames...")
    while success:
        fname = str(count).zfill(4)
        cv2.imwrite(os.path.join(output_path, fname + ".jpg"), image)  # save frame as JPEG file
        success, image = vidcap.read()
        # print('Read a new frame: ', success)
        count += 1
    print("total frames: ", count)


# Functions end

# HW functions:
def create_ref(im_path):
    image = cv2.imread(im_path)
    ratio = image.shape[0] / 300.0
    orig = image.copy()
    image = imutils.resize(image, height=300)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)
    edged_pil = Image.fromarray(edged)
    edged_pil.show()
    plt.figure(2)
    plt.imshow(edged)
    plt.show()
    cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
    screenCnt = None
    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.015 * peri, True)
        if len(approx) == 4:
            screenCnt = approx
            break

    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
    plt.figure(3)
    plt.imshow(image)
    plt.show()
    pts = screenCnt.reshape(4, 2)
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    rect *= ratio
    (tl, tr, br, bl) = rect
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))
    maxHeight = max(int(heightA), int(heightB))
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype="float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(orig, M, (maxWidth, maxHeight))
    ref_image = cv2.cvtColor(warp, cv2.COLOR_BGR2RGB)
    return ref_image


def im2im():
    ref = cv2.imread("ref.jpg")
    ref = cv2.cvtColor(ref, cv2.COLOR_BGR2RGB)
    to_paste = create_ref("inf.jpeg")
    to_paste = cv2.resize(to_paste, (ref.shape[1], ref.shape[0]))
    plt.imshow(to_paste)
    plt.show()

    bg = cv2.imread("steph_5.jpeg")
    bg = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
    p1, p2 = my_homography.getPoints_SIFT(ref, bg)
    H, _ = cv2.findHomography(p1.T, p2.T, cv2.RANSAC)
    to_paste_trans = cv2.warpPerspective(to_paste, H, (np.shape(bg)[1], np.shape(bg)[0]))

    res = np.asarray(to_paste_trans)
    res[(res[:, :, 0] == 0) & (res[:, :, 1] == 0) & (res[:, :, 2] == 0)] = np.array(
        bg[(res[:, :, 0] == 0) & (res[:, :, 1] == 0) & (res[:, :, 2] == 0)])
    plt.imsave("steph_5_inf.jpg", res)
    plt.figure(2)
    plt.imshow(res)
    plt.show()


def my_vid2vid():
    ref = cv2.imread("ref.jpg")
    ref = cv2.cvtColor(ref, cv2.COLOR_BGR2RGB)

    video_to_image_seq("steph_video3.mp4", "steph_frames3")

    for i in tqdm(range(100)):
        frame = str(i).zfill(4)

        foreground = cv2.imread("ResultNew/res{}.jpg".format(frame))
        foreground = cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB)
        foreground = cv2.rotate(foreground, cv2.ROTATE_90_COUNTERCLOCKWISE)
        foreground = cv2.resize(foreground, (ref.shape[1], ref.shape[0]))

        background = cv2.imread("steph_frames3/{}.jpg".format(frame))
        background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
        background = cv2.rotate(background, cv2.ROTATE_180)

        p1, p2 = my_homography.getPoints_SIFT(ref, background)
        H, _ = cv2.findHomography(p1.T, p2.T, cv2.RANSAC)
        foreground_trans = cv2.warpPerspective(foreground, H, (np.shape(background)[1], np.shape(background)[0]))
        res = foreground_trans
        res[(res[:, :, 0] == 0) & (res[:, :, 1] == 0) & (res[:, :, 2] == 0)] = np.array(
            background[(res[:, :, 0] == 0) & (res[:, :, 1] == 0) & (res[:, :, 2] == 0)])
        plt.imsave("steph_dance3/{}.jpg".format(frame), res)

    image_seq_to_video("steph_dance3", "steph_dance3.mp4")


if __name__ == '__main__':
    print('my_ar')
    section = 3.3
    if section == 3.1:
        print('SECTION :', section)
        ref = create_ref("book_dydy.jpeg")
        cv2.imwrite("ref.jpg", ref)
        plt.figure(1)
        plt.imshow(ref)
        plt.show()

    elif section == 3.2:
        print('SECTION :', section)
        im2im()

    elif section == 3.3:
        print('SECTION :', section)
        my_vid2vid()
