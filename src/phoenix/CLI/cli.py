import json
import threading
import time
import os
import subprocess
import sys
from multiprocessing import Process
import pandas as pd


sys.path.append('..')
from phoenix.utils.Broker import Broker
from phoenix.Uploader.GoogleDrive import GoogleDrive
from phoenix.Observation.OManager import OManager
from phoenix.Observation.ObservationStrategy import ObservationStrategy
from phoenix.Observation.EventDrivenStrategy import EventDrivenStrategy
from phoenix.Observation.PeriodicStrategy import PeriodicStrategy
from Path import Path

BOLD1 = "\033[1m"
BOLD2 = "\033[0m"

class CLI:
    def __init__(self):        
        with open('../config.json', 'r') as f:
            self.config = json.load(f)
            
        # self.strategy = EventDrivenStrategy() if self.config["strategy"] == "event-driven" else PeriodicStrategy()
        self.__oManager = OManager(PeriodicStrategy() if self.config["strategy"] == "periodic" else EventDrivenStrategy())
        self.drive = self.config["cloud-provider"]
        self.state = Path(self.config["watch-directories"])
        self.backup = False
        self.process = None
        
        
    def update_config(self):
        with open('../config.json', 'w') as f:
            json.dump(self.config, f)
        
    def process_command(self):
        command = input("-> ")
        
        if command == 'gen-gpg-key':
            self.generate_gpg_keys()

        elif command == 'backup-strategy --event-driven':
            self.set_observation_startegy(EventDrivenStrategy())

        elif command == 'backup-strategy --periodic':
            self.set_observation_startegy(PeriodicStrategy())

        elif command == 'cloud-provider --gdrive':
            self.choose_cloud_provider('gdrive')

        elif command == 'cloud-provider --onedrive':
            self.choose_cloud_provider('onedrive')

        elif command == 'gdrive-cred':
            self.gdrive_credentials()

        elif command == 'onedrive-cred':
            self.onedrive_credentials()

        elif command == 'restore --gdrive':
            self.gdrive_restore()

        elif command == 'restore --onedrive':
            self.onedrive_restore()

        elif command == 'add-wd':
            self.add_watch_directory()
            
        elif command == 'rm-wd':
            self.remove_watch_directory()
            
        elif command == 'get-wd':
            self.get_watch_directories()

        elif command == 'start':
            self.start_observing()

        elif command == 'stop':
            self.stop_observing()

        elif command == 'exit':
            self.exit_phoenix()

        else:
            print("Invalid command. Please try again.")
            return


    def generate_gpg_keys(self):

        if self.backup is True:
            print("Stop backup before configuration")
            return
    
        try:
            result = subprocess.run("gpg --full-generate-key", shell=True, capture_output=True, text=True)
            
            if result.returncode == 0:
                print("Generated GPG key successfully.")
                print("Please remember to save your key.")
            else:
                print("Error generating GPG key")
                print(result.stderr)
                
        except Exception as e:
            print("Error:", e)
            

    def gdrive_credentials(self):

        if self.backup is True:
            print("Stop backup before configuration")
            return
        
        info = True if input("Do you need guidance to get Google Drive credentials? (y/n)") == 'y' else False
            
        if info:
            steps = [
                "1. Go to the Google Cloud Console and create a new project.",
                "2. Enable the Google Drive API for the newly created project.",
                "3. Set up the consent screen:",
                "   > Choose the user type as 'External'.",
                "   > Enter your app name, support email, and developer contact information.",
                "   > Click on 'Save and Continue'.",
                "4. Configure scopes for Google APIs:",
                "   > Click on 'Save and Continue'.",
                "5. Configure test users (if required):",
                "   > Click on 'Save and Continue'.",
                "6. Navigate to the 'Credentials' section.",
                "7. Click on 'Create Credentials' and choose 'OAuth client ID'.",
                "8. Select 'Desktop app' as the application type.",
                "9. Click on 'Create' and then 'Download' to download the credentials file.",
                "10. Copy the content of the downloaded credentials file and paste it here."
                "11. Create a new folder in your Google Drive and get the folder ID.",
                "12. The folder ID is the last part of the URL when you open the folder in your browser."
            ]
            
            print("\nSteps to generate Credentials JSON")
            for step in steps:
                print(step) 
            print()  
        
        cred = input("Enter the credentials: ")

        try:
            credentials = json.loads(credentials)
            if "installed" not in credentials:
                print("Error: credentials JSON object must contain 'installed' key.")
                return False
            required_keys = ["client_id", "project_id", "auth_uri", "token_uri", "auth_provider_x509_cert_url", "client_secret", "redirect_uris"]
            for key in required_keys:
                if key not in credentials["installed"]:
                    print(f"Error: Missing required key '{key}' in 'installed' object.")

        except json.JSONDecodeError as e:
            print("Error decoding credentials JSON:", e)


        with open('../Uploader/gdrive_credentials.json', 'w') as f:
            json.dump(credentials, f)

        gdrive_folder_id = input("Enter the Google Drive folder ID: ")
        self.config["gdrive-folder-id"] = gdrive_folder_id
        self.update_config()


    def onedrive_credentials(self):

        if self.backup is True:
            print("Stop backup before configuration")
            return
        
        info = True if input("Do you need guidance to get One Drive credentials? (y/n)") == 'y' else False

        if info:
            steps = []

            print("\nSteps to get Credentials")
            for step in steps:
                print(step)
            print()

        domain = input("Enter the domain: ")
        sites = input("Enter sites: ")
        siteName = input("Enter the site name: ")
        onedrive_path = input("Enter the path: ")
        client_id = input("Enter the client id: ")
        authority = input("Enter the authority: ")

        try :
            for i in [domain, sites, siteName, onedrive_path, client_id, authority]:
                if i == "":
                    print("Error: All fields are required")
                    return False
        except Exception as e:
            print("Error:", e)

        cred = {}
        cred["domain"] = domain
        cred["sites"] = sites
        cred["siteName"] = siteName
        cred["onedrive_path"] = onedrive_path
        cred["client_id"] = client_id
        cred["authority"] = authority

        with open('../Uploader/onedrive_credentials.json', 'w') as f:
            json.dump(cred, f)          
    
    
    def set_observation_startegy(self, strategy: ObservationStrategy):

        if self.backup is True:
            print("Stop backup before configuration")
            return
         
        self.config["strategy"] = "event-driven" if isinstance(strategy, EventDrivenStrategy) else "periodic"
        self.__oManager.setObservationStrategy(strategy)



    def choose_cloud_provider(self, drive: str):

        if self.backup is True:
            print("Stop backup before configuration")
            return
        
        self.drive = drive
        self.config['cloud-provider'] = drive
        self.update_config()


    def add_watch_directory(self):
        path = input("Enter path to watch directory: ")
        directories = self.state.get_watch_directories()
        if path not in directories:
            print("Directory added successfully")
            directories.append(path)
        else:
            print("Directory was already added")
        self.state = Path(directories)
        

    def remove_watch_directory(self):
        if self.backup is True:
            print("Stop backup before configuration")
            return
        
        path = input("Enter path to remove from watch directory: ")
        directories = self.state.get_watch_directories()
        if path in directories:
            print("Directory removed successfully")
            directories.remove(path)
        else:
            print("Directory was not found")
        self.state = Path(directories)
        
        
    def get_watch_directories(self):
        dirs = self.state.get_watch_directories()
        print("Directories being watched:")
        for dir in dirs:
            print(BOLD1 + dir + BOLD2)


    def start_observing(self):

        if self.backup == False:

            self.backup = True
            print(BOLD1 + "\nMonitoring has started\n" + BOLD2)
            
            self.__oManager = OManager(PeriodicStrategy() if self.config["strategy"] == "periodic" else EventDrivenStrategy())
            self.process = Process(target=self.__oManager.start, args=(self.state,))
            self.process.start()


    def stop_observing(self):

        self.backup = False
        self.__oManager.stop()
        self.process.terminate()
                
        print(BOLD1 + "\nMonitoring has stopped\n" + BOLD2)


    def gdrive_restore(self):

        csv_file = "../Uploader/gdrive_log.csv"

        df = pd.read_csv(csv_file)
        df.columns = ['File Name', 'File ID', 'Time']
        last_n_rows = df.tail(5)

        print("Last 5 files uploaded to Google Drive:")
        print(last_n_rows)
        idx_str = input("Select the files to restore by entering the row index separated by space: ")
        idx = list(map(int, idx_str.split()))

        print(idx)

        try:
            broker = Broker(GoogleDrive(self.config['gdrive-folder-id']))
        except Exception as e:
            print("Error:", e)
        
        for i in idx:
            file_path = last_n_rows['File Name'][i]
            file_path = file_path.split("/")[2]
            file_path = file_path.replace("-", "/")
            broker.download(file_path, last_n_rows['File ID'][i])


    def restore_onedrive(self):
        pass
        #TODO

    def exit_phoenix(self):
        print(BOLD1 + "\nThank you for using Phoenix!\n" + BOLD2)
        self.update_config()
        if self.backup:
            self.stop_observing()
        sys.exit(0)


