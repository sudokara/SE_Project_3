# Compression and Encryption Subsystem

## Compression
- A strategy design pattern is used to switch between compression algorithms. The `TarCompressionStrategy` class defines the concrete strategy. A `NoCompressionStrategy` class is also provided, but should not be used when backing up folders since we abstract folders into a compressed file from this stage on which the `NoCompressionStrategy` does not use.  
- The `ICompressionStrategy` interface is to be implemented by all compression strategies. It contains `compress` and `decompress` functions along with an initalization for the output directories for each. The default output structure is:  
```
.phnx
├── compressed
├── decompressed
├── decrypted
└── encrypted
```
in the directory where the script is run.  
> [!WARNING]  
> When compressing a folder, use `folder_name` to add the folder with its contents to the compressed file or `folder_name/` to compress only its contents.

## Encryption
- A strategy design pattern is used to switch between encryption algorithms. The `IEncryptionStrategy` interface is to be implemented by encryption strategies. It contains `encrypt` and `decrypt` methods along with an initialization for output directories, as mentioned in the compression section.
- A singleton design pattern is used to generate and manage the encryption key, defined in `KeyManager` which uses `SingletonMeta` metaclass, an implementation of the singleton pattern. Encryption algorithms might have differing implementations for this, so we also introduce a strategy design pattern in `IKeyStrategy`. 
- We use GPG to perform encryption. The concrete strategy for `IEncryptionStrategy` is `GPGEncryptionStrategy`. The concrete strategy for `IKeyStrategy` is `GPGKeyStrategy`. Also, we need to ensure a single `gpg` object is used across encryption and key management. A singleton `GPGSingleton.py` is used to initialize gpg with desired config.

## Manager
The `CEManager` owns the compression and encryption strategy that will be used. It is the context class for the strategy pattern for both compression and encryption algorithms. It abstracts away the use of the key manager from the caller.