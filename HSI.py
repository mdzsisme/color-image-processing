import cv2
import numpy as np
import matplotlib.pyplot as plt


def rgb_to_hsi(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

image_path = 'Tugas 7\dw.jpg'

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_hsi = rgb_to_hsi(image)

plt.figure(figsize=(7, 7))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original RGB')

plt.subplot(1, 2, 2)
plt.imshow(image_hsi)
plt.title('HSI')

plt.show()
