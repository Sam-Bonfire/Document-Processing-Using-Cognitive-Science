from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')


@app.route('/', methods=["GET"])
def home():
    return '<html><body><form action = "/uploader" method = "POST" enctype = "multipart/form-data"><input type = "file" name = "file"/><input type = "submit" value = "Submit"/></form></body></html>'


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploads/upload.png')
        return '<h1>File Uploaded Successfully!!!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
