import cv2
import numpy as np

import Image

class ObjectTracking:

	def __init__(config):
		obstacle_npz_file = np.load(config.get_obstacle_hist_filename() + ".npz")
		self.obstacle_histogram = obstacle_npz_file['obstacle_histogram']
		
	def detect_cars(frame):
		gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		thresh_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)[1]

	def detect_obstacles(frame):
		
		rows, cols, channels = frame.shape

		for i in range(rows):
			for j in range(cols):
				pixel = frame[i][j]


		pixels = [ filter(p) for p in image.getdata() ]
	    nim = Image.new("RGB",image.size)
	    nim.putdata(pixels)
	    return nim
