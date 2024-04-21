from abc import ABC, abstractmethod

class IKeyStrategy(ABC):
    """
    The KeyStrategy defines the interface for key generation and retrieval algorithms that can be used in the CEManager.
    All key strategies implement this interface and define their own key generation and retrieval methods.
    """
    
    @abstractmethod
    def generate_key(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_key(self, *args, **kwargs):
        pass