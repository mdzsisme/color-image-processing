import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_to_ycbcr(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2YCrCb)

image_path = 'Tugas 7\dw.jpg'

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_ycbcr = rgb_to_ycbcr(image)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original RGB')

plt.subplot(1, 2, 2)
plt.imshow(image_ycbcr)
plt.title('YCbCr')

plt.show()
