import cv2
from config import Config
import numpy as np

from histogram_building

class FrameProcessor:

	def __init__(config):


		# Load camera matrix and distortion coefficients from camera calibration
		self.calibration_npz_file = np.load(config.get_calibration_filename() + ".npz")
		self.camera_matrix = calibration_npz_file['camera_matrix']
		self.distortion_coefficients = calibration_npz_file['distortion_coefficients']

	def undistort(image)
		undistorted_image = cv2.undistort(image, self.camera_matrix, self.distortion_coefficients, None, )
		return undistorted_image
