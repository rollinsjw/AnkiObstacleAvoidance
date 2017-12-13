import numpy as np
import cv2
import time

def stream():

	vid = cv2.VideoCapture(0)

	# Check that capture was initialized
	if not vid.isOpened():
		vid.open()

	counter = 0

	while True:
		return_value, frame = vid.read()
		print("read frame")
		time.sleep(5)

		if counter > 7:
			break
		counter+=1

	vid.release()

if __name__ == "__main__":
	stream()
