
class Comment:

    def __init__(self,id, content, player, submission_timeStamp):
        self.id = id
        self.content = content
        self.player = player
        self.submission_timeStamp = submission_timeStamp

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content

    def getPlayer(self):
        return self.player

    def setPlayer(self, player):
        self.player = player

    def getSubmission_timeStamp(self):
        return self.submission_timeStamp

    def setSubmission_timeStamp(self, submission_timeStamp):
        self.submission_timeStamp = submission_timeStamp
