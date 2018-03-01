import map
import ride

Rides = []
Map = None

def read_input():
	rows, columns, num_vehicles, num_rides, ride_bonus, num_steps = [int(s) for s in input().split(" ")]
	Map = Map(rows, columns, num_vehicles, num_rides, ride_bonus, num_steps)
	
	for i in range(0, num_rides):
		start_row, start_column, finish_row, finish_column, earliest_start, latest_finish = [int(s) for s in input().split(" ")]
		Rides.append(Ride((start_row, start_column), (finish_row, finish_column), earliest_start, latest_finish))

def main():
	read_input()

if __name__ == '__main__':
	main()