class Map(object):
	
	def __init__(self, rows, columns, num_vehicles, num_rides, ride_bonus, num_steps):
		super(Map, self).__init__()
		self.rows = rows
		self.columns = columns
		self.num_vehicles = num_vehicles
		self.num_rides = num_rides
		self.ride_bonus = ride_bonus
		self.num_steps = num_steps

	def distance(self, pos1, pos2):
		return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])