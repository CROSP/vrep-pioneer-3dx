import sys

import rx
from rx import Observer


class InputLoopObserver(Observer):
    def __init__(self):
        self.input_handlers = {}
        self.is_running = True

    def on_next(self, value):
        print("Received {0}".format(value))

    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("Error Occurred: {0}".format(error))


user_input_observable = rx.Observable.from_(sys.stdin)
user_input_observable.subscribe(InputLoopObserver())
