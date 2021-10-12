import cv2 as cv
import numpy as np
import argparse
from matplotlib import pyplot as plt


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Takes in file name.")

	parser.add_argument('-f', '--file', required=True, help="Path to image file.")
	parser.add_argument('-p', '--parameters', nargs=2, help="Specifications for edge detection analysis", type=int, default=(100,200))

	args = parser.parse_args()
	p1, p2 = args.parameters

	img = cv.imread(args.file, 0)
	edges = cv.Canny(img,p1,p2)

	plt.subplot(121)
	plt.imshow(img,cmap = 'gray')
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122)
	plt.imshow(edges,cmap = 'gray')
	plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
	plt.show()
