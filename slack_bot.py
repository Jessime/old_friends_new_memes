import os
from slackclient import SlackClient


class SlackBot:

    def __init__(self):
        SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
        self.slack_client = SlackClient(SLACK_TOKEN)
        self.name = 'ofnm'
        self.index = 'https://old-friends-new-memes.appspot.com'
        self.voting = self.index + '/voting'
        self.results = self.index + '/results'

    def send_message(self, message, channel_id='general'):
        self.slack_client.api_call(
            "chat.postMessage",
            channel=channel_id,
            text=message,
            username=self.name,
            icon_emoji=':robot_face:'
        )

    def new_game(self):
        message = ('Hey, friends! '
                   'The game for this week is ready to go. '
                  f'Click below to play!\n{self.index}\n')
        self.send_message(message)

    def do_voting(self):
        message = ("Ahoy, Mateys! "
                   "People are finished submitting. "
                   f"It's time to v-v-v-vote!\n{self.voting}\n")
        self.send_message(message)

    def see_results(self):
        message = ('Hola, amigos. '
                   f'Wanna see how you did this week?\n{self.results}\n')
        self.send_message()