
class Score:

    def __init__(self,id, player, best, accuracy, deception, overall):
        self.id = id
        self.player = player
        self.best = best
        self.accuracy = accuracy
        self.deception = deception
        self.overall = overall

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getPlayer(self):
        return self.player

    def setPlayer(self, player):
        self.player = player

    def getBest(self):
        return self.best

    def setBest(self, best):
        self.best = best

    def getAccuracy(self):
        return self.accuracy

    def setAccuracy(self, accuracy):
        self.accuracy = accuracy

    def getDeception(self):
        return self.deception

    def setDeception(self, deception):
        self.deception = deception

    def getOverall(self):
        return self.overall

    def setOverall(self, overall):
        self.overall = overall
