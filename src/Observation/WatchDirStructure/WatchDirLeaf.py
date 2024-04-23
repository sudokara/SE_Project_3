import os
from .WatchDirComponent import WatchDirComponent

class WatchDirLeaf(WatchDirComponent):

    def __init__(self, path):
        self.path = path
        self.filename = os.path.basename(self.path)
        self.size = os.path.getsize(self.path)

    def get_num_files(self):
        return 1

    def get_storage_size(self):
        return self.size