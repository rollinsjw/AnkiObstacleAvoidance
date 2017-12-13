import ConfigParser

class Config:

	def __init__():
		self.config = ConfigParser.ConfigParser()
		self.config.read('properties.ini')

	def get_calibration_filename():
		return self.config.get('calibration', 'file_name')

	def get_obstacle_hist_filename():
		return self.config.get('obstacle_histogram', 'file_name')

	def get_obstacle_hist_bucket_size():
		return int(self.config.get('obstacle_histogram', 'bucket_size'))