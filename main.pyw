from flask import Flask, request
import webbrowser
import os
import time

app = Flask(__name__)

UPLOAD_FOLDER = 'C:/Users/{USER}/Downloads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/data', methods=['POST'])
def data():
    data = request.get_json()

    if 'url' in data:
        webbrowser.open(data['url'])
        return 'Success'
    
    if "text" in data:
        #open text editor temporarily to write url into file and open it and delete it afterwards
        f = open("C:/Users/{USER}/Desktop/transfer_text.txt", "w")
        f.write(data['text'])
        f.close()
        os.startfile("C:/Users/{USER}/Desktop/transfer_text.txt")
        time.sleep(1)
        os.remove("C:/Users/{USER}/Desktop/transfer_text.txt")
        return 'Success'

@app.route('/media', methods=['POST'])
def media():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']
    if file.filename == '':
        return 'No selected file'

    if file:
        #check if file with same name already exists
        if os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], file.filename)):
            filename = file.filename.split(".")
            #get time and date in following format "18112023"
            date = time.strftime("%d%m%Y")
            filename = filename[0] + "_" + date +  "." + filename[1]
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            os.startfile(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'Success'
        else:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            os.startfile(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            return 'Success'

    return 'Error in uploading file'

app.run(host='0.0.0.0', port=9000) # Stellen Sie sicher, dass Ihr Gerät erreichbar ist