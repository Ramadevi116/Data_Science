import numpy as np
import pandas as pd
import seaborn as sns
df=pd.read_csv('supermarket.csv')
df.head()
df.info()
#DATA CLEANING PROCESS:
df.isnull().sum()
#OUTLIERS DETECTION AND REMOVAL
df.boxplot()
from scipy import stats
data=df.copy()
df=df.drop("Invoice ID", axis=1)
df=df.drop("Branch", axis=1)
df=df.drop("City", axis=1)
df=df.drop("Customer type", axis=1)
df=df.drop("Gender", axis=1)
df=df.drop("Product line", axis=1)
df=df.drop("Date", axis=1)
df=df.drop("Time", axis=1)
df=df.drop("Payment", axis=1)
z=np.abs(stats.zscore(df))
df2=df.copy()
q1=df2.quantile(0.25)
q3=df2.quantile(0.75)
IQR=q3-q1
df2_new=df2[((df2>=q1-1.5*IQR)&(df2<=q3+1.5*IQR)).all(axis=1)]
df2_new.boxplot()
#EXPLORATORY ANALYSIS
#STATISTICAL METHOD OF VIEWING THE DATA
data["Branch"].value_counts()
data["City"].value_counts()
data["Gender"].value_counts()
#CORRELATION
data.corr()
#GRAPHICAL METHOD OF DISPLAYING
sns.countplot(x='City',data=data)
sns.countplot(x='Customer type',data=data)
sns.countplot(x='Payment',data=data)
sns.displot(data["Time"])
sns.displot(data["Date"])
sns.countplot(x='Customer type',hue='Gender',data=data)
sns.countplot(x='Payment',hue='Gender',data=data)
#HEAT MAP
sns.heatmap(data.corr(),annot=True)