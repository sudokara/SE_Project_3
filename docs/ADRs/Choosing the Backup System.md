# Choosing the Backup Systems:

## **Context:**
We are making a Backup system, which a user can use to backup file or directories periodically, or triggred by an event.
The user should have multiple backup options, both local and cloud based.
The system should be scalable, cost effective, secure, and easy to use.
The system will be made by a team of two in 1 week. It should also be easy to engineer and maintain.

## Considered Alternatives:
### OneDrive
- Configuration and usability is moderately complex.
- 5 GB free storage limit; larger storage requires Microsoft 365 subscription.

### Google Drive
- 15 GB of free storage.
- Easy to maintain and use

### AWS
- Highly scalable and flexible with Amazon S3.
- Configuration and management complexity.
- Variable costs based on usage. No free storage.
- Not made for single users, but for organisations
  
### Local Storage
- Full control over data security and privacy.
- Fast data access and recovery speeds.
- Requires physical space and maintenance.
- Vulnerable to local disasters (e.g., fire, theft) without off-site redundancy.

## Decision
We opted for a multi-system backup strategy incorporating Local Storage, Azure, and Google Drive. This approach ensures scalability, cost-effectiveness, security, and ease of use, leveraging Azure’s robust cloud storage, Google Drive’s generous free storage, and Local Storage’s quick data access and security control.

## Status
Accepted
