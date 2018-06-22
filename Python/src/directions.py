import math 

class Directions():
	def __init__(self, distance):
		self.directions = []
		r = distance	# (r)adius is the distance to be traveled
		for angle in range(360):
			x = math.cos(math.radians(angle)) * r
			y = math.sin(math.radians(angle)) * r
			direction = (x, y)
			self.directions.append(direction)
	def __getitem__(self, index):
		return self.directions[index]

def angle_of_point(point, origin):
	# I hate the way this works.  
	# I have to remap the plane quadrants to quarters of the angle array 
	# using the signs of the coordinates x and y.
	# I wish I could just use a deterministic lookup or a declarative mathematical formula.
	# Seems like I must be doing it wrong.
	px, py = point
	ox, oy = origin
	x = px - ox
	y = py - oy
	h = math.sqrt((x * x) + (y * y))

	angle = math.degrees(math.asin(abs(y) / (h + 0.000001)))

	if (y < 0): 
		angle = angle + 180
		if (x > 0):
			angle = (90-angle) + 90
	elif(x < 0):
		angle = (90-angle) + 90

	return int(angle)

