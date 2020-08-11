# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:
import ps11_visualize
import math
import random
import pylab

# === Provided classes

class Position(object):
	"""
	A Position represents a location in a two-dimensional room.
	"""
	def __init__(self, x, y):
		"""
		Initializes a position with coordinates (x, y).

		x: a real number indicating the x-coordinate
		y: a real number indicating the y-coordinate
		"""
		self.x = x
		self.y = y
	def getX(self):
		return self.x
	def getY(self):
		return self.y
	def getNewPosition(self, angle, speed):
		"""
		Computes and returns the new Position after a single clock-tick has
		passed, with this object as the current position, and with the
		specified angle and speed.

		Does NOT test whether the returned position fits inside the room.

		angle: integer representing angle in degrees, 0 <= angle < 360
		speed: positive float representing speed

		Returns: a Position object representing the new position.
		"""
		old_x, old_y = self.getX(), self.getY()
		# Compute the change in position
		delta_y = speed * math.cos(math.radians(angle))
		delta_x = speed * math.sin(math.radians(angle))
		# creating a new position
		new_x = old_x + delta_x
		new_y = old_y + delta_y
		return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
	"""
	A RectangularRoom represents a rectangular region containing clean or dirty
	tiles.

	A room has a width and a height and contains (width * height) tiles. At any
	particular time, each of these tiles is either clean or dirty.
	"""
	def __init__(self, width, height):
		"""
		Initializes a rectangular room with the specified width and height.
		Initially, no tiles in the room have been cleaned.

		width: an integer > 0
		height: an integer > 0
		"""
		# TODO: Your code goes here

		self.width = width
		self.height = height
		self.totaltiles = width*height
		self.cleaned = []

	def cleanTileAtPosition(self, pos):
		"""
		Mark the tile under the position POS as cleaned.
		Assumes that POS represents a valid position inside this room.

		pos: a Position
		"""
		# TODO: Your code goes here
		self.cleaned.append((int(pos.getX()), int(pos.getY())))

	def isTileCleaned(self, m, n):
		"""
		Return True if the tile (m, n) has been cleaned.

		Assumes that (m, n) represents a valid tile inside the room.

		m: an integer
		n: an integer
		returns: True if (m, n) is cleaned, False otherwise
		"""
		# TODO: Your code goes here
		if (int(m), int(n)) in self.cleaned: 
			return True
		return False

	def getNumTiles(self):
		"""
		Return the total number of tiles in the room.

		returns: an integer
		"""
		# TODO: Your code goes here
		return self.totaltiles 


	def getNumCleanedTiles(self):
		"""
		Return the total number of clean tiles in the room.

		returns: an integer
		"""
		# TODO: Your code goes here
		return len(self.cleaned)

	def getRandomPosition(self):
		"""
		Return a random position inside the room.

		returns: a Position object.
		"""
		# TODO: Your code goes here
		x_possibilities = round(random.uniform(0,self.width+1), 1)
		y_possibilities = round(random.uniform(0,self.height+1), 1)
		return Position(x_possibilities,y_possibilities)

	def isPositionInRoom(self, pos):
		"""
		Return True if POS is inside the room.

		pos: a Position object.
		returns: True if POS is in the room, False otherwise.
		"""
		# TODO: Your code goes here

		if 0 <= pos.getX() <= self.width and 0 <= pos.getY() <= self.height: 
			return True
		else:
			return False

