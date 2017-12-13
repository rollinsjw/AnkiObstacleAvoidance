import cv2

def test():
	image = cv2.imread("pattern.png")
	blue_hist = cv2.calcHist([image], [0], None, [32], [0, 256])
	green_hist = cv2.calcHist([image], [1], None, [32], [0, 256])
	red_hist = cv2.calcHist([image], [2], None, [32], [0, 256])
	#hist = cv2.calcHist([image], [0, 1, 2], None, [32, 32, 32], [0, 256])
	print blue_hist
	print green_hist
	print red_hist


if __name__ == "__main__":
	test()