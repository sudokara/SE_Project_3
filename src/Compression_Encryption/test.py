from KeyManager import KeyManager
from CEManager import CEManager
from NoCompressionStrategy import NoCompressionStrategy
from GPGEncryptionStrategy import GPGEncryptionStrategy
from GPGKeyStrategy import GPGKeyStrategy
from TarCompressionStrategy import TarCompressionStrategy
import os

gpgkeystrategy = GPGKeyStrategy(os.path.expanduser('~/.gnupg'))
keyManager = KeyManager(gpgkeystrategy)
ceManager = CEManager(TarCompressionStrategy(), GPGEncryptionStrategy(), keyManager)

compressed_file_path = ceManager.compress("test", False)
# encrypted_file_path = ceManager.encrypt(compressed_file_path, keyManager.get_key())
# decrypted_file_path = ceManager.decrypt(encrypted_file_path, keyManager.get_key())
# ceManager.decompress(decrypted_file_path)