class BaseRobot(object):
	"""
	Represents a robot cleaning a particular room.

	At all times the robot has a particular position and direction in
	the room.  The robot also has a fixed speed.

	Subclasses of BaseRobot should provide movement strategies by
	implementing updatePositionAndClean(), which simulates a single
	time-step.
	"""
	def __init__(self, room, speed):
		"""
		Initializes a Robot with the given speed in the specified
		room. The robot initially has a random direction d and a
		random position p in the room.

		The direction d is an integer satisfying 0 <= d < 360; it
		specifies an angle in degrees.

		p is a Position object giving the robot's position.

		room:  a RectangularRoom object.
		speed: a float (speed > 0)
		"""
		# TODO: Your code goes here
		self.speed = speed
		self.room = room
		self.p = room.getRandomPosition()
		self.d = random.randrange(0,360)




	def getRobotPosition(self):
		"""
		Return the position of the robot.


		returns: a Position object giving the robot's position.
		"""
		# TODO: Your code goes here

		return self.p
	def getRobotDirection(self):
		"""
		Return the direction of the robot.

		returns: an integer d giving the direction of the robot as an angle in
		degrees, 0 <= d < 360.
		"""
		# TODO: Your code goes here

		return self.d
	def setRobotPosition(self, position):
		"""
		Set the position of the robot to POSITION.

		position: a Position object.
		"""
		# TODO: Your code goes here
		self.p = position

	def setRobotDirection(self, direction):
		"""
		Set the direction of the robot to DIRECTION.

		direction: integer representing an angle in degrees
		"""
		# TODO: Your code goes here

		self.d = direction
class Robot(BaseRobot):
	"""
	A Robot is a BaseRobot with the standard movement strategy.

	At each time-step, a Robot attempts to move in its current
	direction; when it hits a wall, it chooses a new direction
	randomly.
	"""
	def updatePositionAndClean(self):
		"""
		Simulate the passage of a single time-step.

		Move the robot to a new position and mark the tile it is on as having
		been cleaned.
		"""
		# TODO: Your code goes here
		notatwall = True

		while notatwall:
			initial_position = self.getRobotPosition()
			updated_position = initial_position.getNewPosition(self.getRobotDirection(), self.speed)
			if self.room.isPositionInRoom(updated_position):
				self.p = updated_position
				if not self.room.isTileCleaned(updated_position.getX(), updated_position.getY()):
					self.room.cleanTileAtPosition(updated_position)
					# the function returns if the new robot position is within the room and this position
					# has not already been cleaned.
					notatwall = False 
			else:
				# returns a new random position if position not in room
				self.d = random.randrange(0,360)



# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
				  robot_type, visualize):
	"""
	Runs NUM_TRIALS trials of the simulation and returns a list of
	lists, one per trial. The list for a trial has an element for each
	timestep of that trial, the value of which is the percentage of
	the room that is clean after that timestep. Each trial stops when
	MIN_COVERAGE of the room is clean.

	The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
	each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

	Visualization is turned on when boolean VISUALIZE is set to True.

	num_robots: an int (num_robots > 0)
	speed: a float (speed > 0)
	width: an int (width > 0)
	height: an int (height > 0)
	min_coverage: a float (0 <= min_coverage <= 1.0)
	num_trials: an int (num_trials > 0)
	robot_type: class of robot to be instantiated (e.g. Robot or
				RandomWalkRobot)
	visualize: a boolean (True to turn on visualization)
	"""
	# TODO: Your code goes here


	foralltrials = []
	for trials in range(num_trials):
		if visualize:
			anim = ps11_visualize.RobotVisualization(num_robots, width, height) 
		room = RectangularRoom(width,height)

		robotlist = []
		for each in range(num_robots):
			robotlist.append(robot_type(room,speed))   

		percentagecleanedsofar = []
		percent_cleaned = 0.0
		while percent_cleaned < min_coverage:
			for each in robotlist:
				each.updatePositionAndClean()
			if visualize:
				anim.update(room,robotlist)
			percent_cleaned = room.getNumCleanedTiles()/room.getNumTiles()
			percentagecleanedsofar.append(percent_cleaned)
		if visualize:
			anim.done()
		foralltrials.append(percentagecleanedsofar)
	return foralltrials

robot_type = Robot
# avg = runSimulation(2, 1.0, 20, 20, 1.0, 1, robot_type, True) 




