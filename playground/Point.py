import math
class Point:
	"""Class for creating points on a plane"""

# Constructors
	def __init__(self, x, y):
		"""
		Constructor for the Point class
		x : x-coordinate
		y : y-coordinate
		"""
		self.convertCartesianCoordinatesToPolar(x, y)

# Getters
	def getX(self):
		"""
		Getter for the x-coordinate of the point
		"""
		return round(self.rho * math.cos(self.theta), 2)

	def getY(self):
		"""
		Getter for the y-coordinate of the point
		"""
		return round(self.rho * math.sin(self.theta), 2)

# Setters
	def setX(self, x):
		"""
		Setter for the x-coordinate
		"""
		self.convertCartesianCoordinatesToPolar(x, self.getY())

	def setY(self, y):
		"""
		Setter for the y-coordinate
		"""
		self.convertCartesianCoordinatesToPolar(self.getX(), y)

# Helper functions
	def convertCartesianCoordinatesToPolar(self, x, y):
		"""
		Helper function to convert the cartesian coordinates passed in to polar coordinates
		"""
		self.rho = math.sqrt(x**2 + y**2)
		if x != 0:
			self.theta = math.atan(y/x)
		else:
			self.theta = math.pi/2.0

# Some testing
if __name__ == '__main__':
	
	# Test constructor does the right math to store the values of the coordinates
	coordinates = [ (1.2, 1.2), (-1.1, 1.1), (-2.9, -32.0), (7.0, -3.0), (0.0,0.0), (0.0, 4.0), (9.0, 0.0) ]
	print(coordinates)
	success = True
	for coordinate in coordinates:
		point = Point(coordinate[0], coordinate[1])
		try:
			assert((point.getX() == coordinate[0]) and (point.getY() == coordinate[1]) )
		except AssertionError:
			print("point has coordinates: (%s, %s), should have been (%s, %s)" %(point.getX(), point.getY(), coordinate[0], coordinate[1]))
			success = False
			break
	if success:
		print("Constructor test passed!")
	else :
		print("Constructor test failed!")
	
	print("Constructor test finished")
