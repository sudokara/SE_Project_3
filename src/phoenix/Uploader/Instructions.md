# For Google Drive


1. Installation of the Google API Python Client

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
``` 

2. Create a new project in the Google Cloud Console and enable the Google Drive API. In the consent screen choose the user type as `External` and click on `Create`. Add a app name, a support mail and developer Contact Information. Click on `Save and Continue`. In the `Scopes for Google APIs` section also click on `Save and Continue` same for the `Test Users` section.

3. Now go to the `Credentials` section and click on `Create Credentials` and choose `OAuth client ID`. Choose `Desktop app` as the application type and click on `Create`. Click on `Download` to download the credentials file. Rename the file to `credentials.json` and move it to the same directory as the script.

4. Create a new folder in your Google Drive and get the folder ID. The folder ID is the last part of the URL when you open the folder in your browser. For example, if the URL is `https://drive.google.com/drive/u/0/folders/1XZ2e3Y4e5F6g7H8i9J0k1L2m3n4o5p6q`, the folder ID is `1XZ2e3Y4e5F6g7H8i9J0k1L2m3n4o5p6q`.