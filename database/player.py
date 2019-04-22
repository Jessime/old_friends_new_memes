
class Player:

    def __init__(self, first, last, dob):
        self.first = first
        self.last = last
        self.dob = dob

    def getFirst(self):
        return self.first

    def setFirst(self, first):
        self.first = first

    def getLast(self):
        return self.last

    def setLast(self, last):
        self.last = last

    def getDob(self):
        return self.dob

    def setDob(self, dob):
        self.dob = dob