# === Provided function
def computeMeans(list_of_lists):
	"""
	Returns a list as long as the longest list in LIST_OF_LISTS, where
	the value at index i is the average of the values at index i in
	all of LIST_OF_LISTS' lists.

	Lists shorter than the longest list are padded with their final
	value to be the same length.
	"""
	# Find length of longest list
	longest = 0
	for lst in list_of_lists:
		if len(lst) > longest:
		   longest = len(lst)
	# Get totals
	tots = [0]*(longest)
	for lst in list_of_lists:
		for i in range(longest):
			if i < len(lst):
				tots[i] += lst[i]
			else:
				tots[i] += lst[-1]
	# Convert tots to an array to make averaging across each index easier
	tots = pylab.array(tots)
	# Compute means
	means = tots/float(len(list_of_lists))
	return means


# A helper function created to return the average length of lists within a list. This 
# will be used for plots 1-5. 
def AverageListLength(simulation):
	listoflists = simulation
	sizoflists = 0
	numberoflists = 0
	for each in listoflists:
		numberoflists += 1
		sizoflists = sizoflists + len(each)
	return (sizoflists/numberoflists)		




# === Problem 4
def showPlot1():
	"""
	Produces a plot showing dependence of cleaning time on room size.
	"""
	# TODO: Your code goes here

	min_coverage = 0.75
	room_size = [[5,5], [10,10], [15,15], [20,20], [25,25]]
	room_area = []
	for mesaurements in room_size:
		room_area.append(mesaurements[0]*mesaurements[1])
	num_trials = 30
	num_robots = 1
	speed = 1.0
	robot_type = Robot
	visualize = False 
	meantime = []
	for lists in room_size:
		width = lists[0]
		height = lists[1]
		avg = runSimulation(num_robots, speed,width,height, min_coverage, num_trials, robot_type, visualize)
		# print(avg)
		avglength = AverageListLength(avg)
		meantime.append(avglength)
		print(avglength)

	pylab.figure()
	pylab.plot(room_area,meantime)
	pylab.ylabel( 'mean time' )
	pylab.xlabel( 'room area' )
	pylab.title( 'average time taken to clean 75% of different room areas by a single robot' )
	pylab.show()

# showPlot1()	



def showPlot2():
	"""
	Produces a plot showing dependence of cleaning time on number of robots.
	"""
	# TODO: Your code goes here

	min_coverage = 0.75
	width = 25
	height = 25
	num_trials = 10
	num_robots = [1,2,3,4,5,6,7,8,9,10]
	speed = 1.0
	robot_type = Robot
	visualize = False 
	meantime = []
	for numrobots in num_robots:
		avg = runSimulation(numrobots, speed,width,height, min_coverage, num_trials, robot_type, visualize)
		# print(avg)
		avglength = AverageListLength(avg)
		meantime.append(avglength)

	pylab.figure()
	pylab.plot(num_robots, meantime, marker='o', color='r')
	pylab.ylabel( 'mean time' )
	pylab.xlabel( 'number of robots' )
	pylab.title( 'average time taken to clean 75% of a 25x25 room with 1-10 robots' )
	pylab.show()

# showPlot2()

def showPlot3():
	"""
	Produces a plot showing dependence of cleaning time on room shape.
	"""
	# TODO: Your code goes here

	min_coverage = 0.75
	room_size = [[20,20], [25,16], [40,10], [50,8], [80,5], [100,4]]
	ratio = []
	for mesaurements in room_size:
		ratio.append(mesaurements[0]/mesaurements[1])
	num_trials = 10
	num_robots = 2
	speed = 1.0
	robot_type = Robot
	visualize = True 
	meantime = []
	for lists in room_size:
		width = lists[0]
		height = lists[1]
		avg = runSimulation(num_robots, speed,width,height, min_coverage, num_trials, robot_type, visualize)
		# print(avg)
		avglength = AverageListLength(avg)
		meantime.append(avglength)

	pylab.figure()
	pylab.plot(ratio,meantime)
	pylab.ylabel( 'mean time' )
	pylab.xlabel( 'width to height ratio' )
	pylab.title( 'average time taken to clean 75% of differening room dimensions by 2 robots' )
	pylab.show()

# showPlot3()

