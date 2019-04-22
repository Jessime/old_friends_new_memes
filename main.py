# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from datetime import datetime
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from scraper import RedditScraper
import random
import numpy as np
import matplotlib.pyplot as plt
import base64

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/update_time')
def update_time():
    with open('time.txt', 'w') as outfile:
        outfile.write(str(datetime.now()))
    return 'success'

@app.route('/time')
def time():
    with open('time.txt') as infile:
        time = infile.read()
    return time


@app.route('/', methods=['GET','POST'])
def index():
    """Return a friendly HTTP greeting."""
    # has_user_submitted = ping storage DB to see if called for this week, need to send user?
    # has_user_submitted = False
    # if has_user_submitted:
    #     return redirect(url_for('already_submitted'))

    image_url = reddit_scraper.get_top_meme()
    # return reddit_scraper.get_top_meme()
    return render_template('index.html', image_url=image_url)

@app.route('/submitted', methods=['GET','POST'])
def submitted():
    if request.method == 'POST':
        comment = request.form['comment']
        print(comment)
    return render_template('submitted.html')

@app.route('/voting', methods=['GET','POST'])
def voting():
    # has_user_submitted = ping storage DB to see if called for this week, need to send user?
    # has_user_submitted = False
    # if has_user_submitted:
    #     return redirect(url_for('already_submitted'))
    comments = ['1','2','3','4','5','6'] # connect with sherif
    image_url = reddit_scraper.get_top_meme()
    return render_template('voting.html', comments=comments, image_url=image_url)

@app.route('/voted', methods=['GET','POST'])
def voted():
    # has_user_submitted = ping storage DB to see if called for this week, need to send user?
    # has_user_submitted = False
    # if has_user_submitted:
    #     return redirect(url_for('already_submitted'))
    print(request.form)
    if request.method == 'POST':
        best = request.form['best']
        comments = []
        for i in range(1, 7):
            comment = request.form.get(f'bots{i}', None)
            if comment is not None:
                comments.append(comment)
        print(comments)
    return render_template('voted.html')

@app.route('/results')
def results():
    count = 500
    xScale = np.linspace(0, 100, count)
    yScale = np.random.randn(count)
    graph_file = 'score_history.png'
    plt.clf()
    plt.scatter(xScale,yScale)
    plt.savefig(graph_file)
    with open(graph_file, 'rb') as infile:
        string = base64.b64encode(infile.read()).decode("utf-8")
    # graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('results.html', plot=string)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    reddit_scraper = RedditScraper()
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END gae_python37_app]
