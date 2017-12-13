import cv2
import numpy as np

def test():
	#image = cv2.imread("red.png")
	# blue_hist = cv2.calcHist([image], [0], None, [32], [0, 256])
	# green_hist = cv2.calcHist([image], [1], None, [32], [0, 256])
	# red_hist = cv2.calcHist([image], [2], None, [32], [0, 256])
	# hist = cv2.calcHist([image], [0, 1, 2], None, [64, 64, 64], [0, 256, 0, 256, 0, 256])
	# print hist
	# print len(hist)
	# print hist[0]
	# print len(hist)
	# print hist[0][0]
	# print len(hist[0][0])
	# print blue_hist
	# print green_hist
	# print red_hist

	threshold_image = np.zeros((300,300,3),np.uint8)
	print threshold_image




if __name__ == "__main__":
	test()