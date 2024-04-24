from Uploader import Uploader
from OneDrive import OneDrive
import pandas as pd

DOMAIN = 'iiitaphyd-my'
SITES = 'personal'
SITENAME = 'prakhar_jain_research_iiit_ac_in'
ONEDRIVE_PATH = 'Phoenix Backup System'
CLIENT_ID = 'ea6616ef-72cb-49c3-8d8b-b35324b7f5c4'
AUTHORITY = '031a3bbc-cf7c-4e2b-96ec-867555540a1c'

FILE_PATH = '/home/prakhar/Desktop/3-2/Software Engineering/Projects/SE_Project_3/main.zip'

if __name__ == "__main__":
    onedrive = Uploader(OneDrive(siteName=SITENAME, sites=SITES, domain=DOMAIN, onedrive_path=ONEDRIVE_PATH, client_id=CLIENT_ID, authority=AUTHORITY))
    
    # FILE_TO_UPLOAD = '/home/prakhar/Desktop/3-2/Software Engineering/Projects/SE_Project_3/main.zip'
    # onedrive.upload_file(FILE_TO_UPLOAD)
    
    # now download the file using the onedrive_log.csv

    # read the file onedrive_log.csv
    
    df = pd.read_csv('onedrive_log.csv')
    row = df.iloc[0]  # Select the first row

        
        # process the data as needed
    onedrive.download_file(row["Time Stamp File Name"])