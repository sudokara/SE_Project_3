from ObservationStrategy import ObservationStrategy
from time import time
from .. import Path
from EventHandler import EventHandler

class Periodic(ObservationStrategy):
    def __init__(self, period):
        self.period = period
        self.time = 0
        self.observing = False
        self.handler = EventHandler()
    
    def observe(self, state: Path):
        files = state.get_all_files()
        for f in files:
            if self.handler.check_diff(f): # check if a certain amount of time has passed since last backup
                self.handler.backup(f)
            
    def close(self):
        self.observing = False
    
    def start(self, state: Path): # depending on how master works, add a thread to handle sleep
        self.observing = True
        while self.observing:
            self.observe(state)
            time.sleep(self.period)