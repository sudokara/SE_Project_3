from abc import ABC, abstractmethod
from pathlib import Path

class ICompressionStrategy(ABC):
    """
    The CompressionStrategy defines the interface for compression algorithms that can be used in the CEManager.
    All compression strategies implement this interface and define their own compression and decompression methods.
    """
    def __init__(self, compression_dir:str = ".phnx/compressed", decompression_dir:str = ".phnx/decompressed"):
        Path(compression_dir).mkdir(parents=True, exist_ok=True)
        self.compression_dir = compression_dir
        Path(decompression_dir).mkdir(parents=True, exist_ok=True)
        self.decompression_dir = decompression_dir
    
    @abstractmethod
    def compress(self, file_path, *args, **kwargs):
        pass

    @abstractmethod
    def decompress(self, file_path, *args, **kwargs):
        pass
    