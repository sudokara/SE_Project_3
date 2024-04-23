"""
Handles communication between subsytstems. Uses a singleton pattern so that strategies can be retained,
but needs to be initialized with the intended strategies before use.
"""
from phoenix.Compression_Encryption.CEManager import CEManager
from phoenix.Compression_Encryption.KeyManager import KeyManager
from SingletonMeta import SingletonMeta

class Broker(metaclass=SingletonMeta):
    def __init__(self, keyStrategy=None, compressionStrategy=None, encryptionStrategy=None) -> None:
        self.__keyManager = KeyManager(keyStrategy)
        self.__ceManager = CEManager(compressionStrategy, encryptionStrategy, self.__keyManager)

    def backup(self, file_path, is_file):
        compressed_path = self.__ceManager.compress(file_path, is_file)
        encrypted_path = self.__ceManager.encrypt(compressed_path, self.__keyManager.get_key(), is_file)
        return encrypted_path

    def set_key_strategy(self, keyStrategy):
        self.__keyManager.set_key_strategy(keyStrategy)

    def set_compression_strategy(self, compressionStrategy):
        self.__ceManager.setCompressionStrategy(compressionStrategy)

    def set_encryption_strategy(self, encryptionStrategy):
        self.__ceManager.setEncryptionStrategy(encryptionStrategy)