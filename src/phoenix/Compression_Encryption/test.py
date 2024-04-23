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

# compressed_file_paths = ceManager.compress("test", False)
# print(compressed_file_paths)
# encrypted_file_paths = [ceManager.encrypt(compressed_file_path, keyManager.get_key()) for compressed_file_path in compressed_file_paths]
# print(encrypted_file_paths)
# decrypted_file_paths = [ceManager.decrypt(encrypted_file_path, keyManager.get_key()) for encrypted_file_path in encrypted_file_paths]
# print(decrypted_file_paths)
# decompressed_file_paths = [ceManager.decompress(decrypted_file_path) for decrypted_file_path in decrypted_file_paths]
# print(decompressed_file_paths)

compressed_file_path = ceManager.compress("test/test2.txt")
encrypted_file_path = ceManager.encrypt(compressed_file_path, keyManager.get_key())
decrypted_file_path = ceManager.decrypt(encrypted_file_path, keyManager.get_key())
print(ceManager.decompress(decrypted_file_path))