from phoenix.utils.SingletonMeta import SingletonMeta
import gnupg

class GPGSingleton(metaclass=SingletonMeta):
    def __init__(self, gpg_home:str=None):
        if gpg_home:
            self.gpg = gnupg.GPG(gnupghome=gpg_home)
        else:
            self.gpg = gnupg.GPG()
    
    def get_gpg(self):
        return self.gpg
