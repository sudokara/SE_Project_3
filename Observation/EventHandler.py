import pyinotify
import difflib
import os

class EventHandler(pyinotify.ProcessEvent):

    def __init__(self):
        super().__init__()

    def backup(self, absolutePath):

        if os.path.isdir(absolutePath):
            print("Backing up directory: ", absolutePath)

            # backup the directory 
            #  function(absolutePath, False)
        else:
            print("Backing up file: ", absolutePath)
            
            # backup the file
            # function(absolutePath, True)
        

    # def check_diff(self, file):
    #     print("Checking diff for file: ", file)
    #     file2 = file # get the file from the backup
    #     with open(file, 'r') as file1:
    #         file1_lines = file1.readlines()
    #     with open(file2, 'r') as file2:
    #         file2_lines = file2.readlines()
        
    #     diff = difflib.unified_diff(file1_lines, file2_lines, fromfile=file, tofile=file2)
    #     return any(diff)
        

    def process_IN_MOVED_FROM(self, event):
        print("IN_MOVED_FROM: ", event.pathname)
        self.backup(event.pathname)

    def process_IN_MOVED_TO(self, event):
        print("IN_MOVED_TO: ", event.pathname)
        self.backup(event.pathname)

    def process_IN_CREATE(self, event):
        print("IN_CREATE: ", event.pathname)
        self.backup(event.pathname)
            
    def process_IN_DELETE(self, event):
        print("IN_DELETE: ", event.pathname)
        self.backup(event.pathname)
        
    def process_IN_MODIFY(self, event):
        print("IN_MODIFY: ", event.pathname)
        self.backup(event.pathname)