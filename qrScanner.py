from pyzbar import pyzbar
from PIL import Image
import xmltodict

def scanQR(file_name,isWebpage = True):
    image = Image.open('uploads/'+file_name)
    decodedList = pyzbar.decode(image)
    barcodeData = decodedList[0].data
    xmlData = str(barcodeData)[42:-1]
    if isWebpage:
        return xmltodict.parse(xmlData)
    else:
        return xmlData


if __name__ == '__main__':
    print(scanQR('upload.png',isWebpage=False))
