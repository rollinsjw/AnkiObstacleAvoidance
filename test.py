import cv2

def test():
	image = cv2.imread("pattern.png")
	hist = cv2.calcHist([image], [0, 1, 2], None, [32, 32, 32], [0, 256])
	print hist


if __name__ == "__main__":
	test()