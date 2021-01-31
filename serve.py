import threading
import time
from datetime import datetime
import json
import praw
from flask import Flask

v2_gme = [0]
v2_amc = [0]
prev_v1_gme = [0]
prev_v1_amc = [0]
v1_gme = [0]
v1_amc = [0]
prev_gme_count = [0]
prev_amc_count = [0]
gme_count = [0]
amc_count = [0]
output = [""]

with open('credentials.json') as f:
  credentials = json.load(f)

reddit = praw.Reddit(client_id=credentials["client_id"],
                     client_secret=credentials["client_secret"],
                     password=credentials["password"],
                     user_agent="testscript by u/fakebot3",
                     username=credentials["username"])

app = Flask(__name__)


@app.route('/')
def hello_world():
    return output[0]


def stream_comments():
    for comment in reddit.subreddit("wallstreetbets").stream.comments():
        body = str(comment.body)
        gme_count[0] += body.upper().count("GME")
        amc_count[0] += body.upper().count("AMC")

def aggregate_counts():
    while True:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        v1_gme[0] = gme_count[0] - prev_gme_count[0]
        v1_amc[0] = amc_count[0] - prev_amc_count[0]
        v2_gme[0] = v1_gme[0] - prev_v1_gme[0]
        v2_amc[0] = v1_amc[0] - prev_v1_amc[0]

        output[0] += f"{dt_string} V2_GME: {v2_gme[0]} V2_AMC: {v2_amc[0]} V1_GME: {v1_gme[0]} V2_AMC: {v1_amc[0]} GME: {gme_count[0]} AMC: {amc_count[0]}<br/>"
        prev_v1_gme[0] = v1_gme[0]
        prev_v1_amc[0] = v1_amc[0]
        prev_gme_count[0] = gme_count[0]
        prev_amc_count[0] = amc_count[0]
        gme_count[0] = 0
        amc_count[0] = 0
        time.sleep(10)


stream = threading.Thread(target=stream_comments)
aggregate = threading.Thread(target=aggregate_counts)
stream.start()
aggregate.start()

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=9999)
