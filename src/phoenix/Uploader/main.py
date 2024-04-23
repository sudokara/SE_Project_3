# main.py
from Uploader import Uploader
from GoogleDrive import GoogleDrive
from OneDrive import OneDrive

if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the uploader.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    uploader = Uploader(GoogleDrive())
    print("Client: Uploader is set to upload to Google Drive.")
    uploader.upload_file("/path/to/file")


    uploader.download_file("/path/to/file")

    print("Client: Uploader is set to upload to OneDrive.")
    uploader = Uploader(OneDrive())
    uploader.upload_file("/path/to/another/file")

    uploader.download_file("/path/to/another/file")

    
    # Also you can directly change the strategy at runtime.
    uploader.strategy = GoogleDrive()
    print("Client: Uploader is set to upload to Google Drive.")
    uploader.upload_file("/path/to/file")

    uploader.download_file("/path/to/file")

