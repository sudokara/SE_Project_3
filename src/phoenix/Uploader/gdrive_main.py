# main.py
from Uploader import Uploader
from GoogleDrive import GoogleDrive
from OneDrive import OneDrive
import pandas as pd

GDRIVE_FOLDER_ID = '1MGrdDt2S588h7BZhD2fxr-1WwySf8fwP'

if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the uploader.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.
    
    

    gdrive = Uploader(GoogleDrive(GDRIVE_FOLDER_ID))
    # print("Client: Uploader is set to upload to Google Drive.")
    # uploader.upload_file("/home/prakhar/Desktop/3-2/Software Engineering/Projects/SE_Project_3/src/Uploader/abc.zip")

    # Read a row from the CSV file named log.csv
    df = pd.read_csv('log.csv')
    row = df.iloc[0]  # Select the first row

    # Rest of the code
    gdrive = Uploader(GoogleDrive(GDRIVE_FOLDER_ID))
    gdrive.download_file(file_path = df['File Name'][0], file_id = df['File ID'][0])
    # print("Client: Uploader is set to upload to OneDrive.")
    # uploader = Uploader(OneDrive())
    # uploader.upload_file("/path/to/another/file")

    # uploader.download_file("/path/to/another/file")

    
    # # Also you can directly change the strategy at runtime.
    # uploader.strategy = GoogleDrive()
    # print("Client: Uploader is set to upload to Google Drive.")
    # uploader.upload_file("/path/to/file")

    # uploader.download_file("/path/to/file")

