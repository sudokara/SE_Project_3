from ObservationStrategy import ObservationStrategy
from .. import Path
import os
import sys
import pyinotify
from EventHandler import EventHandler

class EventDrivenStrategy(ObservationStrategy):

    def __init__(self):
        self.wm = pyinotify.WatchManager()
        self.mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY | pyinotify.IN_MOVED_TO

        self.handler = EventHandler()

        self.notifier = pyinotify.Notifier(self.wm, self.handler)

    def observe(self, state:Path):

        for path in state.paths:
            self.wm.add_watch(path, self.mask, rec=True, auto_add=True)

    def start(self):
        self.notifier.loop()

    def stop(self):
        self.notifier.stop()
        self.wm.rm_watch(self.wm.get_wd_by_path(self.handler.path))
