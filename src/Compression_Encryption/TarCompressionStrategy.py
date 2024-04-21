from ICompressionStrategy import ICompressionStrategy
import tarfile
import os
import shutil

class TarCompressionStrategy(ICompressionStrategy):
    """
    Uses the tarfile module to compress and decompress files.
    """
    def compress(self, file_path, *args, **kwargs):
        output_file_name = os.path.join(self.compression_dir, os.path.normpath(file_path) + ".tar.gz")
        with tarfile.open(output_file_name, "w:gz") as tar:
            tar.add(file_path, arcname=os.path.basename(file_path))
        return output_file_name

    def decompress(self, file_path, *args, **kwargs):
        shutil.unpack_archive(file_path, self.decompression_dir)
        return os.path.join(self.decompression_dir, os.path.basename(file_path).replace(".tar.gz", ""))
