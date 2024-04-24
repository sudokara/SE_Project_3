"""
Handles communication between subsytstems. Uses a singleton pattern so that strategies can be retained,
but needs to be initialized with the intended strategies before use.
"""
import os

from phoenix.Uploader.Strategy import UploadDownloadStrategy
from phoenix.Compression_Encryption.CEManager import CEManager
from phoenix.Compression_Encryption.KeyManager import KeyManager
from phoenix.Compression_Encryption.GPGKeyStrategy import GPGKeyStrategy
from phoenix.Compression_Encryption.TarCompressionStrategy import TarCompressionStrategy
from phoenix.Compression_Encryption.GPGEncryptionStrategy import GPGEncryptionStrategy
from phoenix.utils.SingletonMeta import SingletonMeta
from phoenix.Uploader.Uploader import Uploader


class Broker(metaclass=SingletonMeta):
    def __init__(self, uploadDownloadStrategy: UploadDownloadStrategy = None, keyStrategy=GPGKeyStrategy(os.path.expanduser('~/.gnupg')), compressionStrategy=TarCompressionStrategy(), encryptionStrategy=GPGEncryptionStrategy()) -> None:
        if uploadDownloadStrategy is None:
            raise ValueError("UploadDownloadStrategy cannot be None")
        
        self.__keyManager = KeyManager(keyStrategy)
        self.__ceManager = CEManager(
            compressionStrategy, encryptionStrategy, self.__keyManager)
        
        self.__uploadDownloadStrategy = uploadDownloadStrategy
        self.__uploader = Uploader(self.__uploadDownloadStrategy)

    def backup(self, file_path, is_file):
        compressed_path = self.__ceManager.compress(file_path, is_file)
        if is_file:
            encrypted_path = self.__ceManager.encrypt(
            compressed_path, self.__keyManager.get_key(), is_file)
            self.upload(encrypted_path)
        else:
            for p in compressed_path:
                encrypted_path = self.__ceManager.encrypt(
                    p, self.__keyManager.get_key(), is_file)
                self.upload(encrypted_path)
                

    def set_key_strategy(self, keyStrategy):
        self.__keyManager.set_key_strategy(keyStrategy)

    def set_compression_strategy(self, compressionStrategy):
        self.__ceManager.setCompressionStrategy(compressionStrategy)

    def set_encryption_strategy(self, encryptionStrategy):
        self.__ceManager.setEncryptionStrategy(encryptionStrategy)

    def upload(self, filepath):
        self.__uploader.upload_file(filepath)

    def download(self, filepath, **kwargs):
        self.__uploader.download_file(filepath, **kwargs)