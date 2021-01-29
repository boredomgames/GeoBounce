import time


class Timer(object):
    def __init__(self):
        self.time = time.time()

    def begin(self):
        self.time = time.time()

    def end(self, fps=60):
        time.sleep(max((1 / fps - (time.time() - self.time)) / 1.25, 0))
