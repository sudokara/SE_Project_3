# Using inotify for File System Monitoring

## Status
Accepted

## Context
Phoenix is an automatic backup system that uploads files to a configurable secondary cloud based storage. The system relies on a file monitoring subsystem to detect changes within the designated directory. These changes encompass file modifications, creations, deletions, and alterations in the directory's file structure. The file monitoring subsystem must provide real-time monitoring capabilities to promptly detect any changes within the watched directory and must be reliable and robust, ensuring accurate detection and reporting of file-related events without any false positives or negatives.

### Alternatives Considered:
- inotify
- fswatch

## Decision
In this context, we propose using the **inotify** mechanism for file system monitoring due to the following reasons:
- It operates asynchronously, allowing applications to monitor file system events without the need for continuous polling, which reduces CPU and I/O overhead.
- inotify provides real-time notification of file system events, allowing applications to respond promptly to changes in the watched directory.
- inotify supports a wide range of event types, including file creations, modifications, deletions, attribute changes, and directory modifications. 
- inotify is designed to handle large volumes of file system events efficiently, making it suitable for applications that require scalable event monitoring capabilities. 
- inotify can be integrated into python applications using the python wrapper `pyinotify`.
- fswatch on the other hand is compatible with other operating systems such as macOS and windows, but it has several issues. Setting up fswatch can be complex and time-consuming. 
- The inotify monitor, may suffer a queue overflow if events are generated faster than they are read from the queue. In any case, the application is guaranteed to receive an overflow notification which can be handled to gracefully recover. fswatch currently throws an exception if a queue overflow occurs.

## Consequences
- Integration: Pyinotify seamlessly integrates with Python applications, making it easier to incorporate into our existing codebase.
- Familiarity: Many members of our team are already familiar with Pyinotify, reducing the learning curve and enabling faster development.
- Platform Compatibility: While Fswatch is compatible with Linux, macOS, and Windows, Pyinotify is primarily designed for Linux systems. However, since our software system primarily targets Linux, this limitation is acceptable for our current needs.