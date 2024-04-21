from IEncryptionStrategy import IEncryptionStrategy
import gnupg

class GPGEncryptionStrategy(IEncryptionStrategy):
    def encrypt(self, file_path, key, *args, **kwargs):
        """
        Encrypts the data using GPG encryption.
        """
        if key is None:
            raise Exception("Key not provided.")
        else:
            with open(file_path, 'rb') as f:
                status = gpg.encrypt_file(
                    f, recipients=[key_id],
                    output=file_path + '.gpg',
                    armor=False
                )
            if status.ok:
                print("File encrypted successfully.")
            else:
                print("Encryption failed:", status.stderr)
        return file_path

    def decrypt(self, file_path, key, *args, **kwargs):
        """
        Decrypts the data using GPG decryption.
        """
        print("Decrypting data using GPG decryption...")
        return file_path