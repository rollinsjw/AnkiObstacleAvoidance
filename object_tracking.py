# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
import cv2
import numpy as np

def detect_cars(frame):
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png", gray_image)
    cv2.namedWindow("gray", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("gray", 400, 300)
    cv2.imshow("gray", gray_image)
    thresh_image = cv2.threshold(gray_image, 196, 255, cv2.THRESH_BINARY)[1]
    cv2.imwrite("thresh.png", thresh_image)
    cv2.namedWindow("thresh", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("thresh", 400, 300)
    cv2.imshow("thresh", thresh_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.resizeWindow("output", 400, 300)
image = cv2.imread("dark.JPG")
cv2.imshow("output", image)

cv2.waitKey(0)
detect_cars(image)
