# one_drive_upload.py
from Strategy import UploadDownloadStrategy
import requests
from msal import PublicClientApplication
import time
import os
import pandas as pd


class OneDrive(UploadDownloadStrategy):
    def __init__(self, siteName, sites, domain, onedrive_path, client_id, authority) -> None:
        super().__init__()
        self.domain = domain
        self.sites = sites
        self.siteName = siteName
        self.onedrive_path = onedrive_path
        self.token_response = None
        self.client_id = client_id
        self.authority = f"https://login.microsoftonline.com/{authority}"
        self.app = PublicClientApplication(
            client_id=self.client_id, authority=self.authority)

    def get_name(self) -> str:
        return "OneDrive"

    def upload(self, file_path: str) -> None:
        # print(f"Uploading file to OneDrive: {file_path}")
        self._onedrive_file_upload(file_path)

    def download(self, filename: str) -> None:
        # print(f"Downloading file from OneDrive: {file_path}")
        self._onedrive_file_download(filename)

    def getEndpoint(self, access_token, domain, sites, siteName, path):

        # Assuming you have an access token
        headers = {
            "Authorization": access_token
        }

        # Get site by URL
        URL = f"https://graph.microsoft.com/v1.0/sites/{domain}.sharepoint.com:/{sites}/{siteName}"
        site_response = requests.get(URL, headers=headers)
        site_id = site_response.json().get('id')

        # Get default drive of the site
        drive_response = requests.get(
            f'https://graph.microsoft.com/v1.0/sites/{site_id}/drive',
            headers=headers
        )
        drive_id = drive_response.json().get('id')

        # print("Site ID:", site_id)
        # print("Drive ID:", drive_id)
        endpoint = f"https://graph.microsoft.com/v1.0/sites/{site_id}/drives/{drive_id}/root:/{path}:/content"

        return endpoint

    def _onedrive_file_upload(self, localFile):
        if self.token_response is None or self._token_is_expired(self.token_response):
            self.token_response = self._get_new_token()
        if "access_token" in self.token_response:
            access_token = self.token_response['access_token']

            filename = os.path.basename(localFile)
            time_filename = pd.Timestamp.now().strftime('%Y-%m-%d_%H-%M-%S') + '_' + filename
            path = os.path.join(self.onedrive_path, time_filename)

            endpoint = self.getEndpoint(access_token, self.domain,
                                        self.sites, self.siteName, path)

            headers = {
                "Authorization": "Bearer " + access_token,
                "Content-Type": "application/zip"  # Change according to your file type
            }

            # Read the file content to upload
            # Modify the file path and mode as needed
            file_content = open(localFile, 'rb').read()

            # Make the HTTP request to upload the file
            response = requests.put(
                endpoint, headers=headers, data=file_content)

            if response.status_code == 201:
                print("File uploaded successfully.")
                # print(response.json())
                # Log the uploaded file in the CSV
                df = pd.DataFrame({'File Name': [filename], 'Time Stamp File Name': [
                                  time_filename], 'time': [pd.Timestamp.now()]})
                csv_file = 'onedrive_log.csv'
                if not os.path.exists(csv_file):
                    df.to_csv(csv_file, index=False)
                else:
                    df.to_csv(csv_file, mode='a', header=False, index=False)
            elif response.status_code == 200:
                print("Failed to upload file. File already exists.")
            else:
                print("Failed to upload file.")
                print(response.status_code, response.text)
        else:
            print("Failed to obtain token.")
            print(self.token_response.get("error"),
                  self.token_response.get("error_description"))

    def _onedrive_file_download(self, filename):
        if self.token_response is None or self._token_is_expired(self.token_response):
            self.token_response = self._get_new_token()
        if "access_token" in self.token_response:
            access_token = self.token_response['access_token']

            # Build the endpoint for downloading the file from OneDrive
            endpoint = f"https://graph.microsoft.com/v1.0/me/drive/root:/{os.path.join(self.onedrive_path, filename)}:/content"

            headers = {
                "Authorization": "Bearer " + access_token,
            }

            # Make the HTTP request to download the file
            response = requests.get(endpoint, headers=headers, stream=True)

            if response.status_code == 200:
                # Save the downloaded content to a file
                with open(filename, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                print("File downloaded successfully.")
            else:
                print("Failed to download file.")
                print(response.status_code, response.text)
        else:
            print("Failed to obtain token.")
            print(self.token_response.get("error"),
                  self.token_response.get("error_description"))

    def _token_is_expired(self, token_response):
        return time.time() > token_response['expires_at']

    def _get_new_token(self):
        scopes = ["Files.ReadWrite", "User.Read", "Files.ReadWrite.All"]
        token_response = self.app.acquire_token_interactive(scopes=scopes)
        token_response['expires_at'] = time.time() + \
            token_response['expires_in']
        return token_response
