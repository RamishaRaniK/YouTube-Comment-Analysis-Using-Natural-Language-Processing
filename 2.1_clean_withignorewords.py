print("start")
import time
start=time.time()
import threading
import re  
import pandas as pd
import chardet

with open(r'Clean_TCP.csv', 'rb') as f:
    result = chardet.detect(f.read())
    
dfList= [] 



for chu in pd.read_csv("Clean_TCP.csv",chunksize=5000,encoding=result['encoding']):
    print(chu.shape)
    dfList.append(chu)
    
words=[]  
def word_append(li):
    text_file = open("ignore_words.txt", "r")
    ignore_words = text_file.read().splitlines()    
    li.index=range(li.shape[0])
    li['filtered_word']=""
    for i,word in enumerate(li['commentText']):
        tt = word.lower()
        t = re.sub(r'[^\w]', ' ', tt)
        for word in t.split():
            if "http" in word:
                continue
            if word not in ignore_words:
                li['filtered_word'][i]+=word +" "
                

for i in range(len(dfList)) :
    
    thread1 = threading.Thread(target = word_append, args = [dfList[i]])
    thread1.start()
    print(f"Th {i} started")
print("All started")
    
    
print("Total number of threads", threading.activeCount())
print("List of threads: ", threading.enumerate())

end=time.time()
print("Exection Time:",(end-start)) 



 
wholeframe=pd.concat(dfList,sort=True)
wholeframe.index= range(wholeframe.shape[0])

wholeframe['Filtered_TW']=wholeframe['filtered_word'].str.split().str.len()
import numpy as np
wholeframe['Filtered_TW'].replace(0, np.nan, inplace=True)
wholeframe.isnull().sum()

wholeframe=wholeframe.dropna(subset=['Filtered_TW'])



wholeframe.to_csv("Cleaned_ignored.csv", index=False)    
    
    
    
    
    
    
    