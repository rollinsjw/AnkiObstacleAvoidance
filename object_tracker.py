import cv2
import numpy as np

import Image

class ObjectTracker:

	def __init__(config):
		obstacle_npz_file = np.load(config.get_obstacle_hist_filename() + ".npz")
		self.obstacle_histogram = obstacle_npz_file['obstacle_histogram']
		self.hist_bucket_size = config.get_obstacle_hist_bucket_size()
		
	def detect_cars(frame):
		gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		thresh_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)[1]

	
	def detect_obstacles(frame):

		"""
		:returns: list of list where each sublist contains pixel coordinates of corners of min rectangles surrounding an obstacle
		"""
		
		rows, cols, channels = frame.shape
		threshold_grid = []

		for i in range(rows):
			threshold_row = []
			for j in range(cols):
				pixel = frame[i][j]  # pixel = [blue, green, red]
				blue = pixel[0]
				green = pixel[1]
				red = pixel[2]
				pixel_frequency = self.obstacle_histogram[blue/self.hist_bucket_size][green/self.hist_bucket_size][red/self.hist_bucket_size]
				if (pixel_frequency >= threshold):
					threshold_row.append(1)
				else:
					threshold_row.append(0)
			threshold_grid.append(threshold_row)





