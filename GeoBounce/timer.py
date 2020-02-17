import time


class Timer(object):
    def __init__(self):
        self.time = time.time()

    def tick(self, interval=60):
        if time.time() - (1 / interval) >= self.time:
            self.time = time.time()
            return True
        else:
            return False
