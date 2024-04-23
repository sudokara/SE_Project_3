import sys

from phoenix.Path import Path
from phoenix.Observation.EventDrivenStrategy import EventDrivenStrategy

if __name__ == '__main__':
    print("main")

    watchDir = sys.argv[1]
    pathObj = Path(watchDir)

    print("Files: ", pathObj.files)
    print("Folders: ", pathObj.folders)
    print("Paths: ", pathObj.paths)
    print()
    
    strategy = EventDrivenStrategy()
    strategy.start(pathObj)