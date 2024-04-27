import pandas as pd
import ssl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
import researchpy as rp

ssl._create_default_https_context = ssl._create_unverified_context
data_csv = pd.read_csv('https://raw.githubusercontent.com/Nikhilg04/strokes/main/brain_stroke.csv')

df = pd.DataFrame(data_csv) # make it into a dataframe
df = df.dropna() # drop na values, but i don't think there are any

gender_count = df.groupby(['gender', 'stroke']).size().unstack(fill_value=0)
age_count = df.groupby(['age', 'stroke']).size().unstack(fill_value=0)
hypertension_count = df.groupby(['hypertension', 'stroke']).size().unstack(fill_value=0)
heart_disease_count = df.groupby(['heart_disease', 'stroke']).size().unstack(fill_value=0)
ever_married_count = df.groupby(['ever_married', 'stroke']).size().unstack(fill_value=0)
work_type_count = df.groupby(['work_type', 'stroke']).size().unstack(fill_value=0)
residence_type_count = df.groupby(['Residence_type', 'stroke']).size().unstack(fill_value=0)
avg_glucose_level_count = df.groupby(['avg_glucose_level', 'stroke']).size().unstack(fill_value=0)
bmi_count = df.groupby(['bmi', 'stroke']).size().unstack(fill_value=0)
smoking_count = df.groupby(['smoking_status', 'stroke']).size().unstack(fill_value=0) # this is big

# now data is in graphing format, can do something different if you want

