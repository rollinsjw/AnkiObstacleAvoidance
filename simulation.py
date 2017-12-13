import numpy as np
import cv2
import time

from config import Config
from object_tracking import ObjectTracking
from undistortion import Undistortion

class Simulation:

	def __init__():
		config = Config()
		self.undistortion = Undistortion(config)
		self.object_tracking = ObjectTracking()

	def stream():
		vid = cv2.VideoCapture(0)

		# Check that capture was initialized
		if (!vid.isOpened()):
			vid.open()

		#TODO: add way to save video

		while True:
			return_value, frame = vid.read()

			if not return_value:
				break

			# Undistort image
			undistorted_frame = self.undistortion.undistort(frame)

			#TODO: call detect cars and detect obstacles from object tracking
			#TODO: use control to change state
			#TODO: send anki commands
			#TODO: convert to ego centric coordinates
			#TODO: instantiate ControlSystem instance
			#TODO: iterate through cars calling ControlSystem.generateTree for each car

		vid.release()
