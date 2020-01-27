from pyzbar import pyzbar
from PIL import Image


def scanQR(file_name):
    image = Image.open('uploads/'+file_name)
    return pyzbar.decode(image)


if __name__ == '__main__':
    print(scanQR('upload.png')[0].data)
