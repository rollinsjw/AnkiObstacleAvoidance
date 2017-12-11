import ConfigParser

class Config:

	def __init__():
		self.config = ConfigParser.ConfigParser()
		self.config.read('properties.ini')

	def get_calibration_filename():
		return self.config.get('file_names', 'calibration_file')