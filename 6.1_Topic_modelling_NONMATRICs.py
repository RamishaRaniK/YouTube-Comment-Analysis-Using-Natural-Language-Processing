"Importing necessary Files"
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

"Changing working directory where file is stored"
os.chdir('D:\\Ramisha_Practice\\NonMixed_Language(Eng)\\5.Most_Comment_greater50_NML')

"Saving  all csv file in the folder"
import glob
extension='csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

results=[]

for filename in all_filenames: #Taking one by one file from load file
    dataset=pd.read_csv(filename)#Reading .csv file for a subcriber from the load file
    tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')# Assign the value for max and min allowance stopwords
    dtm = tfidf.fit_transform(dataset['commentText'])# Transforming commentText to tfdif formula
    nmf_model = NMF(n_components=5,random_state=42)#Assigning number of topics
    nmf_model.fit(dtm)#Tranforming Transformed commentText formula to NMF .This stores the output of 5 topic modelling topics
    print(f'******************{filename}*******************************')
    for index,topic in enumerate(nmf_model.components_):# Now we are printing Top 10 words under each Topic
        print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
        result=([tfidf.get_feature_names()[i] for i in topic.argsort()[-10:]])
        results.append([filename,result])
    topic_results = nmf_model.transform(dtm)
    dataset['Topic'] = topic_results.argmax(axis=1)#Assign respective topics to each commentTent
    dataset.to_csv(f"{filename}_TM_NMF_NML.csv",index=False)# Saving result file


Topic_modelling_NML=pd.DataFrame(results)# Saving the topics for each subcriber

Topic_modelling_NML.to_csv('NMF_Greater50com_Sub_TopicModeling_OT_NML.csv',index=False)

Topic_modelling_NML.head()



