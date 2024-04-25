from flask import Flask, request
import json
from phoenix.Uploader.GoogleDrive import GoogleDrive
from phoenix.Uploader.OneDrive import OneDrive
from phoenix.utils.Broker import Broker

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/encrypt-compress', methods=['POST'])
def encrypt_compress():
    if request.method != 'POST':
        return 'Invalid request method'

    data = request.json

    try:
        broker = Broker()
        broker.backup(data.get('absolutePath'), True if data.get('is_file') else False)
    except Exception as e:
        print("Exception: ", e)

    return "ok"
            
if __name__ == '__main__':
    app.run(port=5000, debug=True)