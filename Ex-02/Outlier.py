import pandas as pd
from scipy import stats
import numpy as np

df=pd.read_csv("weight-height.csv")
print(df.head())
df=df.drop("Gender", axis=1)

z=np.abs(stats.zscore(df))
df1=df.copy()
# df.boxplot()
df2=df.copy()

q1 = np.percentile(df, 25, interpolation = 'midpoint')
q2 = np.percentile(df, 50, interpolation = 'midpoint')
q3 = np.percentile(df, 75, interpolation = 'midpoint')

print('Q1 25 percentile of the given data is, ', q1)
print('Q1 50 percentile of the given data is, ', q2)
print('Q1 75 percentile of the given data is, ', q3)

IQR = q3 - q1
print('Interquartile range is', IQR)

low_lim = q1 - 1.5 * IQR
up_lim = q3 + 1.5 * IQR
print('low_limit is', low_lim)
print('up_limit is', up_lim)

df2_new=df2[((df2>=q1-1.5*IQR)&(df2<=q3+1.5*IQR)).all(axis=1)]
# df2_new.boxplot()