from KeyManager import KeyManager
from CEManager import CEManager
from NoCompressionStrategy import NoCompressionStrategy
from GPGEncryptionStrategy import GPGEncryptionStrategy
from GPGKeyStrategy import GPGKeyStrategy
import os
from ..utils.Logger import logger

gpgkeystrategy = GPGKeyStrategy(os.path.expanduser('~/.gnupg'))
keyManager = KeyManager(gpgkeystrategy)
ceManager = CEManager(NoCompressionStrategy(), GPGEncryptionStrategy())

print(ceManager.compress("test.txt"))
print(ceManager.encrypt("test.txt", keyManager.get_key()))
