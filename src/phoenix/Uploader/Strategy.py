from __future__ import annotations
from abc import ABC, abstractmethod


class UploadDownloadStrategy(ABC):
    """
    The UploadStrategy interface declares operations common to all supported upload strategies.
    """
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def upload(self, file_path: str) -> None:
        pass
    @abstractmethod
    def download(self, file_path: str) -> None:
        pass
