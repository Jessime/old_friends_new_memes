class Game:

    def __init__(self, id, comments, players, url):
        self.id = id
        self.comments = comments
        self.players = players
        self.url = url

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getComments(self):
        return self.comments

    def setComments(self, comments):
        self.comments = comments

    def getPlayers(self):
        return self.players

    def setId(self, players):
        self.players = players

    def getUrl(self):
        return self.url

    def setUrl(self, url):
        self.url = url
