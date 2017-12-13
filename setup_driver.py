import numpy as np

from camera_calibration import calibrate
from config import Config
from histogram import HistogramBuilder

def main():
	
	# Calibrate camera
	calibrate()

	# Create and save histogram for obstacles
	obstacle_image_name = ''
	hist_builder = HistogramBuilder()
	hist = hist_builder.create_historgram(obstacle_image_name)
	config = Config()
	np.savez(config.get_obstacle_hist_filename(), obstacle_histogram=hist)


if __name__ == "__main__":
	main()