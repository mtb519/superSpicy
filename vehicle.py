class Vehicle:
    def __init__(self):
        self.assigned = [] #all ride completed by this vehicle, last element is the current ride being executed
        self.finishingCoords = (0, 0) #coords of the vehicle once it finishes its current ride
        self.finishingTime = 0 #step the car finishes its current ride


