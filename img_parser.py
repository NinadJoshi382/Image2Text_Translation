import cv2 as cv
import pytesseract 
from translator import Translations

class Do_Ocr():
    def __init__(self,path) -> None:
        self.img_path = path
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    
    def get_text(self)-> str:
        img = cv.imread(self.img_path,cv.IMREAD_GRAYSCALE)
        x,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
        #img = cv.cvtColor(img, cv.COLOR_BGR2RGB) 
        #x,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
        output_text = pytesseract.image_to_string(th1) 
        '''if True :#Translations.trans_late()
            tslate = Translations(output_text,'0b57146c3d8693bf6736a6ec24ba004e')
            return tslate.trans_late('en')'''
        return output_text
        
    def box_text(self):
        img = cv.imread(self.img_path)
        Himg,Wimg,Temp = img.shape
        boxes_list = pytesseract.image_to_boxes(img)
        for b in boxes_list.splitlines():
        #print(b)
            b = b.split(' ')
        #print(b)
            x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
            cv.rectangle(img,(x,Himg-y),(w,Himg-h),(0,0,255),1)
            cv.putText(img,b[0],(x,Himg-y+25),cv.FONT_HERSHEY_COMPLEX_SMALL,1,(100,100,100),2)
        cv.imshow('Result',img)
        cv.waitKey(0)
        cv.destroyAllWindows()


