import cv2 as cv
import numpy as np
import argparse
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser(description="Takes in file name.")

parser.add_argument('-f', '--file', required=True, help="Path to image file.")

args = parser.parse_args()

img = cv.imread(args.file, 0)
edges = cv.Canny(img,100,200)

plt.subplot(121)
plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
