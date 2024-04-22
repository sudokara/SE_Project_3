from .ObservationStrategy import ObservationStrategy
import os
import sys

sys.path.append("..")
from Path import Path
import pyinotify
from .EventHandler import EventHandler


class EventDrivenStrategy(ObservationStrategy):

    def __init__(self):
        self.wm = pyinotify.WatchManager()
        self.mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_MODIFY | pyinotify.IN_MOVED_FROM | pyinotify.IN_MOVED_TO
        
        self.handler = EventHandler()

        self.notifier = pyinotify.Notifier(self.wm, self.handler)

    def observe(self):
        for path in self.state.paths:
            self.wm.add_watch(path, self.mask, rec=False, auto_add=True)


    def start(self, state:Path):
        if state is None:
            print("No path given")
            sys.exit(1)
        self.state = state

        self.observe()
        self.notifier.loop()


    def add_watch(self, path):
        self.wm.add_watch(path, self.mask, rec=False, auto_add=True)


    def remove_watch(self, path):
        wd = self.wm.get_wd_by_path(path)
        if wd:
            self.wm.rm_watch(wd)

    def stop(self):
        self.notifier.stop()
        # sys.exit(0)
        # for path in self.state.paths:
        #     self.remove_watch(path)
