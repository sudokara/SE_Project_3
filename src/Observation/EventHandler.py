import pyinotify
import difflib

class EventHandler(pyinotify.ProcessEvent):

    def backup(self, file):
        print("Backing up file: ", file)
        
    def check_diff(self, file):
        print("Checking diff for file: ", file)
        file2 = file # get the file from the backup
        with open(file, 'r') as file1:
            file1_lines = file1.readlines()
        with open(file2, 'r') as file2:
            file2_lines = file2.readlines()
        
        diff = difflib.unified_diff(file1_lines, file2_lines, fromfile=file, tofile=file2)
        return any(diff)
        
    def process_default(self, event):

        if(self.check_diff(event.pathname)):
            print("File has changed: ", event.pathname)
            self.backup(event.pathname)