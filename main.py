from Path import Path
import sys
from Observation.EventDrivenStrategy import EventDrivenStrategy

if __name__ == "__main__":
    watchDir = sys.argv[1]
    pathObj = Path(watchDir)

    print("Files: ", pathObj.files)
    print("Folders: ", pathObj.folders)
    print("Paths: ", pathObj.paths)
    print()
    
    strategy = EventDrivenStrategy()
    strategy.start(pathObj)