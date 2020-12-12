import numpy as np
import cv2
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

def vratiImeGrupe(img):
    #preporucujem koriscenje opencv biblioteke preko PIL jer je uspesnije prepoznavanje
    cropped = img[7:29, 71:245]
    #cv2.imwrite('cropped.png',cropped)

    #vracaju se 4 rezultata, posto varira koji je najuspesniji od konkretnog primera
    tekstLatinica = pytesseract.image_to_string(img, lang='srp_latn')
    tekstCirilica = pytesseract.image_to_string(img, lang='srp')
    tekstLatinicaCropped = pytesseract.image_to_string(cropped, lang = 'srp_latn')
    tekstCirilicaCropped = pytesseract.image_to_string(cropped, lang = 'srp')
    
    niz = [tekstLatinica,tekstLatinicaCropped,tekstCirilica,tekstCirilicaCropped]
    for i in range(len(niz)):
        niz[i] = ''.join(x for x in niz[i] if x.isalpha())
    return niz[0]


