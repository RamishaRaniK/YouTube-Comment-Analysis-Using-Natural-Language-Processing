import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

os.chdir('D:\\Ramisha_Practice\\Mixed_Language(Eng and Tamil)\\5.Most_Comment_greater50_ML')

import glob
extension='csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

results=[]

for filename in all_filenames:#Taking one by one file from load file
    dataset=pd.read_csv(filename)#Reading .csv file for a subcriber from the load file
    cv = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')# Assign the value for max and min allowance stopwords
    dtm = cv.fit_transform(dataset['commentText'])# Transforming commentText to tfdif formula
    LDA = LatentDirichletAllocation(n_components=5,random_state=42)#Assigning number of topics
    LDA.fit(dtm)
    print(f'******************{filename}*******************************')
    for index,topic in enumerate(LDA.components_):
        print(f'THE TOP 15 WORDS FOR TOPIC #{index}')
        result=([cv.get_feature_names()[i] for i in topic.argsort()[-10:]])
        results.append([filename,result])
        print('\n')
    topic_results = LDA.transform(dtm)
    dataset['Topic'] = topic_results.argmax(axis=1)
    dataset.to_csv(f"{filename}_TM_ML.csv",index=False)


Topic_modelling_NML=pd.DataFrame(results)

Topic_modelling_NML.to_csv('Greater50com_Sub_TopicModeling_OT_NML.csv',index=False)

Topic_modelling_NML.head()



