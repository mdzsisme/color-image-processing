import cv2
import numpy as np
import matplotlib.pyplot as plt


def rgb_to_yuv(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2YUV)

image_path = 'Tugas 7\dw.jpg'

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_yuv = rgb_to_yuv(image)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original RGB')

plt.subplot(1, 2, 2)
plt.imshow(image_yuv)
plt.title('YUV')

plt.show()
