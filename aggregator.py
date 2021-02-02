import collections, threading
import time
from datetime import datetime


class Aggregator:
    def __init__(self, seconds):
        self.output = ""
        self.prev_counter = collections.Counter()
        self.counter = collections.Counter()
        self.prev_velocity = collections.Counter()
        self.velocity = collections.Counter()
        self.acceleration = collections.Counter()
        self.thread = threading.Thread(target=self.aggregate_counts, args=(seconds,))

    def aggregate_counts(self, seconds: int):
        while True:
            cur_counter = self.counter.copy()
            self.counter = collections.Counter()
            for symbol in cur_counter:
                self.velocity[symbol] = cur_counter[symbol] - self.prev_counter[symbol]
                self.acceleration[symbol] = self.velocity[symbol] - self.prev_velocity[symbol]
            self.prev_counter = cur_counter.copy()
            self.prev_velocity = self.velocity.copy()

            self.generate_output()
            time.sleep(seconds)

    def generate_output(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        top_list = self.prev_counter.most_common(10)
        self.output = dt_string + "</br>"
        for i, e in enumerate(top_list):
            symbol, count = e
            self.output += f"{i+1}: {symbol} | " \
                           f"a: {self.acceleration[symbol]} | " \
                           f"v: {self.velocity[symbol]} | " \
                           f"c: {count}</br>"


    def start_aggregating(self):
        self.thread.start()

    def stop_aggregating(self):
        self.thread.join()

    def get_output(self):
        return self.output
