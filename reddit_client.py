import json, praw, collections
import threading


class RedditClient:
    def __init__(self, aggregator):
        with open('credentials.json') as f:
            credentials = json.load(f)
            self.reddit = praw.Reddit(client_id=credentials["client_id"],
                                      client_secret=credentials["client_secret"],
                                      password=credentials["password"],
                                      user_agent="testscript by u/fakebot3",
                                      username=credentials["username"])

        with open('symbols.json') as f:
            self.symbols = json.load(f)

        self.stream = threading.Thread(target=self.stream_comments, args=(aggregator,))

    def stream_comments(self, aggregator):
        while True:
            try:
                for comment in self.reddit.subreddit("wallstreetbets").stream.comments():
                    body = str(comment.body)
                    body = body.split()
                    for word in body:
                        if word[0] == "$":
                            aggregator.counter[word[1:]] += 1
                        elif word in self.symbols:
                            aggregator.counter[word] += 1
            except Exception as e:
                print(e)

    def start_streaming(self):
        self.stream.start()

    def stop_streaming(self):
        self.stream.join()
