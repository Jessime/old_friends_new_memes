import os
import praw


class RedditScraper:

    def __init__(self):
        self.reddit = praw.Reddit(client_id='NClWY-91GSZ3oQ',
                                  client_secret=os.environ['OFNM_SECRET'],
                                  user_agent='Old Friends, New Memes')

    def get_top_meme(self):
        pass

    def get_top_comments(self):
        pass
