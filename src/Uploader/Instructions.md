# For Google Drive


1. Installation of the Google API Python Client

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
``` 

2. Create a new project in the Google Cloud Console and enable the Google Drive API. In the consent screen choose the user type as `External` and click on `Create`. Add a app name, a support mail and developer Contact Information. Click on `Save and Continue`. In the `Scopes for Google APIs` section also click on `Save and Continue` same for the `Test Users` section.

3. Now go to the `Credentials` section and click on `Create Credentials` and choose `OAuth client ID`. Choose `Desktop app` as the application type and click on `Create`. Click on `Download` to download the credentials file. Rename the file to `credentials.json` and move it to the same directory as the script.

4. Create a new folder in your Google Drive and get the folder ID. The folder ID is the last part of the URL when you open the folder in your browser. For example, if the URL is `https://drive.google.com/drive/u/0/folders/1XZ2e3Y4e5F6g7H8i9J0k1L2m3n4o5p6q`, the folder ID is `1XZ2e3Y4e5F6g7H8i9J0k1L2m3n4o5p6q`.



# For OneDrive


### Azure Portal Setup:
- Navigate to [Azure Portal](https://portal.azure.com).
- In the search bar, enter `App registrations` and select it.
- Click on `New registration`.
- Provide a name for the application.
- For `Supported account types`, select `Accounts in any organizational directory (Any Microsoft Entra ID tenant - Multitenant)`.
- Under `Redirect URI (optional)`, choose `Public client/native (mobile and desktop)` and enter `http://localhost:8000` as the redirect URI.
- Click `Register`. You'll be redirected to the application overview page.
- Go to `API permissions`.
- Click `Add permission`.
- Select `Microsoft Graph`.
- Choose `Delegated permissions`.
- Select `Files.ReadWrite` and `Files.ReadWrite.All`.
- Click `Add permissions`.

### Code Changes:
- Update the `siteName` and `onedrive` path in your code. Ensure the `onedrive` path is a file path, not a folder path.
- Change `onedrive_path`
- Fill in the `client ID` with the `Application (client) ID` found on the `App Registration Overview` page.
- Retrieve the `Directory (tenant) ID` from the `App Registration Overview` page and append it to the authority URL, replacing the last segment after the slash.

These steps should help you effectively set up your application in Azure and make the necessary code adjustments.
