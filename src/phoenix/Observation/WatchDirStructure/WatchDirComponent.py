from abc import ABC, abstractmethod

class WatchDirComponent(ABC):
    '''
    Get the number of files in the directory
    '''
    @abstractmethod
    def get_num_files(self):
        pass

    '''
    Get the total size of the files in the directory
    '''
    @abstractmethod
    def get_size(self):
        pass
