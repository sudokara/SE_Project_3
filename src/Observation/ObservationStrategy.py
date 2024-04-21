from abc import ABC, abstractmethod

class ObservationStrategy(ABC):
    
    
    '''
    Observe the state and also call the backup function if state has changed
    '''
    @abstractmethod
    def observe(self, state):
        pass
    
    # '''
    # Close the observer
    # '''
    # @abstractmethod
    # def close(self):
    #     pass
    
    '''
    Start the observer
    '''
    @abstractmethod
    def start(self):
        pass