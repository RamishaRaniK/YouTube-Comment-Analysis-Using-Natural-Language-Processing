"Importing library"
import pandas as pd
import os

"Changing Path"
os.chdir('D:\\Ramisha_Practice\\NonMixed_Language(Eng)')


"Reading file"
dataset=pd.read_csv('3.Wholefile_Pos_Neg_NML.csv')

"Getting how many times each subcriber commented on the channel, filtering by who commented morethan 50 times."

indexs=(dataset['user'].value_counts() >= 50).sum()

"Creating dataframe all subcriber who commented on the channel"
users=pd.DataFrame(dataset['user'].value_counts())
l,w=users.shape


"Changing index to new columns"
users['Username']=users.index


"Changing index to numbers according to the rows of users dataframe"
users.index=range(l)

"creating new dataFrame with index of filtered number"
filterlist= pd.DataFrame(index=range(indexs))

"Creating new columns for filtered subcriber as Username nd No of comments"
filterlist['Username']=""
filterlist['NComments']= 0

"Filtering subcriber comment greater than 50, entring into seperate created dataframe"
for i,user, UName in users.itertuples(): 
    print(user)
    if(user >= 50):
        print('gresterthan 50')
        filterlist['Username'][i]= UName
        filterlist['NComments'][i]= user

"Converting filtered data to csv file"
filterlist.to_csv('Most_Commented_greater50com_list_NML.csv',encoding='utf-8',index=False)

"Reading the file to get whole information of who commmeted more than 50 comments"
Sortedcomments=pd.read_csv('4.Most_Commented_greater50com_list_NML.csv')

Sortedcomments.head()

"For loop for getting whole infomation of who commmeted more than 50 comments from cleaned data"
for i, name in enumerate(Sortedcomments['Username']):
    print(name)
    (dataset[dataset['user']==name]).to_csv(f'{i}_{name}_Label.csv')
    print(f'Successfully {i}_{name}_label.csv file was created')
    








