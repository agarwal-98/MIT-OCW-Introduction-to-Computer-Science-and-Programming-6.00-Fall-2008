# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:

SUBJECT_FILENAME = "shapes.txt"
from string import *

class Shape(object):
	def area(self):
		raise AttributeException("Subclasses should override this method.")

class Square(Shape):
	def __init__(self, h):
		"""
		h: length of side of the square
		"""
		self.side = float(h)
	def area(self):
		"""
		Returns area of the square
		"""
		return self.side**2
	def __str__(self):
		return 'Square with side ' + str(self.side)
	def __eq__(self, other):
		"""
		Two squares are equal if they have the same dimension.
		other: object to check for equality
		"""
		return type(other) == Square and self.side == other.side

# square1 = Square(5)  
# print (square1)   
# print (square1.area())


class Circle(Shape):
	def __init__(self, radius):
		"""
		radius: radius of the circle
		"""
		self.radius = float(radius)
	def area(self):
		"""
		Returns approximate area of the circle
		"""
		return 3.14159*(self.radius**2)
	def __str__(self):
		return 'Circle with radius ' + str(self.radius)
	def __eq__(self, other):
		"""
		Two circles are equal if they have the same radius.
		other: object to check for equality
		"""
		return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.

class Triangle(Shape):
	def __init__(self, b, h):
		# b: base of the triangle
		# h: height of the triangle
		self.base = float(b)
		self.height = float(h)

	def area(self):
		# area is computed as: 1/2*b*h

		return 0.5*(self.base*self.height)

	def __str__(self):
		# print statemet
		return "Triangle with base " + str(self.base) + " and height " + str(self.height)

	def __eq__(self, other):
		# testing for equality
		return type(other) == Triangle and self.base == other.base and self.height == other.height

# triangle1 = Triangle(5,3)  
# print (triangle1)   
# print (triangle1.area())


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
	def __init__(self):
		"""
		Initialize any needed variables
		"""
		self.set = []
		self.place = None
	def addShape(self, sh):
		"""
		Add shape sh to the set; no two shapes in the set may be
		identical
		sh: shape to be added
		"""
		if sh in self.set:
			raise ValueError('duplicate shape')
		else:
			self.set.append(sh)

	def __iter__(self):
		"""
		Return an iterator that allows you to iterate over the set of
		shapes, one shape at a time
		"""
		# quickest way
		for shape in self.set:
			yield shape


	def __str__(self):
		"""
		Return the string representation for a set, which consists of
		the string representation of each shape, categorized by type
		(circles, then squares, then triangles)
		"""
		s = ""
		for shapes in self.set:
			s = s + str(shapes) + "\n" 	
		return s

ss = ShapeSet()
ss.addShape(Triangle(3,8))
ss.addShape(Circle(1))
ss.addShape(Square(3.6))
ss.addShape(Triangle(4,6))
ss.addShape(Circle(2.2))

# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
	"""
	Returns a tuple containing the elements of ShapeSet with the
	   largest area.
	shapes: ShapeSet
	"""
	# initializing largest area
	largestarea = 0
	# creating a list which will hold the largest area
	largestarea_list = [largestarea]
	for shape in shapes:
		# if the area of shape is greater than the last largest
		# area recorded, remove the last one recorded from the 
		# list and add this shape to the list instead
		if shape.area() > largestarea:
			largestarea = shape.area()
			largestarea_list.pop()
			largestarea_list.append(shape)
		# if area of shape same as the last largest area recorded,
		# add it to the list
		elif shape.area() == largestarea:
			largestarea_list.append(shape)

	return tuple(largestarea_list)


# largest = findLargest(ss)
# for largestarea in largest: print (largestarea)


#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
	"""
	Retrieves shape information from the given file.
	Creates and returns a ShapeSet with the shapes found.
	filename: string
	"""
	## TO DO
	inputFile = open(filename)
	# creating object of class ShapeSet
	adding_shapes = ShapeSet()
	for line in inputFile:
		# splittng the line by using comma as the delimiter and
		# automatically stores in the form of a list
		line = line.strip().split(',')
		if line[0] == 'circle':
			adding_shapes.addShape(Circle(line[1]))
		if line[0] == 'square':
			adding_shapes.addShape(Square(line[1]))

		if line[0] == 'triangle':
			adding_shapes.addShape(Triangle(line[1],line[2]))

	return adding_shapes
		

# readshapes = readShapesFromFile(SUBJECT_FILENAME)
# print (readshapes)