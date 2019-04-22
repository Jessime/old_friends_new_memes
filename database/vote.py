
class Vote:

    def __init__(self,id, submitter, funniest_Comment, bots_list):
        self.id = id
        self.submitter = submitter
        self.funniest_Comment = funniest_Comment
        self.bots_list = bots_list

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getSubmitter(self):
        return self.submitter

    def setSubmitter(self, submitter):
        self.submitter = submitter

    def getfunniest_Comment(self):
        return self.funniest_Comment

    def setFunniest_Comment(self, funniest_Comment):
        self.funniest_Comment = funniest_Comment

    def getBots_list(self):
        return self.bots_list

    def setBots_list(self, bots_list):
        self.bots_list = bots_list
