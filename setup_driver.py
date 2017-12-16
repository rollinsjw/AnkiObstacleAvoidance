import numpy as np

from camera_calibration import calibrate
from config import Config
from histogram_builder import HistogramBuilder

def main():

	config = Config()
	
	# Calibrate camera
	calibrate(config)
	
	# Create and save histogram for obstacles
	obstacle_image_names = ['obstacles_without_background.jpg']
	hist_builder = HistogramBuilder()
	hist = hist_builder.create_histogram(obstacle_image_names, config.get_obstacle_hist_bucket_size())

	f = open("hist_text", "w")
	f.write(hist)

	np.savez(config.get_obstacle_hist_filename(), obstacle_histogram=hist)


if __name__ == "__main__":
	main()