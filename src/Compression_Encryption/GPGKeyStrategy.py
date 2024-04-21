from IKeyStrategy import IKeyStrategy
import gnupg
import subprocess

class GPGKeyStrategy(IKeyStrategy):
    """
    The GPGKeyStrategy class is a concrete implementation of the IKeyStrategy interface that generates and retrieves
    GPG keys.
    """
    def __init__(self, gpghome:str=None):
        if gpghome:
            self.__gpg = gnupg.GPG(gnupghome=gpghome)
        else:
            self.__gpg = gnupg.GPG()

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