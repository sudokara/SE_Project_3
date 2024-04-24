# one_drive_upload.py
from Strategy import UploadDownloadStrategy


class OneDrive(UploadDownloadStrategy):
    def get_name(self) -> str:
        return "OneDrive"

    def upload(self, file_path: str) -> None:
        print(f"Uploading file to OneDrive: {file_path}")

    def download(self, file_path: str) -> None:
        print(f"Downloading file from OneDrive: {file_path}")
