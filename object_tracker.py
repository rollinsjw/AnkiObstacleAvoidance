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
		:returns: list of lists where each sublist contains pixel coordinates of corners of min rectangle surrounding an obstacle
		"""
		
		rows, cols, channels = frame.shape
		threshold_image_pixels = []

		for i in range(rows):
			threshold_row = []
			for j in range(cols):
				pixel = frame[i][j]  # pixel = [blue, green, red]
				blue = pixel[0]
				green = pixel[1]
				red = pixel[2]

				if (self.obstacle_histogram[blue/self.hist_bucket_size][green/self.hist_bucket_size][red/self.hist_bucket_size] >= ): #TODO
					threshold_row.append([255, 255, 255])
				else:
					threshold_row.append([0, 0, 0])
			threshold_image_pixels.append(threshold_row)

		dt = np.dtype('f8')
		threshold_image = np.array(threshold_image_pixels, dtype=dt)

		image = cv2.cvtColor(threshold_image, cv2.COLOR_BGR2GRAY)

		contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		max_rectangle = (0, 0, 0 , 0)
		for i in range(len(contours)):	
			x,y,w,h = cv2.boundingRect(contours[i])
			if w*h > max_rectangle[2]*max_rectangle[3]:
				max_rectangle = (x, y, w, h)

		#x,y,w,h = max_rectangle
		
		#cv2.rectangle(original_image,(x,y),(x+w,y+h),(0,0,255),2)

		return max_rectangle
	





