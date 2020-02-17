import time


class Timer(object):
    def __init__(self):
        self.time = time.time()

    def begin(self):
        self.time = time.time()

    def end(self, fps=60):
        time.sleep(max(1 / fps - (time.time() - self.time), 0))

    def tick(self, interval=60):  # legacy api, do not use
        if time.time() - (1 / interval) >= self.time:
            self.time = time.time()
            return True
        else:
            return False
