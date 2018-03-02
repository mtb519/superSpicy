from map import Map
from ride import Ride
from vehicle import Vehicle

DEBUG = True

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
    Rides = sorted(Rides, key=lambda r: r.earliestStart)

    if DEBUG:
        total = 0
        for ride in Rides:
            total += ride.distance()
        print("Upper-bound on score / with bonuses: {:d} / {:d}".format(total, total + OurMap.ride_bonus * len(Rides)))
        print()

        row_format = "{:>16}"
        print("Accepted Rides: ")
        print((row_format * 8).format("R.Index", "finishingTime", "distanceToStart", "waitTime", "timeAtStart", "timeAtFinish", "bonus", "score"))
    
    unnassigned = []
    
    for ride in Rides:
        highestScore = (0, None)
        for car in Vehicles:
            score = car.score(OurMap, ride)
            if score > highestScore[0]:
                highestScore = (score, car)
        if highestScore[0] > 0:
            if DEBUG:
                highestScore[1].score(OurMap, ride, debug=True)

            highestScore[1].assign(OurMap, ride)
        else:
            unnassigned.append(ride)

    if DEBUG:
        print("\nRejected Rides:")
        print((row_format * 6).format("R.Index", "startIntersect", "finishIntersect", "earliestStart", "latestFinish", "distance"))
        for ride in unnassigned:
            print((row_format * 6).format(ride.index, str(ride.startIntersect), str(ride.finishIntersect), ride.earliestStart, ride.latestFinish, ride.distance()))
    
    output(Vehicles)

if __name__ == '__main__':
    main()
