from abc import ABC, abstractmethod
from ICompressionStrategy import ICompressionStrategy
from IEncryptionStrategy import IEncryptionStrategy
from KeyManager import KeyManager

class CEManager():
    def __init__(self, compressionStrategy: ICompressionStrategy, encryptionStrategy: IEncryptionStrategy):
        self.__compressionStrategy: ICompressionStrategy = compressionStrategy
        self.__encryptionStrategy: IEncryptionStrategy = encryptionStrategy

    def getCompressionStrategy(self):
        return self.__compressionStrategy
    
    def setCompressionStrategy(self, compressionStrategy: ICompressionStrategy):
        self.__compressionStrategy = compressionStrategy

    def getEncryptionStrategy(self):
        return self.__encryptionStrategy
    
    def setEncryptionStrategy(self, encryptionStrategy: IEncryptionStrategy):
        self.__encryptionStrategy = encryptionStrategy

    def compress(self, file_path, *args, **kwargs):
        return self.__compressionStrategy.compress(file_path, *args, **kwargs)

    def encrypt(self, file_path, key, *args, **kwargs):
        return self.__encryptionStrategy.encrypt(file_path, key, *args, **kwargs)