import firebase_admin
from firebase_admin import firestore
import datetime
import comment
import player
import game
import vote
import score

class Storage:
    """
    Must have GOOGLE_APPLICATION_CREDENTIALS set. See:
        https://firebase.google.com/docs/firestore/quickstart
    for more details.
    """
    def __init__(self):
        self.default_app = firebase_admin.initialize_app()
        self.db = firestore.client()

    def save_reddit_data(self, comment_dict):
        return self.createGame(comment_dict, self.db)

    def save_player_comment(self, comment, player):
        return self.save_comment(comment, player)

    def all_players_submitted(self):
        counter_game = self.getCurrentGameId()
        doc = self.db.collection(u'games').document(str(counter_game)).get()
        info = doc.to_dict()
        print(info)
        return (len(info.get("players"))==7)

    def save_player_vote(self, submitter, funniest_Comment, bots_comments):
        counter_game = self.getCurrentGameId()
        counter_vote = self.getCurrentVoteId(counter_game)
        vote_id  = counter_vote + 1
        v = vote.Vote(vote_id, submitter, funniest_Comment, bots_comments)
        vote_dict = {}
        vote_dict["Submitter"] = v.getSubmitter()
        vote_dict["Funniest_Comment"] = v.getfunniest_Comment()
        vote_dict["Bots_comments"] = v.getBots_list()
        self.db.collection(u'games').document(str(counter_game)).collection(u'votes').document(str(v.getId())).set(vote_dict)
        return vote_id

    def all_players_voted(self):
        counter_game = self.getCurrentGameId()
        counter_vote = self.getCurrentVoteId(counter_game)
        docs = self.db.collection(u'games').document(str(counter_game)).collection(u'votes').get()
        submitters = []
        for doc in docs:
            info = doc.to_dict()
            submitters.append(info.get("Submitter"))

        doc = self.db.collection(u'games').document(str(counter_game)).get()
        info = doc.to_dict()
        players = info.get("players")
        print(players)
        a = all((s in players) for s in submitters)
        print("A", a)
        b = len(submitters)==len(players)
        print("B", b)
        return (a and b)

    def save_player_scores(self, scores):
        counter_game = self.getCurrentGameId()
        for  i in range (1, len(scores)):
            row = scores[i]
            counter_score = self.getCurrentScoreId(counter_game)
            score_id  = counter_score + 1
            s = score.Score(score_id, str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]))
            score_dict = {}
            score_dict["Player"] = s.getPlayer()
            score_dict["Best"] = s.getBest()
            score_dict["Accuracy"] = s.getAccuracy()
            score_dict["Deception"] = s.getDeception()
            score_dict["Overall"] = s.getOverall()
            self.db.collection(u'games').document(str(counter_game)).collection(u'scores').document(str(s.getId())).set(score_dict)
        return score_id

############ Sherif #############

    def createGame(self, comments_dict, db):
        comments = []
        players = []
        counter = self.getCurrentGameId()
        game_id = counter + 1
        #print("game_id: ", game_id)
        for i in range(len(comments_dict['top_comments'])):
            comment_id = i+1
            content = comments_dict['top_comments'][i]
            player = "internet_player_" + str(i+1)
            submission_timeStamp = datetime.datetime.now()
            com = comment.Comment(comment_id, content, player, submission_timeStamp)
            comments.append(com)
            players.append(player)

        g = game.Game(game_id, comments, players, comments_dict['url'])

        game_dict ={}
        game_dict['url'] = g.getUrl()
        game_dict['players'] = g.getPlayers()

        doc_ref = self.db.collection(u'games').document(str(g.getId()))
        doc_ref.set(game_dict)

        listcomment_dicts = []
        comment_dict ={}
        for c in g.getComments():
            comment_dict["Player"] = c.getPlayer()
            comment_dict["Content"] = c.getContent()
            comment_dict["Submission_timeStamp"] = c.getSubmission_timeStamp()
            listcomment_dicts.append(comment_dict)
            self.db.collection(u'games').document(str(g.getId())).collection(u'comments').document(str(c.getId())).set(comment_dict)
        return game_id

    def didUserComment(self, player):
        counter = self.getCurrentGameId()
        doc = self.db.collection(u'games').document(str(counter)).get()
        info = doc.to_dict()
        print(info)
        return player in info.get("players")

    def getCurrentGameId(self):
        docs = self.db.collection(u'games').get()
        counter =0
        for doc in docs:
            counter += 1
        return counter

    def getCurrentCommentId(self, counter_game):
        docs=self.db.collection(u'games').document(str(counter_game)).collection(u'comments').get()
        counter = 0
        for doc in docs:
            counter += 1
        return counter

    def getCurrentVoteId(self, counter_game):
        docs = self.db.collection(u'games').document(str(counter_game)).collection(u'votes').get()
        counter = 0
        for doc in docs:
            counter += 1
        return counter

    def getCurrentScoreId(self, counter_game):
        docs = self.db.collection(u'games').document(str(counter_game)).collection(u'scores').get()
        counter = 0
        for doc in docs:
            counter += 1
        return counter

    def save_comment(self, content, player):
        counter_game = self.getCurrentGameId()
        counter_comment = self.getCurrentCommentId(counter_game)

        comment_id = counter_comment + 1
        print("comment_id: ", comment_id)
        submission_timeStamp = datetime.datetime.now()
        com = comment.Comment(comment_id, content, player, submission_timeStamp)

        comment_dict ={}
        comment_dict["Player"] = com.getPlayer()
        comment_dict["Content"] = com.getContent()
        comment_dict["Submission_timeStamp"] = com.getSubmission_timeStamp()

        print("comment_dict: ", comment_dict)
        self.db.collection(u'games').document(str(counter_game)).collection(u'comments').document(str(com.getId())).set(comment_dict)

        #### update the game with the extra comment and the new player
        counter = self.getCurrentGameId()
        doc = self.db.collection(u'games').document(str(counter)).get()
        info = doc.to_dict()
        print("before:" , info)
        info.get("players").append(player)
        print("after:" , info)
        return comment_id
