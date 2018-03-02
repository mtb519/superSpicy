class Vehicle:
    def __init__(self):
        self.assigned = [] #all ride completed by this vehicle, last element is the current ride being executed
        self.finishingCoords = (0, 0) #coords of the vehicle once it finishes its current ride
        self.finishingTime = 0 #step the car finishes its current ride

    def score(self, Map, Ride, debug=False):
        distanceToStart = Map.distance(self.finishingCoords, Ride.startIntersect)
        waitTime = Ride.earliestStart - (self.finishingTime + distanceToStart)
        timeAtStart = max(Ride.earliestStart, self.finishingTime + distanceToStart)
        timeAtFinish = timeAtStart + Ride.distance()

        score = 0
        bonus = 0
        if timeAtFinish <= Ride.latestFinish and timeAtFinish <= Map.num_steps:
            bonus = int(timeAtStart <= Ride.earliestStart) * Map.ride_bonus
            score = (Ride.distance() + bonus) / (distanceToStart + max(1, waitTime))

        if debug:
            row_format = "{:>16}" * 8
            print(row_format.format(Ride.index, self.finishingTime, distanceToStart, waitTime, timeAtStart, timeAtFinish, bonus, "{:.1f}".format(score)))

        return score

    def assign(self, Map, Ride):
        distanceToStart = Map.distance(self.finishingCoords, Ride.startIntersect)

        self.assigned.append(Ride)
        self.finishingCoords = Ride.finishIntersect
        self.finishingTime = max(Ride.earliestStart, self.finishingTime + distanceToStart) + Ride.distance()
