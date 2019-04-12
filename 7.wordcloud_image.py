# Python program to generate WordCloud 
  
# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd 
import os

os.chdir("D:\\Ramisha_Practice\\NonMixed_Language(Eng)") 

import glob
extension='csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

 
# Reads 'Youtube04-Eminem.csv' file
  
comment_words = ' '
stopwords = set(STOPWORDS) 

for filename in all_filenames:
# iterate through the csv file 
    dataset=pd.read_csv('2.Cleaned_Wholefile_NML.csv')
    
    for val in dataset.commentText: 
      
    # typecaste each val to string 
        val = str(val) 
  
    # split the value 
        tokens = val.split() 
      
    # Converts each token into lowercase 
        for i in range(len(tokens)): 
            tokens[i] = tokens[i].lower() 
          
        for words in tokens: 
            comment_words = comment_words + words + ' '
  


    wordcloud = WordCloud(width = 800, height = 800, 
                          background_color ='white', 
                          stopwords = stopwords, 
                          min_font_size = 10).generate(comment_words) 
  
# plot the WordCloud image  
    print(f"***************************{filename}****************************************")
    plt.figure(figsize = (15, 15), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis("off") 
    plt.tight_layout(pad = 0) 
    plt.savefig('Topicmodelling_wholefile_NML.PNG')
    plt.show() 
    print("Successfully created")