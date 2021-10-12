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

	filtered = cv.bilateralFilter(img, 7, 50, 50)
	filtered_edges = cv.Canny(filtered, p1, p2)

	edges = cv.Canny(img,p1,p2)

	plt.subplot(141)
	plt.imshow(img,cmap = 'gray')
	plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(142)
	plt.imshow(edges,cmap = 'gray')
	plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(143)
	plt.imshow(filtered,cmap = 'gray')
	plt.title('Filtered Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(144)
	plt.imshow(filtered_edges,cmap = 'gray')
	plt.title('Filtered Edge Image'), plt.xticks([]), plt.yticks([])
	plt.show()
