from map import Map
from ride import Ride
from vehicle import Vehicle

def read_input():
    rows, columns, num_vehicles, num_rides, ride_bonus, num_steps = [int(s) for s in input().split(" ")]
    OurMap = Map(rows, columns, num_vehicles, num_rides, ride_bonus, num_steps)
    Vehicles = [Vehicle() for i in range(num_vehicles)]
    Rides = []

    for i in range(0, num_rides):
        start_row, start_column, finish_row, finish_column, earliest_start, latest_finish = [int(s) for s in input().split(" ")]
        Rides.append(Ride(i, (start_row, start_column), (finish_row, finish_column), earliest_start, latest_finish))

    return (OurMap, Vehicles, Rides)

def output(vehicles):
    for vehicle in vehicles:
        string = str(len(vehicle.assigned))
        for ride in vehicle.assigned:
            string += " " + str(ride.index)
        print(string)

def main():
    OurMap, Vehicles, Rides = read_input()
    Rides = sorted(Rides, key=Ride.getEarliestStartTime)

    for rideNumber in range(0, len(Rides)):
        highestScore = (0, None)
        for car in Vehicles:
            score = car.score(OurMap, Rides[rideNumber])
            if score > highestScore[0]:
                highestScore = (score, car)
        highestScore[1].assigned.append(Rides[rideNumber])

        print(str(Rides[rideNumber].earliestStart))

    output(Vehicles)

if __name__ == '__main__':
    main()
