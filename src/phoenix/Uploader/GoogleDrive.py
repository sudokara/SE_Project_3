# google_drive_upload.py
from Strategy import UploadDownloadStrategy
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.http import MediaIoBaseDownload
import os
import io
import pandas as pd

# PATH_TO_CREDENTIALS = '/home/prakhar/Desktop/3-2/Software Engineering/Projects/SE_Project_3/src/Uploader/credentials.json'


class GoogleDrive(UploadDownloadStrategy):
    def __init__(self, folder_id) -> None:
        super().__init__()
        self._folder_id = folder_id
        self._service = self._get_service()

    def get_name(self) -> str:
        return "Google Drive"

    def upload(self, file_path: str) -> None:
        print(f"Uploading file to Google Drive: {file_path}")
        self._gdrive_file_upload(file_path, self._folder_id)

    def download(self, file_path: str, file_id) -> None:
        print(f"Downloading file from Google Drive: {file_path}")
        self._gdrive_file_download(file_path, file_id)

    def _gdrive_file_upload(self, filename, gdrive_folder_id):
        # File to upload
        file_metadata = {'name': filename, 'parents': [gdrive_folder_id]}
        media = MediaFileUpload(filename, mimetype='application/zip')
        file = self._service.files().create(body=file_metadata,
                                      media_body=media,
                                      fields='id').execute()
        file_id = file.get('id')
        
        new_data = pd.DataFrame({'File Name': [filename], 'File ID': [file_id], 'time': [pd.Timestamp.now()]})
        
        csv_file = 'log.csv'

        # Check if the file exists
        if not os.path.exists(csv_file):
            new_data.to_csv(csv_file, index=False)
        else:
            new_data.to_csv(csv_file, mode='a', header=False, index=False)
        

        # df = pd.DataFrame(columns=['File Name', 'File ID', 'time'])
        # print(filename, file_id, pd.Timestamp.now())

        # df = pd.concat([df, pd.DataFrame({'File Name': [filename], 'File ID': [file_id], 'time': [pd.Timestamp.now()]})], ignore_index=True)
        
        return file.get('id')

    def _gdrive_file_download(self, file_path, file_id):
        request = self._service.files().get_media(fileId=file_id)

        # Replace 'filename' with the path where you want to save the downloaded file
        fh = io.FileIO(file_path, mode='wb')
        downloader = MediaIoBaseDownload(fh, request)

        done = False
        while not done:
            status, done = downloader.next_chunk()
            print("Download Progress: {0}".format(status.progress() * 100))

        fh.close()
        print("File has been downloaded successfully.")

    def _get_service(self):
        SCOPES = ['https://www.googleapis.com/auth/drive.file']

        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first time.
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        service = build('drive', 'v3', credentials=creds)
        return service
