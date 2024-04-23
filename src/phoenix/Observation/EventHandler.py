import pyinotify
import difflib
import os
import pandas as pd

from phoenix.Observation.WatchDirStructure.WatchDirComposite import WatchDirComposite
from phoenix.Observation.WatchDirStructure.WatchDirLeaf import WatchDirLeaf
from phoenix.utils.Broker import Broker

class EventHandler(pyinotify.ProcessEvent):

    def __init__(self):
        super().__init__()

    def backup(self, absolutePath, maskname):

        if os.path.isdir(absolutePath):
            broker = Broker()
            encrypted_path = broker.backup(absolutePath, False)

            num_files_backing_up = WatchDirComposite(absolutePath).get_num_files()
            size_backing_up = WatchDirComposite(absolutePath).get_size()

        else:
            print(maskname)

            try:
                broker = Broker()
                encrypted_path = broker.backup(absolutePath, True)
            except Exception as e:
                print("Exception: ", e)
        
            num_files_backing_up = WatchDirLeaf(absolutePath).get_num_files()
            size_backing_up = WatchDirLeaf(absolutePath).get_size()
        

        new_data = pd.DataFrame({'Event Name': [maskname], 'Event Path': [absolutePath], 'No. of Files Backing Up': [num_files_backing_up], 'Size of Backup': [size_backing_up], 'Time': [pd.Timestamp.now()]})
    
        csv_file = 'log.csv'

        # Check if the file exists
        if not os.path.exists(csv_file):
            new_data.to_csv(csv_file, index=False)
        else:
            new_data.to_csv(csv_file, mode='a', header=False, index=False)
        

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
        self.backup(parent_directory, "IN_MOVED_FROM")

    def process_IN_MOVED_TO(self, event):
        # print("IN_MOVED_TO: ", event.pathname)
        # self.backup(event.pathname)

        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory, "IN_MOVED_TO")

    def process_IN_CREATE(self, event):
        # print("IN_CREATE: ", event.pathname)

        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory, "IN_CREATE")
            
    def process_IN_DELETE(self, event):
        # print("IN_DELETE: ", event.pathname)
        # self.backup(event.pathname)

        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory, "IN_DELETE")
        
    def process_IN_MODIFY(self, event):
        # print("IN_MODIFY: ", event.pathname)
        self.backup(event.pathname, "IN_MODIFY")