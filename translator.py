import sys
from deep_translator import GoogleTranslator, single_detection
import pandas as pd

class Translations():
    def __init__(self,text,key) -> None:
        self.text = text        #text that needs to be translated
        self.size = len(text)
        self.key = key
        if(self.size>500):
            self.over_limit = True #GoogleTranslator can not translate more than 500 char containing string at a time
        else:
            self.over_limit = False

    def detect_lang(self):
        lan = single_detection(text=self.text,api_key=self.key)
        print(f"Translated from {lan} \n")
    

    def trans_late(self,lang) -> str:
        out_text = ""  
        if self.over_limit:
            main_range = int((self.size)/500) # eg. 1023 = (2)*500 + 23
            rest_range = (self.size) % 500    # num = a.q + r 
            for i in range(main_range):
                #Translations(self.text[i * 500 : (i + 1) * 500]).detect_lang()
                out_text += GoogleTranslator(source="auto", target=lang).translate(text=self.text[i * 500 : (i + 1) * 500])
            out_text +=  GoogleTranslator(source="auto", target=lang).translate(text=self.text[:-(rest_range)])
        else:
            out_text = GoogleTranslator(source="auto", target=lang).translate(text=self.text)
        return out_text 
    

