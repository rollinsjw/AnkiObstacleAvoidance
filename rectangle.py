
class Rectangle:

	def __init__(self):
		self.top_left = (0, 0)
		self.top_right = (0, 0)
		self.bottom_left = (0, 0)
		self.bottom_right = (0, 0)

	@property
	def top_left(self):
		return self.__top_left

	@top_left.setter
	def top_left(self, top_left):
		self.__top_left = top_left


	@property
	def top_right(self):
		return self.__top_right

	@top_right.setter
	def top_right(self, top_right):
		self.__top_right = top_right

	@property
	def bottom_left(self):
		return self.__bottom_left

	@bottom_left.setter
	def bottom_left(self, bottom_left):
		self.__bottom_left = bottom_left

	@property
	def bottom_right(self):
		return self.__bottom_right

	@bottom_right.setter
	def bottom_right(self, bottom_right):
		self.__bottom_right = bottom_right
