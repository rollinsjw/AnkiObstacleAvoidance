from matplotlib import pyplot as plt
import numpy as np
import cv2

def create_histogram(image_filename):
	image = cv2.imread(image_filename)
	hist = cv2.calcHist([image], [0, 1, 2], None, [32, 32, 32], [0, 256])


if __name__ == "__main__":
	image_filename = ""
	create_histogram(image_filename)