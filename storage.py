import firebase_admin
from firebase_admin import firestore


class Storage:
    """
    Must have GOOGLE_APPLICATION_CREDENTIALS set. See:
        https://firebase.google.com/docs/firestore/quickstart
    for more details.
    """
    def __init__(self):
        self.default_app = firebase_admin.initialize_app()
        self.db = firestore.client()

    def save_reddit_data(self):
        pass

    def save_player_comment(self):
        pass

    def all_players_submitted(self):
        pass

    def save_player_vote(self):
        pass

    def all_players_voted(self):
        pass

    def save_player_scores(self):
        pass
