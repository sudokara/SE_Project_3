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
import requests


class Broker(metaclass=SingletonMeta):
    def __init__(self, keyStrategy=GPGKeyStrategy(os.path.expanduser('~/.gnupg')), compressionStrategy=TarCompressionStrategy(), encryptionStrategy=GPGEncryptionStrategy()) -> None:
        
        self.__keyManager = KeyManager(keyStrategy)
        self.__ceManager = CEManager(
            compressionStrategy, encryptionStrategy, self.__keyManager)

    def backup(self, file_path, is_file):
        compressed_path = self.__ceManager.compress(file_path, is_file)
        if is_file:
            encrypted_path = self.__ceManager.encrypt(
            compressed_path, self.__keyManager.get_key(), is_file)

            encrypted_path = f"../Compression_Encryption/{encrypted_path}"

            url = "http://localhost:5001/upload"
            headers = {
                "content-type": "application/json"
            }
            data = {
                "encryptedPath": encrypted_path
            }

            response = requests.post(url, headers=headers, json=data)

        else:
            for p in compressed_path:
                encrypted_path = self.__ceManager.encrypt(
                    p, self.__keyManager.get_key(), is_file)
                
                encrypted_path = f"../Compression_Encryption/{encrypted_path}"

                url = "http://localhost:5001/upload"
                headers = {
                    "content-type": "application/json"
                }
                data = {
                    "encryptedPath": encrypted_path
                }

                response = requests.post(url, headers=headers, json=data)
                

    def set_key_strategy(self, keyStrategy):
        self.__keyManager.set_key_strategy(keyStrategy)

    def set_compression_strategy(self, compressionStrategy):
        self.__ceManager.setCompressionStrategy(compressionStrategy)

    def set_encryption_strategy(self, encryptionStrategy):
        self.__ceManager.setEncryptionStrategy(encryptionStrategy)

    # def upload(self, filepath):
    #     self.__uploader.upload_file(filepath)

    def download(self, filepath, **kwargs):
        self.__uploader.download_file(filepath, **kwargs)