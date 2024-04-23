from phoenix.Compression_Encryption.IEncryptionStrategy import IEncryptionStrategy
from phoenix.Compression_Encryption.GPGSingleton import GPGSingleton
import os
import getpass

class GPGEncryptionStrategy(IEncryptionStrategy):
    def encrypt(self, file_path, key, *args, **kwargs):
        """
        Encrypts the data using GPG encryption.
        """
        if key is None:
            raise Exception("Key not provided.")
        else:
            output_path = os.path.join(self.encryption_dir, os.path.basename(file_path) + '.gpg')
            with open(file_path, 'rb') as f:
                status = GPGSingleton().get_gpg().encrypt_file(
                    f, recipients=[key['keyid']],
                    # output=file_path + '.gpg',
                    output=output_path,
                    armor=False
                )
            if status.ok:
                print("File encrypted successfully.")
            else:
                print("Encryption failed:", status.stderr)
        return output_path

    def decrypt(self, file_path, key, *args, **kwargs):
        """
        Decrypts the data using GPG decryption.
        """
        if key is None:
            raise Exception("Key not provided.")
        else:
            output_path = os.path.join(self.decryption_dir, os.path.basename(file_path)[:-4])
            with open(file_path, 'rb') as f:
                status = GPGSingleton().get_gpg().decrypt_file(
                    f, passphrase=getpass.getpass("GPG Password: "),
                    output=output_path
                )
            if status.ok:
                print("File decrypted successfully.")
            else:
                print("Decryption failed:", status.stderr)
        
        return output_path