class Vehicle:
    def __init__(self):
        self.assigned = [] #all ride completed by this vehicle, last element is the current ride being executed
        self.finishingCoords = (0, 0) #coords of the vehicle once it finishes its current ride
        self.finishingTime = 0 #step the car finishes its current ride

    def score(self, Map, Ride):
        distanceToStart = Map.distance(self.finishingCoords, Ride.startIntersect)
        waitTime = Ride.earliestStart - (self.finishingTime + distanceToStart)
        if self.finishingTime + distanceToStart + max(0, waitTime) + Ride.distance() > Ride.latestFinish:
            return 0
        else:
            bonus = int(waitTime >= 0) * Map.ride_bonus
            score = (Ride.distance() + bonus) / (distanceToStart + max(0, waitTime) + 1)
            return score
