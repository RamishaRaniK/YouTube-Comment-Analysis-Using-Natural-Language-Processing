
#have to open folder
import os
import pandas as pd

os.chdir('D:\\Ramisha_Practice\\50 commets')

os.chdir('D:\\Ramisha_Practice\\50_c0mment_label')

results=[]

#write for loop for finding pos and negtive for each file
import glob
extension='csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]


for filename in all_filenames:
    print(filename)
    dataset=pd.read_csv(filename,encoding='utf-8-sig')
    result=dataset['comp_score'].value_counts()
    print("result")
    results.append([filename,result])
    print("appended")

print(results)


Each_sub_pos_Neg=pd.DataFrame(results)


Each_sub_pos_Neg.to_csv('Each_Sub_Sup_PosNeg_ML.csv', index=False)


