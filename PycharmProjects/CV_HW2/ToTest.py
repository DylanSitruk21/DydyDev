import cv2
import os


if not os.path.isdir('checkpoints'):
    print('yes')
    os.mkdir('checkpoints')