import os
    
class Path:
    def __init__(self, watch_directory):
        self.watch_directory = watch_directory # array of directories to watch
        self.files = self.get_all_files()
        self.folders = self.get_all_folders()
        self.paths = self.folders + self.files
    
    def get_all_files(self): 
        files_list = []
        for directory in self.watch_directory:
            for root, dirs, files in os.walk(directory):
                for f in files:
                    files_list.append(os.path.join(root, f))
        return files_list
        
    
    def get_all_folders(self):
        folders = []
        for directory in self.watch_directory:
            for root, dirs, files in os.walk(directory):
                for d in dirs:
                    folders.append(os.path.join(root, d))

        folders.append(self.watch_directory)
        return folders
    
    def get_all_paths(self):
        return self.get_all_folders() + self.get_all_files()    
    
    def get(self):
        return self.paths

    def get_watch_directories(self):
        return self.watch_directory