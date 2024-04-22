from abc import ABC, abstractmethod
import sys

sys.path.append("..")
from Path import Path

class ObservationStrategy(ABC):
    
    '''
    Observe the state and also call the backup function if state has changed
    '''
    @abstractmethod
    def observe(self, state):
        pass
    
    '''
    Start the observer
    '''
    @abstractmethod
    def start(self, state: Path):
        pass

    '''
    Stop the observer
    '''
    @abstractmethod
    def stop(self):
        pass