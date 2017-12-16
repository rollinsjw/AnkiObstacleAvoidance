import cv2
import numpy as np
import copy

import Image

from rectangle import Rectangle

class ObjectTracker:

	def __init__(self, config):
		obstacle_npz_file = np.load(config.get_obstacle_hist_filename() + ".npz")
		self.obstacle_histogram = obstacle_npz_file['obstacle_histogram']
		self.hist_bucket_size = config.get_obstacle_hist_bucket_size()
		
	def detect_cars(self, frame):
		gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		thresh_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)[1]

	
	def detect_obstacles(self, frame):

		"""
		:returns: list of lists where each sublist contains pixel coordinates of corners of min rectangle surrounding an obstacle
		"""
		
		rows, cols, channels = frame.shape
		
		image = copy.deepcopy(frame)

		for i in range(rows):
			threshold_row = []
			for j in range(cols):
				pixel = frame[i][j]  # pixel = [blue, green, red]
				blue = pixel[0]
				green = pixel[1]
				red = pixel[2]

				if (self.obstacle_histogram[blue/self.hist_bucket_size][green/self.hist_bucket_size][red/self.hist_bucket_size] >= 2.5):
					frame[i][j] = [255, 255, 255]
				else:
					frame[i][j] = [0, 0, 0]

		gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		cv2.imwrite('thresh_obstacles2.jpg', gray_image)

		contours, hierarchy = cv2.findContours(gray_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		object_rectangles = []
		
		for i in range(len(contours)):	
			x,y,w,h = cv2.boundingRect(contours[i])
			if w>10 and h>10:
				print "hello"
				cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
				rect = Rectangle()
				rect.top_left = (x, y)
				rect.top_right = (x+w, y)
				rect.bottom_left = (x, y+h)
				rect.bottom_right = (x+w, y+h)
				object_rectangles.append(rect)

		cv2.imwrite('obstacles_found2.jpg', image)

		cv2.imshow('image', image)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
				

		# return object_rectangles
	





