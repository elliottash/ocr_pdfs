
# coding: utf-8
# Author: Dhivyabharathi Ramasamy
# Requirement: Tesseract library


from urllib.request import urlopen
from tika import parser
import requests
from glob import glob
import os
from pdf2image import convert_from_path, convert_from_bytes
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

#files to be ocr'ed
pdf_folder = os.path.join(os.getcwd(),'data','pdf','')
#temp files
temp_folder = os.path.join(os.getcwd(),'temp','')
#results folder
results_folder = os.path.join(os.getcwd(),'results','')

#take all the pdf files in this folder to ocr'ed
zfiles = glob(pdf_folder+'/*.pdf')


for file in zfiles:
			#filename 
            filename = file.split('.pdf')[0].split('\\')[-1]
            print(filename)
			#convert the pdfs to images to be ocr'ed and save them in temp_folder
            try:
                images = convert_from_path(file)
            except:
                pass
            print(filename+': ' + str(len(images))+' pages. OCR and saving.')
            titles = []
            try:
                for i in range(len(images)):
                    title = 'out_'+str(i) + '.jpg'
                    titles.append(title)
                    try:
                        images[i].save(temp_folder+title, 'JPEG')
                    except:
                        pass
            except:
                pass
            #check if the ocr for the file already exists 
            try:
                os.remove(results_folder+filename+'.txt')
                print('ocr already done')
            except:
                pass
            #ocr using tesseract and write the data into .txt file in result_folder
            for title in titles:
                try:
                    data = pytesseract.image_to_string(Image.open(temp_folder+title))
                    with open(results_folder+filename+'.txt','a+') as f:
                        f.write(data)
                except:
                    pass
            print("OCR Done.")
            #clean up the temp files
            files = glob(temp_folder+'*')
            for f in files:
                os.remove(f)
            print("All files Done.")
            

