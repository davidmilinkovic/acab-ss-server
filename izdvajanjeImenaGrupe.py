import numpy as np
import cv2
import pytesseract
from PIL import Image
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"
tessdata_dir_config = r'--tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"'

paja = config["Paja"]

def vratiImeGrupe(img):
    #preporucujem koriscenje opencv biblioteke preko PIL jer je uspesnije prepoznavanje
    cropped = img.crop((int(paja["goreLevoX"]), int(paja["goreLevoY"]), int(paja["doleDesnoX"]), int(paja["doleDesnoY"])))
    #cropped = img[7:29, 71:245]
    #cv2.imwrite('cropped.png',cropped)
    cropped.save("cropped.png")

    #vracaju se 4 rezultata, posto varira koji je najuspesniji od konkretnog primera
    #tekstLatinica = pytesseract.image_to_string(img, lang='srp_latn', config=tessdata_dir_config)
    #tekstCirilica = pytesseract.image_to_string(img, lang='srp',  config=tessdata_dir_config)
    tekstLatinicaCropped = pytesseract.image_to_string(cropped, lang = 'srp_latn',  config=tessdata_dir_config)
    #tekstCirilicaCropped = pytesseract.image_to_string(cropped, lang = 'srp',  config=tessdata_dir_config)
    '''
    niz = [tekstLatinica,tekstLatinicaCropped,tekstCirilica,tekstCirilicaCropped]
    for i in range(len(niz)):
        niz[i] = ''.join(x for x in niz[i] if x.isalpha())
    '''
    tekstLatinicaCropped = ''.join(x for x in tekstLatinicaCropped if x.isalpha())
    return tekstLatinicaCropped


