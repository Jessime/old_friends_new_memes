import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import storage


### create a new game ######
comments_dict={}
top_comments = ["Hola amigo", "this sucks", "awesome dude"]
url = "www.reddit.com/bestMeme"
comments_dict['top_comments'] = top_comments
comments_dict['url'] = url
print(comments_dict)


###### Testing if a new user commented
new_comment = "Life is awesome"
new_player = "Wes"

####### Example of  vote ##########
submitter = "Jessime"
funniest_Comment = "Trump is such an ass"
bots_comments = ["Hola amigo", "this sucks", "awesome dude"]

##### Example of scores #######
header = ['player', 'best', 'accuracy', 'deception', 'overall']
row1 = ['Jessime', 0.8, 0.96, 0.5, 0.7]
row2 = ['Kimiko', 0.8, 0.96, 0.5, 0.7]
row3 = ['Wes', 0.8, 0.96, 0.5, 0.7]
row4 = ['Sherif', 0.8, 0.96, 0.5, 0.7]

scores = [header, row1, row2, row3, row4 ]

storage = storage.Storage()
#storage.save_reddit_data(comments_dict)
#print("########")
#print("Boolan: ", storage.didUserComment("Mike"))
#print("CurrentGameId: ", storage.getCurrentGameId())
#print("save_new_Comment: ", storage.save_player_comment(new_comment, new_player))
#print("Save a new vote: ", storage.save_player_vote(submitter, funniest_Comment, bots_comments))
#print("All_players_votes: ",  storage.all_players_voted())
print("Final_Score: ", storage.save_player_scores(scores))
