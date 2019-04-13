
# coding: utf-8

# In[1]:


#Author: Dhivyabharathi Ramasamy
#This script extracts text from pdf using tika. Set path as required.

# Import statements
from urllib.request import urlopen
from tika import parser
import requests

#Set path
pdf_path = os.getcwd()+'/data/pdf/'
extract_path = os.getcwd()+'/data/extracted_files/'

# Extract pdf to text
files = glob(pdf_path+'*.pdf')
print("files found ",len(files))

count = 0
for file in files:
    filename = file.split(pdf_path)[1]
    try:
        raw = parser.from_file(pdf_path+filename)
        with open(extract_path+filename,'w+') as f:
            f.write(raw['content'])
        count += 1
    except:
        print("unable to parse ",filename)
        
print("files extracted ",count)
print('Done')

