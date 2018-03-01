class Ride(object):

    def __init__(self, index, startIntersect, finishIntersect, earliestStart, latestFinish):
        self.index = index
        self.startIntersect = startIntersect
        self.finishIntersect = finishIntersect
        self.earliestStart = earliestStart
        self.latestFinish = latestFinish

    def distance(self):
        return abs(self.startIntersect[0] - self.finishIntersect[0]) + abs(self.startIntersect[1] - self.finishIntersect[1])

    def getEarliestStartTime(self):
        return self.earliestStart
