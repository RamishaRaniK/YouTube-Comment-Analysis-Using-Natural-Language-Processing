## YouTube-Comment-Analysis-Using-Natural-Language-Processing
This repository helps to analysis YouTube comments using Natural Language Processing.

YouTube comments may contain more than one language. So I have splitted into two set output branch. Mixed Language(Eng, tam and any) as ML and Non-Mixed Language(Only english) as NML

Same code for both the cases, For effective analysis I have analysed as two parts ML and NML

### Step 1: Collect interested YouTube comment in a seperate folder using below link ##

using the http://ytcomments.klostermann.ca/ can download interested youtube video comments
My full hearted thanks to this team who made time consuming work in to one click work.

## Step 2 &  Step 3 for Python Beginners(Optional for others)

### Step 2 : Download Anaconda Distribution from the below link ###

click  this https://www.anaconda.com/distribution/#download-section 
According to your operating System Download the distribution and install( can refer any youtube videos)

### Step 3: Creating Virtual Environment ###

After the installation of Anaconda, type Anaconda prompt in the windows search bar 

    1. Anaconda Prompt --> Right Click --> Run as Administrator 

    2. conda create -n <project name>

Example:
     conda create -n nlp

    3.After this step close the Anaconda Prompt.

    4. Again open

    Anaconda Prompt --> Click
    $(base)D:\er\# activate nlp
    (nlp)D:\er\# pip install numpy
    (nlp)D:\er\# pip install nltk
    (nlp)D:\er\# pip install chardet
    (nlp)D:\er\# pip install pandas
    (nlp)D:\er\# pip install matplotlib
    (nlp)D:\er\# pip install spyder=3.2.3 (This will install Python 3.6.8)
    
  
### Step 4: Have to merge whole collected .csv file as one file(only if you want to analysis more video comments files at a time)

1_All_to_one_YT.py

#### Note: My order of output file name
    orderno_taskname_Algorithms_decription_classificationname
#### 1. After combined number files into one file  
    1_Uncleaneddata_Algo_Wholefile_ML.csv    Python file name: 1_All_to_one_YT.py      
#### 2. Removed empty rows, Unwanted rows 
    2_Cleaneddata_Algo_Wholefile_ML.csv      Python file name: 2_Cleaning_YT.py
#### 3. Sentimental Analysis for whole file using Vader from NLTK
    3_PosNeg(senti)_Vader_Wholefile_ML.csv    Python file name: 3_PosNeg(senti)_Vader_Wholefile.py
#### 4. Same person may commented many times, if u want to see who commented number of times. Here, I have done for who commented more than 50 times. Only lists stored in the file which will be used later. Condition depends on your need.         
    4_MostCommented_grt50com_list_ML.csv    Python file name: 4_Most commented file.py
#### 5. With the help of previous list file, entire information of particular people will be stored as .csv file for each subcriber who are all commented more than 50 times.              
     5_MostCommented_grt50com_ML(Folder contains .csv)  Python file name: 4_Most commented file.py
#### 6. Sentimental Analysis for each subcriber comments
     6_PosNeg(senti)_grt50com_Eachsub_ML(Assign Senti to each .csv file from 5. )   Python file name: 5_PosNeg(senti)_grt50com_Eachsub
#### 7. Topic MOdelling using LDA 
       Python file name: 6.Topic modelling_LDA 
      7_Onlytopic_50LDA_Eachsub_ML  #Only topic list are storted for each subcriber using LDA
      7.1_OnlyTopic_LDA_Wholefile_ML # Only Topic list for whole file
      7.2_TopicAssign_LDA_Wholefile_Ml # Topic Assignment for whole file
      7.3_TopicAssign_LDA_Eachsub_ML(Folder) # Topic Assignment for each subcriber
#### 8. Topic Modelling Using NMF
       Python file name: 6.1_Topic_modelling_NONMATRICs
      8_OnlyTopic_50NMF_Eachsub_ML # Only topic list are storted for each subcriber using NMF
      8.1_Onlytopic_NMF_Wholefile_ML # Only Topic list for whole file
      8.2_TopicAssign_NMF_Wholefile_Ml # Topic Assignment for each subcriber
      8.3_TopicAssign_NMF_Eachsub_ML # Topic Assignment for each subcriber  
#### 9. Wordcloud     
    Python file name: 7.wordcloud_image
    9_Wordcloud_Algo_Topic_Wholefile_ML (image)  # Word cloud for wholefile                             
    9.1_Wordcloud_Algo_Topic_Eachsub_ML(Folder)   # Word cloud for each subcriber comments 
    
Note: Above output format follows same for NON MIXED Language.

## Conclusion

Here I have download youtube comments  and processed using NLP. The concept analysed are

1. Sentimental Analysis
2. Topic Modelling
3. Word Cloud

Those who want to do hands-on NLP you can try under different conditions.

Thank You.




