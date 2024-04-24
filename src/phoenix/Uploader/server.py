from flask import Flask, request
import json
from phoenix.Uploader.GoogleDrive import GoogleDrive
from phoenix.Uploader.OneDrive import OneDrive
from phoenix.Uploader.Uploader import Uploader

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload', methods=['POST'])
def upload():
    if request.method != 'POST':
        return 'Invalid request method'

    data = request.data
    
    with open("../config.json") as f:
        config = json.load(f)
    
    if config['cloud-provider'] == "gdrive":
        uploadDownloadStrategy = GoogleDrive(config['gdrive-folder-id'])
    else:

        with open("../Uploader/onedrive_credentials.json") as f:
            onedrive_config = json.load(f)

        uploadDownloadStrategy = OneDrive(siteName=onedrive_config['siteName'], sites=onedrive_config['sites'], domain=onedrive_config['domain'], onedrive_path=onedrive_config['onedrive_path'], client_id=onedrive_config['client_id'], authority=onedrive_config['authority'])

    uploader = Uploader(uploadDownloadStrategy)
    uploader.upload_file(data.get('encryptedPath'))   
    
    return 'Success'     

if __name__ == '__main__':
    app.run(port=5001, debug=True)