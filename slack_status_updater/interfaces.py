from abc import ABC, abstractmethod

class StatusUpdater(ABC):
    @abstractmethod
    def update_status(self, text: str, emoji: str, expiration: int = 0) -> None:
        """Update the status"""
        pass