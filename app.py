from flask import Flask, render_template, request
from qrScanner import scanQR
from tesseractOCR import scanForText
from face_extractor import extract_face

app = Flask(__name__, template_folder='template')


@app.route('/', methods=["GET"])
def home():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        #Getting Data from form: -  print(request.form["text"])
        f.save('uploads/upload.png')
        dataDict = scanQR('upload.png')

        extract_face('prathamesh.jpg')
        return render_template('response.html', 
            Image = 'prathamesh.jpg',
            UID=dataDict['PrintLetterBarcodeData']['@uid'], 
            Name=dataDict['PrintLetterBarcodeData']['@name'], 
            Gender=dataDict['PrintLetterBarcodeData']['@gender'], 
            Date_of_Birth=dataDict['PrintLetterBarcodeData']['@dob'], 
            CO=dataDict['PrintLetterBarcodeData']['@co'],
            Loc=dataDict['PrintLetterBarcodeData']['@loc'],
            VTC=dataDict['PrintLetterBarcodeData']['@vtc'],
            Po=dataDict['PrintLetterBarcodeData']['@po'],
            District=dataDict['PrintLetterBarcodeData']['@dist'],
            SubDistrict=dataDict['PrintLetterBarcodeData']['@subdist'],
            State=dataDict['PrintLetterBarcodeData']['@state'],
            Pincode=dataDict['PrintLetterBarcodeData']['@pc'],
            Year_of_Birth=dataDict['PrintLetterBarcodeData']['@yob'],
            OCR=scanForText(image="uploads/upload.png",preprocess="blur"))


if __name__ == '__main__':
    app.run(debug=True)
