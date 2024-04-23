from phoenix.utils.SingletonMeta import SingletonMeta
from phoenix.Compression_Encryption.IKeyStrategy import IKeyStrategy

class KeyManager(metaclass=SingletonMeta):
    """
    The KeyManager class is a Singleton that manages the encryption and decryption keys for the CEManager.
    """
    def __init__(self, keyStrategy: IKeyStrategy):
        self.__keyStrategy = keyStrategy
        self.__key = None
    
    def generate_key(self, *args, **kwargs):
        """
        Generates a new encryption key using the key strategy.
        """
        self.__key = self.__keyStrategy.generate_key(*args, **kwargs)

    def get_key(self, *args, **kwargs):
        """
        Retrieves the encryption key using the key strategy.
        """
        if not self.__key:
            self.__key = self.__keyStrategy.get_key(*args, **kwargs)
        return self.__key
    
    def set_key_strategy(self, keyStrategy: IKeyStrategy):
        """
        Sets the key strategy for the KeyManager.
        """
        self.__keyStrategy = keyStrategy
        self.__key = None