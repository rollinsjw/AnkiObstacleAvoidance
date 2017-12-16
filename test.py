import cv2
import numpy as np

from object_tracker import ObjectTracker

def test():

	ot = ObjectTracker()

	im = cv2.imread('obstacles.jpg')

	ot.detect_obstacles(im)



if __name__ == "__main__":
	test()
