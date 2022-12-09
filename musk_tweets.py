import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Overview
df = pd.read_csv('rawdata.csv')
print(df.head())
print(df.info())
print(df.describe())

'''
Things I want to do:
clean data -> make date and time col
           -> clean tweet with NLP

EDA on clean data
most common time for tweets
most retweeted tweet
most tweeted about thing
'''
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}

df['Date'] = pd.to_datetime(df['Date'])
df['Hour'] = df['Date'].apply(lambda time: time.hour)
df['DoW'] = df['Date'].apply(lambda time: time.dayofweek)
df['DoW'] = df['DoW'].map(dmap)
print(df.head())


# Exploritory data analysis
#sns.pairplot(data=df, y='Retweets')