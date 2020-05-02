from flask import Flask, render_template, request, redirect, url_for
from qrScanner import scanQR
from tesseractOCR import scanForText
from face_extractor import extract_face
from dbHandle import authenticateUser, isLoggedIn
import config

app = Flask(__name__, template_folder=config.TEMPLATE_FOLDER)


@app.route('/', methods=["GET"])
def home():
    return render_template('home.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form["login-username"]
        password = request.form["login-password"]
        if authenticateUser(username, password):
            print("Log in")
            return redirect(url_for('upload_file'))
        else:
            print("Fails")
            return redirect(url_for('login'))


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        if isLoggedIn:
            return render_template('upload.html')
        else:
            return redirect(url_for('login'))
    elif request.method == 'POST':
        f = request.files['aadhar-card']
        # Getting Data from form: -  print(request.form["text"])
        f.save('uploads/upload.png')
        dataDict = scanQR('upload.png')

        extract_face('prathamesh.jpg')
        return render_template('response.html',
                               Image='prathamesh.jpg',
                               UID=dataDict['PrintLetterBarcodeData']['@uid'],
                               Name=dataDict['PrintLetterBarcodeData']['@name'],
                               Gender=dataDict['PrintLetterBarcodeData']['@gender'],
                               Date_of_Birth=dataDict['PrintLetterBarcodeData']['@dob'],
                               CO=dataDict['PrintLetterBarcodeData']['@co'],
                               Loc=dataDict['PrintLetterBarcodeData']['@loc'],
                               VTC=dataDict['PrintLetterBarcodeData']['@vtc'],
                               Po=dataDict['PrintLetterBarcodeData']['@po'],
                               District=dataDict['PrintLetterBarcodeData']['@dist'],
                               # SubDistrict=dataDict['PrintLetterBarcodeData']['@subdist'],
                               State=dataDict['PrintLetterBarcodeData']['@state'],
                               Pincode=dataDict['PrintLetterBarcodeData']['@pc'],
                               Year_of_Birth=dataDict['PrintLetterBarcodeData']['@yob'],
                               OCR=scanForText(image="uploads/upload.png", preprocess="blur"))


if __name__ == '__main__':
    app.run(debug=True)
