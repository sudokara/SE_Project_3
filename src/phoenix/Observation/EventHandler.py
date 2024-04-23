import pyinotify
import difflib
import os

from WatchDirStructure.WatchDirComposite import WatchDirComposite
from WatchDirStructure.WatchDirLeaf import WatchDirLeaf
from phoenix.utils.Broker import Broker

class EventHandler(pyinotify.ProcessEvent):

    def __init__(self):
        super().__init__()

    def backup(self, absolutePath):

        if os.path.isdir(absolutePath):
            # print("Backing up directory: ", absolutePath)

            # backup the directory 
            #  function(absolutePath, False)
            Broker().backup(absolutePath, False)

            num_files_backing_up = WatchDirComposite(absolutePath).get_num_files()
            size_backing_up = WatchDirComposite(absolutePath).get_storage_size()

            print("Number of files backing up: ", num_files_backing_up)
            print("Size of files backing up: ", size_backing_up)

        else:
            # print("Backing up file: ", absolutePath)
            
            # backup the file
            # function(absolutePath, True)
            Broker().backup(absolutePath, True)
        
            num_files_backing_up = WatchDirLeaf(absolutePath).get_num_files()
            size_backing_up = WatchDirLeaf(absolutePath).get_storage_size()

            print("Number of files backing up: ", num_files_backing_up)
            print("Size of files backing up: ", size_backing_up)
        

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
        # print("IN_MOVED_FROM: ", event.pathname)
        # self.backup(event.pathname)

        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory)

    def process_IN_MOVED_TO(self, event):
        # print("IN_MOVED_TO: ", event.pathname)
        # self.backup(event.pathname)

        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory)

    def process_IN_CREATE(self, event):
        # print("IN_CREATE: ", event.pathname)

        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory)
            
    def process_IN_DELETE(self, event):
        # print("IN_DELETE: ", event.pathname)
        # self.backup(event.pathname)

        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory)
        
    def process_IN_MODIFY(self, event):
        # print("IN_MODIFY: ", event.pathname)
        self.backup(event.pathname)