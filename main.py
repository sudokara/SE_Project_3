import sys
import subprocess
import pprint

from src.Path import Path
from src.Observation.EventDrivenStrategy import EventDrivenStrategy

if __name__ == "__main__":
    # watchDir = sys.argv[1]
    # pathObj = Path(watchDir)

    # print("Files: ", pathObj.files)
    # print("Folders: ", pathObj.folders)
    # print("Paths: ", pathObj.paths)
    # print()
    
    # strategy = EventDrivenStrategy()
    # strategy.start(pathObj)

    # try:
    #     result = subprocess.run("gpg --full-generate-key", shell=True, capture_output=True, text=True)
        
    #     if result.returncode == 0:
    #         print("Generated GPG key successfully.")
    #         print("Please remember to save your key.")
    #     else:
    #         print("Error generating GPG key")
    #         print(result.stderr)
            
    # except Exception as e:
    #     print("Error:", e)


    # steps = [
    #     "* Go to the Google Cloud Console and create a new project.",
    #     "* Enable the Google Drive API for the newly created project.",
    #     "* Set up the consent screen:",
    #     "   - Choose the user type as 'External'.",
    #     "   - Enter your app name, support email, and developer contact information.",
    #     "   - Click on 'Save and Continue'.",
    #     "* Configure scopes for Google APIs:",
    #     "   - Click on 'Save and Continue'.",
    #     "* Configure test users (if required):",
    #     "   - Click on 'Save and Continue'.",
    #     "* Navigate to the 'Credentials' section.",
    #     "* Click on 'Create Credentials' and choose 'OAuth client ID'.",
    #     "* Select 'Desktop app' as the application type.",
    #     "* Click on 'Create' and then 'Download' to download the credentials file.",
    #     "* Copy the content of the downloaded credentials file and paste it here."
    # ]

    # for step in steps:
    #     print(step)

    BOLD1 = "\033[1m"
    BOLD2 = "\033[0m"

    print(BOLD1 + "\nWelcome to the Phoenix!" + BOLD2)

    print(BOLD1 + "\nBefore starting the backup, please ensure you have completed the following steps:" + BOLD2)

    print(" * Generated a GPG key pair for encryption and decryption using the " + BOLD1 + 'generate-gpg-key' + BOLD2 + " command (required only once)")
    print(" * Entered your Google Drive credentials using the " + BOLD1 + 'enter-gdrive-credentials' + BOLD2 + " command (required only once)")
    print(" * Set the backup strategy:")
    print("   - For event-driven backup, use the command " + BOLD1 +  'set-backup-strategy --event-driven' + BOLD2)
    print("   - For periodic backup, use the command " + BOLD1 +   'set-backup-strategy --periodic' + BOLD2)
    print(" * Select the cloud provider to upload to:")
    print("   - For Google Drive, use the command " + BOLD1 +  'choose-cloud-provider --gdrive' + BOLD2)
    print("   - For OneDrive, use the command " + BOLD1 +   'choose-cloud-provider --onedrive' + BOLD2)
    
    print(BOLD1 + "\nOnce you have completed these steps, you can start the backing up your files :)" + BOLD2)

    print(" * To start monitoring your files use the command " + BOLD1 + 'start-phoenix' + BOLD2)
    print(" * To stop monitoring your files use the command " + BOLD1 + 'stop-phoenix' + BOLD2)

    print(BOLD1 + "\nModify Phoenix Configuration at any time by halting the backup process and then utilizing setup commands.\n" + BOLD2)