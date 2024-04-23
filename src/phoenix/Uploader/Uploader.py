# uploader.py
from __future__ import annotations
from abc import ABC
from Strategy import UploadDownloadStrategy


class Uploader():
    """
    The Uploader defines the interface of interest to clients.
    """

    def __init__(self, strategy: UploadDownloadStrategy) -> None:
        """
        Usually, the Uploader accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """

        self._strategy = strategy

# getter and setter for strategy
    @property
    def strategy(self) -> UploadDownloadStrategy:
        """
        The Uploader maintains a reference to one of the UploadStrategy objects. The
        Uploader does not know the concrete class of a strategy. It should work
        with all strategies via the UploadStrategy interface.
        """
        
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: UploadDownloadStrategy) -> None:
        """
        Usually, the Uploader allows replacing an UploadStrategy object at runtime.
        """
        if strategy is None:
            raise ValueError("Strategy cannot be None. Please provide a valid strategy.")

        self._strategy = strategy

# upload and download file

    def upload_file(self, file_path: str) -> None:
        """
        The Uploader delegates file uploading to the UploadStrategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        print(f"Uploader: Uploading file to {self._strategy.get_name()}")
        self._strategy.upload(file_path)


    def download_file(self, file_path: str, **kwargs) -> None:
        """
        The Uploader delegates file downloading to the UploadStrategy object instead of
        implementing multiple versions of the algorithm on its own.
        """

        print(f"Uploader: Downloading file from {self._strategy.get_name()}")
        self._strategy.download(file_path, kwargs['file_id'])