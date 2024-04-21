from abc import ABC, abstractmethod

class IEncryptionStrategy(ABC):
    """
    The EncryptionStrategy defines the interface for encryption algorithms that can be used in the CEManager.
    All encryption strategies implement this interface and define their own encrypt and decrypt methods.
    """
    
    @abstractmethod
    def encrypt(self, file_path, key, *args, **kwargs):
        pass

    @abstractmethod
    def decrypt(self, file_path, key, *args, **kwargs):
        pass
    