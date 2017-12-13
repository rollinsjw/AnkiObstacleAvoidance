import cv2
import numpy as np

def test():
	
	image = cv2.imread('white_circle.jpg')

	im2, contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	print contours

	contour = contours[0]

	rect = cv2.minAreaRect(contour)
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	cv2.drawContours(image,[box],0,(0,0,255),2)


	cv2.imshow('image', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()




if __name__ == "__main__":
	test()