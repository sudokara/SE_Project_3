from abc import ABC, abstractmethod
from ICompressionStrategy import ICompressionStrategy
from IEncryptionStrategy import IEncryptionStrategy
from KeyManager import KeyManager

class CEManager():
    def __init__(self, compressionStrategy: ICompressionStrategy, encryptionStrategy: IEncryptionStrategy, keyManager: KeyManager):
        self.__compressionStrategy: ICompressionStrategy = compressionStrategy
        self.__encryptionStrategy: IEncryptionStrategy = encryptionStrategy
        self.__keyManager: KeyManager = keyManager

    def getCompressionStrategy(self):
        return self.__compressionStrategy
    
    def setCompressionStrategy(self, compressionStrategy: ICompressionStrategy):
        self.__compressionStrategy = compressionStrategy

    def getEncryptionStrategy(self):
        return self.__encryptionStrategy
    
    def setEncryptionStrategy(self, encryptionStrategy: IEncryptionStrategy):
        self.__encryptionStrategy = encryptionStrategy

    def getKeyManager(self):
        return self.__keyManager
    
    def setKeyManager(self, keyManager: KeyManager):
        self.__keyManager = keyManager

    def compress(self, file_path, *args, **kwargs):
        return self.__compressionStrategy.compress(file_path, *args, **kwargs)
    
    def decompress(self, file_path, *args, **kwargs):
        return self.__compressionStrategy.decompress(file_path, *args, **kwargs)

    def encrypt(self, file_path, *args, **kwargs):
        return self.__encryptionStrategy.encrypt(file_path, self.__keyManager.get_key(), *args, **kwargs)
    
    def decrypt(self, file_path, *args, **kwargs):
        return self.__encryptionStrategy.decrypt(file_path, self.__keyManager.get_key(), *args, **kwargs)