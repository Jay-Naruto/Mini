import pytesseract
from PIL import Image
import datetime
from cv2 import cv2
import sys
import os
import os.path
import re
from pyzbar.pyzbar import decode

from dummy3 import AadhaarSecureQr

try:
            img = cv2.imread('Adhaar5.jpg')
            for barcode in decode(img):
                x = barcode.data
            obj = AadhaarSecureQr(int(x.decode(encoding='UTF-8')))
            data = obj.decodeddata()
            name = data["name"]
            g = data["gender"]
            digit = data["adhaar_last_4_digit"]
            x = {"name": name, "g": g, "digi": digit}

except:
            print("Not valid")