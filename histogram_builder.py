import cv2

class HistogramBuilder:

	def create_histogram(image_filename):
		image = cv2.imread(image_filename)
		hist = cv2.calcHist([image], [0, 1, 2], None, [32, 32, 32], [0, 256])
		return hist

