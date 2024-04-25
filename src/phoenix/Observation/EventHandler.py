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

class EventHandler(pyinotify.ProcessEvent):

    def __init__(self):
        super().__init__()

    def _get_cloud_provider(self):
        
        with open("../config.json") as f:
            config = json.load(f)
        
        if config['cloud-provider'] == "gdrive":
            return GoogleDrive(config['gdrive-folder-id'])
        else:

            with open("../Uploader/onedrive_credentials.json") as f:
                onedrive_config = json.load(f)

            return OneDrive(siteName=onedrive_config['siteName'], sites=onedrive_config['sites'], domain=onedrive_config['domain'], onedrive_path=onedrive_config['onedrive_path'], client_id=onedrive_config['client_id'], authority=onedrive_config['authority'])
            

    def backup(self, absolutePath, maskname):

        logger.info(f"Event: {maskname} Path: {absolutePath}")

        uploadDownloadStrategy = self._get_cloud_provider()

        if os.path.isdir(absolutePath):

            try:
                broker = Broker(uploadDownloadStrategy=uploadDownloadStrategy)
                broker.backup(absolutePath, False)
            except Exception as e:
                print("Exception: ", e)

            num_files_backing_up = WatchDirComposite(absolutePath).get_num_files()
            size_backing_up = WatchDirComposite(absolutePath).get_size()

        else:

            try:
                broker = Broker(uploadDownloadStrategy=uploadDownloadStrategy)
                broker.backup(absolutePath, True)
            except Exception as e:
                print("Exception: ", e)
        
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