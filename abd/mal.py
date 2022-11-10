# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:55:42 2022

@author: cse
"""

import pandas as pd
import matplotlib.pyplot as p
df=pd.read_csv('C:/Users/cse/Documents/athlete_events.csv')
print(df.head())
p.hist(df['Age'])
p.show()
df[df['Sex']=='M']['Medal'].value_counts().plot(kind='bar')
p.scatter(df['Height'],df['Weight'])
p.xlabel('Height')
p.ylabel('Weight')
df[df['Year']==2000]['Medal'].value_counts().plot(kind='bar')