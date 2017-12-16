import cv2
import numpy as np

from config import Config
from object_tracker import ObjectTracker
from frame_processor import FrameProcessor

def test():



	config = Config()

	im = cv2.imread('obstacles2.jpg')

	fp = FrameProcessor(config)
	undistorted_image = fp.undistort(im)

	cv2.imwrite('undistorted_image2.jpg', undistorted_image)

	ot = ObjectTracker(config)

	ot.detect_obstacles(undistorted_image)



if __name__ == "__main__":
	test()
