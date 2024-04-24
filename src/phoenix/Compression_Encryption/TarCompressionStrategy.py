from phoenix.Compression_Encryption.ICompressionStrategy import ICompressionStrategy
import tarfile
import os
import shutil

class TarCompressionStrategy(ICompressionStrategy):
    """
    Uses the tarfile module to compress and decompress files.
    """
    def compress(self, file_path, *args, **kwargs):
        if args and not args[0]:
            output_file_names = []

            for root, dirs, files in os.walk(os.path.normpath(file_path)):
                for file in files:
                    input_file_name = os.path.join(root, file)
                    output_file_name = os.path.join(self.compression_dir + "/" + f"{root}-{file}.tar.gz".replace("/", "-"))
                    output_file_names.append(output_file_name)
                    with tarfile.open(output_file_name, "w:gz") as tar:
                        tar.add(input_file_name, arcname=input_file_name.replace("/", "-"))

            return output_file_names
        else:
            output_file_name = os.path.join(self.compression_dir + f"/{file_path.replace('/', '-')}.tar.gz")
            with tarfile.open(output_file_name, "w:gz") as tar:
                tar.add(file_path, arcname=os.path.basename(file_path))
            return output_file_name

    def decompress(self, file_path, *args, **kwargs):
        output_filename = os.path.join(self.decompression_dir, os.path.basename(file_path).replace(".tar.gz", ""))
        shutil.unpack_archive(file_path, self.decompression_dir)
        return output_filename
