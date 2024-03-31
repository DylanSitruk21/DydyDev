import cv2
import glob
import os

# Add imports if needed:
from tqdm import tqdm
import numpy as np
from PIL import Image
import torch
import torchvision.transforms as transforms


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


def DeepLearningSegmentation(image, model, device, L):
    # perform pre-processing
    input_tensor = preprocess(image)
    input_batch = input_tensor.unsqueeze(0)  # create a mini-batch of size 1 as expected by the model

    # send to device
    model = model.to(device)
    input_batch = input_batch.to(device)
    # forward pass
    with torch.no_grad():
        output = model(input_batch)['out'][0]
    output_predictions = output.argmax(0)

    # create a color pallette, selecting a color for each class
    palette = torch.tensor([2 ** 25 - 1, 2 ** 15 - 1, 2 ** 21 - 1])
    colors = torch.as_tensor([i for i in range(21)])[:, None] * palette
    colors = (colors % 255).numpy().astype("uint8")

    # plot the semantic segmentation predictions of 21 classes in each color
    r = Image.fromarray(output_predictions.byte().cpu().numpy()).resize(image.size)
    r.putpalette(colors)

    labels = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle',
              'bus', 'car', 'cat', 'chair', 'cow',
              'diningtable', 'dog', 'horse', 'motorbike', 'person',
              'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

    # what labels were recognized?
    np.unique(output_predictions.cpu().numpy())
    # create a mask
    mask = torch.zeros_like(output_predictions).float().to(device)
    mask[output_predictions == L] = 1

    masked_img = image * mask.unsqueeze(2).byte().cpu().numpy()

    return masked_img, r


model = torch.hub.load('pytorch/vision:v0.5.0', 'deeplabv3_resnet101', pretrained=True)
model.eval()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
preprocess = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
video_to_image_seq("fortnite2.mp4", "fortnite2_frames")
video_to_image_seq("fortnite3.mp4", "fortnite3_frames")
for i in tqdm(range(100)):
    frame = str(i).zfill(4)
    bg = Image.open('steph_dance3/{}.jpg'.format(frame))

    to_seg = Image.open('./fortnite2_frames/{}.jpg'.format(frame))
    fg, mask = DeepLearningSegmentation(to_seg, model, device, 15)
    mask = np.asarray(mask)
    _, mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
    mask = Image.fromarray(mask)
    mask = mask.convert('L')
    fg = Image.fromarray(fg)
    bg.paste(fg, (0, 0), mask)

    to_seg = Image.open('./fortnite3_frames/{}.jpg'.format(frame))
    fg, mask = DeepLearningSegmentation(to_seg, model, device, 15)
    mask = np.asarray(mask)
    _, mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
    mask = Image.fromarray(mask)
    mask = mask.convert('L')
    fg = Image.fromarray(fg)
    bg.paste(fg, (1000, 0), mask)
    res = np.asarray(bg)
    cv2.imwrite("steph_fortnite23/{}.jpg".format(frame), cv2.cvtColor(res, cv2.COLOR_BGR2RGB))

image_seq_to_video("steph_fortnite23", "steph_fortnite23_dance.mp4")
