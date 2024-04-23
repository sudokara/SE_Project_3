# Observation Subsystem

## Observation
- A strategy design pattern is used to switch between observation algorithms. The `ObservationStrategy` interface is to be implemented by observation strategies. It contains `start` and `stop` method and require a `Path` object for the directory being observed.
- The `EventDrivenStrategy` and `PeriodicStrategy` are the concrete strategies for `ObservationStrategy`. 
- The `EventDrivenStrategy` observes the directories of interest for any event (the events defined are `created`, `modified`, `deleted`, `moved`). Upon an event, the strategy triggers a call to the event handler which will initiate the file backup. It uses `inotify` API for monitoring filesystem events.
- The `PeriodicStrategy` periodically triggers a call to the event handler for file backup.

## Event Handler
- The `EventHandler` class is responsible for handling the events triggered by the observation strategies. It initiates the backup process for the files that have been changed. Depending on the type of event received, it either initiates the backup for a single file or for an entire directory.
- It gives information about the number of files being backed up and the size of the files using `WatchDirComposite` class.

## Watch Directory Structure
- A composite pattern is used to get information regarding the number of files within a directory and the size of the files. 
- The `WatchDirComponent` is to be implemented by both the composite `WatchDirComposite` and the children `WatchDirLeaf`.
- The `WatchDirComposite` class is the container that comprises any number of files, including other directories. A `WatchDirLeaf` class is used to represent a single file. 
- A `WatchDirComposite` class has the same methods as a `WatchDirLeaf` class. However, instead of doing something on its own, it passes the request recursively to all its children and “sums up” the result.