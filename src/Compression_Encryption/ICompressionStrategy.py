from abc import ABC, abstractmethod

class ICompressionStrategy(ABC):
    """
    The CompressionStrategy defines the interface for compression algorithms that can be used in the CEManager.
    All compression strategies implement this interface and define their own compression and decompression methods.
    """
    
    @abstractmethod
    def compress(self, file_path, *args, **kwargs):
        pass

    @abstractmethod
    def decompress(self, file_path, *args, **kwargs):
        pass
    