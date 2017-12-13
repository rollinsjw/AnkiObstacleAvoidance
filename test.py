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

	frame = cv2.imread("New_Picture.png")
	rows, cols, channels = frame.shape
	threshold_image_pixels = []

	for i in range(rows):
		threshold_row = []
		for j in range(cols):
			pixel = frame[i][j]  # pixel = [blue, green, red]
			blue = pixel[0]
			green = pixel[1]
			red = pixel[2]
			
			if (green >= 30):
				threshold_row.append([255, 255, 255])
			else:
				threshold_row.append([0, 0, 0])
		threshold_image_pixels.append(threshold_row)

	dt = np.dtype('f8')
	threshold_image = np.array(threshold_image_pixels, dtype=dt)

	cv2.imshow('image', threshold_image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()




if __name__ == "__main__":
	test()
