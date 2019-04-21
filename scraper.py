import os
import praw

class RedditScraper:

    def __init__(self):
        self.reddit = praw.Reddit(client_id='NClWY-91GSZ3oQ',
                                  client_secret=os.environ['OFNM_SECRET'],
                                  user_agent='Old Friends, New Memes')

        self.top_submission = None

    def get_top_meme(self, use_sub='memes', n=100):
        subreddit = self.reddit.subreddit(use_sub)

        for submission in subreddit.top(limit=n, time_filter='week'):
            if not submission.is_self:
                break

        self.top_submission =submission

        return submission.url

    def get_top_comments(self, n=3):
        submission = self.reddit.submission(id=self.top_submission)

        comments_list = []

        for i in range(0,n):
            comments_list.append(submission.comments[i].body)

        comments_dict = {
            "top_comments": comments_list,
            "url" : submission.url
        }

        return comments_dict
