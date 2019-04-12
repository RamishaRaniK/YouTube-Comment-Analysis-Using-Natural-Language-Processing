"Chaging working directory"
import os
os.chdir("D:\\Ramisha_Practice\\NonMixed_Language(Eng)")


"Importing neccessary file"
import pandas as pd
import chardet
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF


results=[]

dataset=pd.read_csv('2.Cleaned_Wholefile_NML.csv')
tfidf = TfidfVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = tfidf.fit_transform(dataset['commentText'])
nmf_model = NMF(n_components=5,random_state=42)
nmf_model.fit(dtm)
#print(f'******************{filename}*******************************')
for index,topic in enumerate(nmf_model.components_):
    #print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
    result=([tfidf.get_feature_names()[i] for i in topic.argsort()[-10:]])
    results.append(['Cleaned_Wholefile_NML',result])
   # print('\n')
topic_results = nmf_model.transform(dtm)
dataset['Topic'] = topic_results.argmax(axis=1)
dataset.to_csv("Wholefile_TM_NMF_NML.csv",index=False)


Topic_modelling_NML=pd.DataFrame(results)

Topic_modelling_NML.to_csv('Wholefile_NMF_OT_NML.csv',index=False)

Topic_modelling_NML.head()


