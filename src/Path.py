import os

class path:
    def __init__(self) -> None:
        self.paths = []
        
    def add(self, state):
        self.paths.append(state)
        
    def get(self):
        return self.paths
    
    def get_all_files(self):
        files = []
        for r, d, f in os.walk(self.paths[0]):
            for folder in d:
                files.append(os.path.join(r, folder))
        return files
    