def showPlot4():
	"""
	Produces a plot showing cleaning time vs. percentage cleaned, for
	each of 1-5 robots.
	"""
	# TODO: Your code goes here
	width = 25
	height = 25
	num_trials = 5
	num_robots = [1,2,3,4,5]
	speed = 1.0
	robot_type = Robot
	visualize = True 
	# initiating a list that contains lists of average time taken to clean a room with different minimum
	# coverage requirements where each list is specific to number of robots used to clean the room.
	avg_listoflists = []
	# initiating a list that contains lists of varying minimum coverages where each list is specific
	# to the number of robots used to clean the room
	coverage_listoflists = []

	for numrobots in num_robots:
		min_coverage = [0.2, 0.3, 0.4, 0.5, 0.6, 0.75, 0.85, 0.9]
		meantime = []
		for coverage in min_coverage:
			avg = runSimulation(numrobots, speed,width,height, coverage, num_trials, robot_type, visualize)
			avglength = AverageListLength(avg)
			meantime.append(avglength)

		avg_listoflists.append(meantime)
		coverage_listoflists.append(min_coverage)

	for each in range(len(avg_listoflists)):
		pylab.plot(coverage_listoflists[each], avg_listoflists[each], label = ('number of robots:' + str(each+1)))
	
	pylab.ylabel( 'mean time' )
	pylab.xlabel( 'minimum coverage' )
	pylab.title( 'time taken to clean a 25x25 room with varying minimum coverage using each 1-5 robots' )
	pylab.legend(loc = 0)
	pylab.show()

# showPlot4()

# === Problem 5

class RandomWalkRobot(BaseRobot):
	"""
	A RandomWalkRobot is a robot with the "random walk" movement
	strategy: it chooses a new direction at random after each
	time-step.
	"""
	# TODO: Your code goes here

	def updatePositionAndClean(self):

		notatwall = True

		while notatwall:
			initial_position = self.getRobotPosition()
			# setting the robot direction to random after every position
			self.setRobotDirection(random.randrange(0,360))
			# updating the robot direction as per the above 
			updated_position = initial_position.getNewPosition(self.getRobotDirection(), self.speed)
			if self.room.isPositionInRoom(updated_position):
				self.p = updated_position
				if not self.room.isTileCleaned(updated_position.getX(), updated_position.getY()):
					self.room.cleanTileAtPosition(updated_position)
					# the function returns if the new robot position is within the room and this position
					# has not already been cleaned.
					notatwall = False 
			else:
				self.d = random.randrange(0,360)

# avg = runSimulation(1, 1.0, 20, 20, 1.0, 1, RandomWalkRobot, True) 

# === Problem 6

def showPlot5():
	"""
	Produces a plot comparing the two robot strategies.
	"""
	# TODO: Your code goes here
	width = 15
	height = 7
	num_trials = 1
	num_robots = 3
	speed = 1.0
	robot_type = [Robot, RandomWalkRobot]
	visualize = True 
	# initiating a list that contains lists of average time taken to clean a room with different minimum
	# coverage requirements where each list is specific to the type of robot used.
	avg_listoflists = []
	# initiating a list that contains lists of varying minimum coverages where each list is specific
	# to the type of robot used
	coverage_listoflists = []

	for types in robot_type:
		min_coverage = [0.2, 0.3, 0.5, 0.65, 0.75, 0.9]
		meantime = []
		for coverage in min_coverage:
			avg = runSimulation(num_robots, speed, width, height, coverage, num_trials, types, visualize)
			avglength = AverageListLength(avg)
			meantime.append(avglength)

		avg_listoflists.append(meantime)
		print(avg_listoflists)
		coverage_listoflists.append(min_coverage) 

	for each in range(len(avg_listoflists)):
		pylab.plot(coverage_listoflists[each], avg_listoflists[each], label = ('robot type is:' + str(robot_type[each])))
	
	pylab.ylabel( 'mean time' )
	pylab.xlabel( 'minimum coverage' )
	pylab.title( 'time taken to clean the tiles with varying minimum coverage using each robot type')
	pylab.legend(loc = 0)
	pylab.show()

# showPlot5()

# Plot 5 displays that is nearly negligible difference between the time taken by this new robot and a normal robot
# Thus, it as good as the previous version, if not better. This may warranty the redundancy of producing the new desgin