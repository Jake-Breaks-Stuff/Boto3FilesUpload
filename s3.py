from flask import Flask, request

import boto3

app = Flask(__name__)


@app.route("/")
def index():
    return '''<form method=POST enctype=multipart/form-data action="upload">
    <input type=file name=myfile multiple="">
    <input type=submit>
    </form>'''


@app.route('/upload', methods=['POST'])
def upload():
    #Initializing the resource, and fileContents.
    s3 = boto3.resource('s3')
    fileContents = request.files.getlist('myfile')
    
    #for loop to cycle through all the selected files and upload their names and content. 
    for files in fileContents:
        file_contents = files.read()

        fileNames = files.filename
        s3.Bucket('INPUT BUCKET NAME HERE').put_object(Key=fileNames,
                                                  Body=file_contents)

    return index()


if __name__ == '__main__':
    app.run(debug=True)
