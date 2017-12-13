import ConfigParser

class Config:

	def __init__():
		self.config = ConfigParser.ConfigParser()
		self.config.read('properties.ini')

	def get_calibration_filename():
		return self.config.get('file_names', 'calibration_file')

	def get_obstacle_hist_filename():
		return self.config.get('file_names', 'obstacle_histogram_file')