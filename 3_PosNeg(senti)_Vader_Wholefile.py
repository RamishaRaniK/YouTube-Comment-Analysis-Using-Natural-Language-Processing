"Changing directory"
import os
os.chdir("D:\\Ramisha_Practice\\NLP\\NLP_Python\\wholefile")

"Reading file"
import pandas as pd
data=pd.read_csv('Whole_file.csv')

"Importing NLTK"
import nltk
nltk.download('vader_lexicon')#downloading vader_lexicon for the process

"Importing Necessary Packeage"
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

"Deleting null pr empty value"
data.dropna(inplace=True)

"Checking for a comment"
sid.polarity_scores(data['commentText'][4478])

"Creating respective columns"

data['scores'] = data['commentText'].apply(lambda commentText: sid.polarity_scores(commentText))
data['compound']  = data['scores'].apply(lambda score_dict: score_dict['compound'])
data['Negtive']  = data['scores'].apply(lambda score_dict: score_dict['neg'])
data['Postive']  = data['scores'].apply(lambda score_dict: score_dict['pos'])
data['Neutral']  = data['scores'].apply(lambda score_dict: score_dict['neu'])

"Creating final pos or neg using compound score"
data['comp_score'] = data['compound'].apply(lambda c: 'pos' if c >=0 else 'neg')

"Checking how many pos and neg"
data['comp_score'].value_counts()


"Converting most commented uer to csv file"
data['user'].value_counts().to_csv('Mostcomment.csv',index=True)

data.to_csv('PosNeg(senti)_Vader_Wholefile_ML.csv', index=False)

