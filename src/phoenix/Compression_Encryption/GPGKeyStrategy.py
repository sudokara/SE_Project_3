from phoenix.Compression_Encryption.IKeyStrategy import IKeyStrategy
from phoenix.Compression_Encryption.GPGSingleton import GPGSingleton
import gnupg
import subprocess

class GPGKeyStrategy(IKeyStrategy):
    """
    The GPGKeyStrategy class is a concrete implementation of the IKeyStrategy interface that generates and retrieves
    GPG keys.
    """
    def __init__(self, gpghome:str=None):
        if gpghome:
            self.__gpg = GPGSingleton(gpghome).get_gpg()
        else:
            self.__gpg = GPGSingleton().get_gpg()

    def generate_key(self, *args, **kwargs):
        print("Follow the process to generate a gpg key. Use the default if unsure.")
        subprocess.run(["gpg", "--full-generate-key"])

    def get_key(self, *args, **kwargs):
        keys = self.__gpg.list_keys()
        if not keys:
            raise Exception("No keys found.")
        elif args and args[0] < len(keys):
            return keys[args[0]]
        else:
            return keys[0]