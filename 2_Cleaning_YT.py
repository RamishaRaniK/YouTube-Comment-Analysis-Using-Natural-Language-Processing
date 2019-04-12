
"Chaging working directory"
import os
os.chdir("D:\\Ramisha_Practice\\NLP\\NLP_Python\\wholefile")


"Importing neccessary file"
import numpy as np
import pandas as pd
import chardet

"Raw file contains mixed language to read all"
with open(r'eff.csv', 'rb') as f:
    result = chardet.detect(f.read())    
dataset=pd.read_csv(r'eff.csv',encoding=result['encoding'])

"Checking total count"
dataset.tail()

"Checking Null value"
dataset.isnull().sum()

"Droping Null value"
dataset=dataset.dropna(subset=['commentText'])
dataset=dataset.dropna(subset=['user'])

"Agian Checking"
dataset.isnull().sum()

"Replacing Puncation with place. All tamil lanugae changed to question mark"
dataset['commentText'] = dataset['commentText'].str.replace('[^\w\s]','')
dataset['user'] = dataset['user'].str.replace('[^\w\s]','')

"Changing all string to lowercase"
dataset['commentText'] = dataset['commentText'].str.lower()
dataset['user'] = dataset['user'].str.lower()  

"Have to remove empty commentText row which contains whitespace"
dataset['onlysapce']=0
dataset['onlyspace_user']=0
[l,h]=dataset.shape
dataset.index=range(l)

#removing unwanted whitespace and calculating total character(length) in the columns
for k,comment in enumerate(dataset.index):
    print(k)
    print(comment)
    if k not in dataset.index:
            pass
    else:
        dataset['onlysapce'][k]=len(dataset['commentText'][k].strip())
        dataset['onlyspace_user'][k]=len(dataset['user'][k].strip()) 
        
#BAckup file      
dataset.to_csv('spacevalue.csv',index=False)
     

# dropping entire row which deoes not not contain informaation    
for k, serial in enumerate(dataset['onlysapce']):
    if(serial==0 or serial ==1):
        print(serial)
        dataset=dataset.drop(k)
        print("droped")
    else:
        pass
    
    
[l,h]=dataset.shape
dataset.index=range(l)

#droping user which is empty
for k, serial in enumerate(dataset['onlyspace_user']):
    if(serial==0):
        print(serial)
        dataset=dataset.drop(k)
        print("droped")
    else:
        pass

#checking numeric and dropping it
for k, serial in enumerate(dataset['commentText']):
    if(serial.isnumeric()):
        print(serial)
        dataset=dataset.drop(k)
        print("droped")
    else:
        pass

#backupfile
dataset.to_csv('Clean_TCP.csv',index=False)















