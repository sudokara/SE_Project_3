from ICompressionStrategy import ICompressionStrategy

class NoCompressionStrategy(ICompressionStrategy):
    def compress(self, file_path, *args, **kwargs):
        return file_path

    def decompress(self, file_path, *args, **kwargs):
        return file_path
