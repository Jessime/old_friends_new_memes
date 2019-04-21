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
from scraper import RedditScraper


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


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    image_url = reddit_scraper.get_top_meme()
    # return reddit_scraper.get_top_meme()
    return render_template('index.html', image_url=image_url)

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.form['comment']
    print(comment)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    reddit_scraper = RedditScraper()
    app.run(host='127.0.0.1', port=8080, debug=True)

# [END gae_python37_app]
