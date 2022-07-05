import pandas as pd
import numpy as np

excel_file = 'sample_scores.xlsx'
df = pd.read_excel(excel_file)

print(df)