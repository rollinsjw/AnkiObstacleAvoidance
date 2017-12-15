import cv2
import glob
import numpy as np
import config


'''
The purpose of this module is to:
  1. Create the camera matrix:
    | f_x  0  c_x |
    |  0  f_y c_y |
    |  0   0   1  |

    where:
      (f_x, f_y) = focal length
      (c_x, c_y) = optical center  
  2. Find the distortion coefficients: (k_1, k_2, p_1, p_2, k_3)

'''

SQUARE_SIZE = .0245 #meters
BOARD_HEIGHT = 9 #number of corners
BOARD_WIDTH = 6 #number of corners


# Corner refinement termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def __create_known_chessboard():

    chessboard_size = (BOARD_HEIGHT, BOARD_WIDTH)

    # Creates array of height*width arrays of size 3. Initializes all values to 0
    unit_corners = np.zeros((np.prod(chessboard_size), 3), np.float32) 
    
    # Creates array of height*width arrays of size 3. Values give relative locations of corners on grid
    unit_corners[:, :2] = np.indices(chessboard_size).T.reshape(-1, 2)
    corners = unit_corners * SQUARE_SIZE

    return corners


def calibrate():

    object_points = []
    image_points = []

    images = glob.glob('calibration_images/*.jpg') # List of all filenames ending in .jpg in current directory

    known_corners = __create_known_chessboard()

    for filename in images:
        image = cv2.imread(filename)  # Load image
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # Covert image to grayscale

        # Find the chess board corners
        is_chessboard_found, corners = cv2.findChessboardCorners(gray_image, (BOARD_HEIGHT, BOARD_WIDTH), None)

        if is_chessboard_found:
            
            object_points.append(known_corners)

            refined_corners = cv2.cornerSubPix(gray_image, corners, (11,11), (-1,-1), criteria)
            image_points.append(refined_corners)

            pattern_image = cv2.drawChessboardCorners(image, (BOARD_HEIGHT, BOARD_WIDTH), refined_corners, is_chessboard_found)

            cv2.imwrite('pattern'+filename, pattern_image)

        else:
            print "ERROR: did not find chessboard in file " + filename

    # Get camera matrix and distortion coefficients
    return_bool, camera_matrix, distortion_coefficients, rotation_vectors, translation_vectors = cv2.calibrateCamera(object_points, image_points, gray_image.shape[::-1],None,None)

    # Write callibration info to npz file
    np.savez(config.get_calibration_filename(), camera_matrix=camera_matrix, distortion_coefficients=distortion_coefficients)

if __name__ == "__main__":
    calibrate()


