import cv2

class HistogramBuilder:

	def create_histogram(self, image_filenames, bucket_size):
		images = []
		for image_filename in image_filenames:
			image = cv2.imread(image_filename)
			images.append(image)
		hist = cv2.calcHist(images, [0, 1, 2], None, [256/bucket_size, 256/bucket_size, 256/bucket_size], [0, 256, 0, 256, 0, 256])
		return hist

