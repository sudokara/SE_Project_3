import pyinotify
import difflib
import os
import pandas as pd
import json

from phoenix.Uploader.OneDrive import OneDrive
from phoenix.Uploader.GoogleDrive import GoogleDrive
from phoenix.Observation.WatchDirStructure.WatchDirComposite import WatchDirComposite
from phoenix.Observation.WatchDirStructure.WatchDirLeaf import WatchDirLeaf
from phoenix.utils.Broker import Broker
from phoenix.utils.Logger import logger
import requests
from datetime import datetime

class EventHandler(pyinotify.ProcessEvent):

    def __init__(self):
        super().__init__()

    def backup(self, absolutePath, maskname):

        logger.info(f"Event: {maskname} Path: {absolutePath}")

        # data = {
        #     'absolutePath': absolutePath,
        #     'is_file': os.path.isfile(absolutePath),
        # }
        # try:
        #     response = requests.post('http://localhost:5000/encrypt-compress', data=data)
        # except Exception as e:
        #     print(f"Exception: {e}")

        url = "http://localhost:5000/encrypt-compress"
        headers = {
            "content-type": "application/json"
        }
        data = {
            "absolutePath": absolutePath,
            "is_file": os.path.isfile(absolutePath)
        }

        response = requests.post(url, headers=headers, json=data)


        if os.path.isdir(absolutePath):

            num_files_backing_up = WatchDirComposite(absolutePath).get_num_files()
            size_backing_up = WatchDirComposite(absolutePath).get_size()

        else:        
            num_files_backing_up = WatchDirLeaf(absolutePath).get_num_files()
            size_backing_up = WatchDirLeaf(absolutePath).get_size()
        

        new_data = pd.DataFrame({'Event Name': [maskname], 'Event Path': [absolutePath], 'No. of Files Backing Up': [num_files_backing_up], 'Size of Backup': [size_backing_up], 'Time': [pd.Timestamp.now()]})
    
        csv_file = 'log.csv'

        if not os.path.exists(csv_file):
            new_data.to_csv(csv_file, index=False)
        else:
            new_data.to_csv(csv_file, mode='a', header=False, index=False)

        logger.info(f"Number of files backing up: {num_files_backing_up}, Size of backup: {size_backing_up}")
        logger.info(f"Backup completed!")

        with open("../../../microservice_benchmarking/backup_time.txt", "a") as f:
            f.write(f"{datetime.now()}\n")
        

    def process_IN_MOVED_FROM(self, event):
        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory, "IN_MOVED_FROM")

    def process_IN_MOVED_TO(self, event):
        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory, "IN_MOVED_TO")

    def process_IN_CREATE(self, event):
        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory, "IN_CREATE")
            
    def process_IN_DELETE(self, event):
        parent_directory = os.path.dirname(event.pathname)
        self.backup(parent_directory, "IN_DELETE")
        
    def process_IN_MODIFY(self, event):
        self.backup(event.pathname, "IN_MODIFY")