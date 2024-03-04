import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
data_csv = pd.read_csv('https://raw.githubusercontent.com/Nikhilg04/strokes/main/brain_stroke.csv', header=None)

print(data_csv.head())