def print_startup_info():

    print(BOLD1 + "\nWelcome to Phoenix!" + BOLD2)

    print(BOLD1 + "\nBefore starting the backup, please ensure you have completed the following steps:" + BOLD2)

    print(" * Generated a GPG key pair for encryption and decryption using the " + BOLD1 + 'gen-gpg-key' + BOLD2 + " command (required only once)")
    print(" * Set the backup strategy:")
    print("   - For event-driven backup, use the command " + BOLD1 +  'backup-strategy --event-driven' + BOLD2)
    print("     * Enter your Google Drive credentials using the " + BOLD1 + 'gdrive-cred' + BOLD2 + " command (required only once)")
    print("   - For periodic backup, use the command " + BOLD1 +   'backup-strategy --periodic' + BOLD2)
    print(" * Select the cloud provider to upload to:")
    print("   - For Google Drive, use the command " + BOLD1 +  'cloud-provider --gdrive' + BOLD2)
    print("   - For OneDrive, use the command " + BOLD1 +   'cloud-provider --onedrive' + BOLD2)
    print(" * Add a directory to be watched using the command " + BOLD1 + 'add-wd' + BOLD2)
    
    print(BOLD1 + "\nOnce you have completed these steps, you can start the backing up your files :)" + BOLD2)

    print(" * To start monitoring your files, use the command " + BOLD1 + 'start' + BOLD2)
    print(" * To stop monitoring your files, use the command " + BOLD1 + 'stop' + BOLD2)
    print(" * To exit application, use the command " + BOLD1 + 'exit' + BOLD2)
    print(" * Remove a directory from being watched using the command " + BOLD1 + 'rm-wd' + BOLD2)
    print(" * Get directories being watched using the command " + BOLD1 + 'get-wd' + BOLD2)
    print(" * Restore files from Google Drive using the command " + BOLD1 + 'restore --gdrive' + BOLD2)

    print(BOLD1 + "\nModify Phoenix Configuration at any time by halting the backup process and then utilizing setup commands.\n" + BOLD2)


def main():

    cli = CLI()

    print_startup_info()

    while True:
        try:
            cli.process_command()
        except Exception as e:
            cli.update_config()
            cli.exit_phoenix()
        except KeyboardInterrupt as e:
            cli.update_config()
            cli.exit_phoenix()


if __name__ == '__main__':
    main()
