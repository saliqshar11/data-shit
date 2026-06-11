import pandas as pd
import sqlite3

df = pd.read_csv('healthcare-dataset-stroke-data.csv')

print(df.head())
print(df.columns.tolist())
print(df.shape)

conn = sqlite3.connect('stroke.db')
df.to_sql('patients', conn, if_exists='replace', index=False)
conn.close()

print("Done. Database created")