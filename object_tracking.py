# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
import cv2
import numpy as np

class ObjectTracking:

	def detect_cars(frame):
		gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		thresh_image = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)[1]

	def detect_obstacles(frame):
		pass

