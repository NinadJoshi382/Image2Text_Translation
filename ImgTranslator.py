from base64 import encode
import cv2 as cv
from cv2 import phase
import pytesseract
from deep_translator import GoogleTranslator, single_detection
import googletrans 
Akey ='generate your key on https://detectlanguage.com/users/sign_in'
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' #file that contains already trained Data set of diff fonts of texts.
img = cv.imread('your image',cv.IMREAD_GRAYSCALE)#grey scale img read (cv.IMREAD_GRAYSCALE)
x,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)#so that non white color texts can also be detected by pytesseract
#to detect text from the image
txt = pytesseract.image_to_string(th1)
#spliting it into phrases 
To_trans = txt.split('\n')
#print(To_trans)
langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)
print(langs_dict,'\n')




cvt = input("Enter Language to Translate to \n")             
cvt2 = langs_dict[cvt]

for i in range(len(To_trans)):
    if(To_trans[i]!=''):
        text_trans = To_trans[i]
        print("------------------------------------------------------------------------\n")
        print(text_trans+'\n')
        lan = single_detection(text=text_trans,api_key=Akey)
        print(f"Translated from {lan} to {cvt} \n")
        print(GoogleTranslator(source="auto",target=cvt2).translate(text=text_trans,encode='utf-8')+'\n')
        print("------------------------------------------------------------------------\n")
    else:
        pass    

cv.imshow('Result',img)
cv.waitKey(0)
cv.destroyAllWindows()

