"Import Necessary Files"
import os
import glob
import pandas as pd

"Change the directory where working files placed"
os.chdir("D:\\Ramisha_Practice\\NLP\\NLP_Python\\CSV")

extension = 'csv'

"Merging all the collected files as one file "
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
combined_csv = pd.concat([pd.read_csv(f,error_bad_lines=False) for f in all_filenames ])

"Checking length of merged file"
len(combined_csv)
#export to csv
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')