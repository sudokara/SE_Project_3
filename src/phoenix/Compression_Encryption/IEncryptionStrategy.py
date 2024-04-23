from abc import ABC, abstractmethod
from pathlib import Path

class IEncryptionStrategy(ABC):
    """
    The EncryptionStrategy defines the interface for encryption algorithms that can be used in the CEManager.
    All encryption strategies implement this interface and define their own encrypt and decrypt methods.
    """
    def __init__(self, encryption_dir:str = ".phnx/encrypted", decryption_dir:str = ".phnx/decrypted"):
        """Initialize the strategy by setting up the directories for encryption and decryption.

        Args:
            encryption_dir (str, optional): Directory where encrypted files will be stored. Defaults to ".phnx/encrypted".
            decryption_dir (str, optional): Directory where decrypted files will be stored. Defaults to ".phnx/decrypted".
        """
        Path(encryption_dir).mkdir(parents=True, exist_ok=True)
        self.encryption_dir = encryption_dir
        Path(decryption_dir).mkdir(parents=True, exist_ok=True)
        self.decryption_dir = decryption_dir

    @abstractmethod
    def encrypt(self, file_path: str, key, *args, **kwargs):
        """Encrypt file at file_path using key. Stored to encryption_dir.

        Args:
            file_path (str): Path of file to encrypt.
            key (_type_): Encryption key
        """
        pass

    @abstractmethod
    def decrypt(self, file_path, key, *args, **kwargs):
        """Decrypt file at file_path using key. Stored to decryption_dir.

        Args:
            file_path (_type_): Path of file to decrypt.
            key (_type_): _description_
        """
        pass
    