import pandas as pd
import numpy as np

excel_file = 'sample_scores.xlsx'
df = pd.read_excel(excel_file)

#print(df)


scorer = df['Name'].where(df['Test 1']==74)
print(scorer.dropna())

excel_files = ['sample_scores.xlsx','sample_scores2.xlsx','sample_scores3.xlsx']
for individual_excel_file in excel_files:
    df = pd.read_excel(individual_excel_file)
    scorer = df['Name'].where(df['Test 1']==74).dropna()

    print('File Name:' + individual_excel_file)
    print(scorer)