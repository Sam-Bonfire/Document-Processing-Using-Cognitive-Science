from flask import Flask, render_template, request
from qrScanner import scanQR

app = Flask(__name__, template_folder='template')


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploads/upload.png')
        dataDict = scanQR('upload.png')
        renderData = ''
        for key in dataDict['PrintLetterBarcodeData']:
            renderData+='<p>'+str(key)+' : '+str(dataDict['PrintLetterBarcodeData'][key])+'</p>'
        return renderData


if __name__ == '__main__':
    app.run(debug = True)
