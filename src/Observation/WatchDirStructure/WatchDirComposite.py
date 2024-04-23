import os
from .WatchDirComponent import WatchDirComponent
from .WatchDirLeaf import WatchDirLeaf

class WatchDirComposite(WatchDirComponent):

    def __init__(self, path):
        self.path = path
        self.contents = []
        self._populate_contents()
        self.dirname = os.path.basename(self.path)

    def _populate_contents(self):

        for item in os.listdir(self.path):
            item_path = os.path.join(self.path, item)
            if os.path.isfile(item_path):
                self.contents.append(WatchDirLeaf(item_path))
            elif os.path.isdir(item_path):
                self.contents.append(WatchDirComposite(item_path))

    def get_num_files(self):
        num_files = 0
        for item in self.contents:
            num_files += item.get_num_files()
        return num_files

    def get_storage_size(self):
        total_size = 0
        for item in self.contents:
            total_size += item.get_storage_size()
        return total_size