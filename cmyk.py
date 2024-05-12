import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_to_cmy(image):
    return 255 - image

def rgb_to_cmyk(image):
    cmy = rgb_to_cmy(image)
    cmyk = np.zeros_like(image, dtype=np.float32)
    cmyk[:, :, 0] = cmy[:, :, 0] / 255.0  # C
    cmyk[:, :, 1] = cmy[:, :, 1] / 255.0  # M
    cmyk[:, :, 2] = cmy[:, :, 2] / 255.0  # Y
    min_cmy = np.min(cmyk, axis=2)
    cmyk = np.stack((cmyk[:,:,0], cmyk[:,:,1], cmyk[:,:,2], min_cmy), axis=2)
    return cmyk * 100

image_path = 'Tugas 7\dw.jpg'

image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image_cmyk = rgb_to_cmyk(image)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original RGB')

plt.subplot(1, 2, 2)
plt.imshow(image_cmyk)
plt.title('CMYK')

plt.show()
