import cv2
import numpy as np

from config import Config
from object_tracker import ObjectTracker

def test():

	config = Config()
	ot = ObjectTracker(config)

	im = cv2.imread('obstacles.jpg')

	ot.detect_obstacles(im)



if __name__ == "__main__":
	test()
