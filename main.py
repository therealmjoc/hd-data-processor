import pandas as pd

df = pd.read_csv('data/data.csv')

df.columns = [column.replace(" ", "_") for column in df.columns]

df['Pedigree_Status'] = df['Pedigree_Status'].str.replace(" ", "_")

print(df.query("Pedigree_Status == 'Birth_Notified'"))