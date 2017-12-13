import cv2

class HistogramBuilder:

	def create_histogram(image_filename, bucket_size):
		image = cv2.imread(image_filename)
		hist = cv2.calcHist([image], [0, 1, 2], None, [256/bucket_size, 256/bucket_size, 256/bucket_size], [0, 256, 0, 256, 0, 256])
		return hist

