from .ObservationStrategy import ObservationStrategy
from time import time
import sys
sys.path.append("..")
from Path import Path
from EventHandler import EventHandler

class PeriodicStrategy(ObservationStrategy):
    def __init__(self, period):
        self.period = period
        self.time = 0
        self.observing = False
        self.handler = EventHandler()
    
    # def observe(self):
        # for f in self.state.paths:
        #     if self.handler.check_diff(f): # check if a certain amount of time has passed since last backup
        #         self.handler.backup(f)
            
    def start(self, state: Path): # depending on how master works, add a thread to handle sleep
        self.observing = True
        self.state = state
        while self.observing:
            # self.observe()
            self.handler.backup(self.state.watch_directory)
            time.sleep(self.period)

    def stop(self):
        self.observing = False
        sys.exit(0)
    