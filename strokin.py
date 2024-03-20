import pandas as pd
import ssl
import matplotlib as mpl
import numpy as np

ssl._create_default_https_context = ssl._create_unverified_context
data_csv = pd.read_csv('https://raw.githubusercontent.com/Nikhilg04/strokes/main/brain_stroke.csv')

gender = data_csv['gender']
age = data_csv['age']
hypertension = data_csv['hypertension']
heart_disease = data_csv['heart_disease']
ever_married = data_csv['ever_married']
work_type = data_csv['work_type']
residence_type = data_csv['Residence_type']
avg_glucose_level = data_csv['avg_glucose_level']
bmi = data_csv['bmi']
smoking_status = data_csv['smoking_status']
stroke = data_csv['stroke']

