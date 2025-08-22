import pandas as pd
# df = pd.read_csv(r'C:\Users\hp\pandai\covid_toy - covid_toy.csv')
# print (df)

# how can we check top 5 data ? 
# print (df.head())

# how can we check last data ? 
# print (df.tail()) 

# how can we check total column name in a dataframe ? 
# df.shape 

# how can we check total column name in a dataframe ?
# print (df.columns)

# how can we check random indexed data ?
# print(df.sample(3))

# data frame is numtable 
# print(df.head(5))

# df['gender'][0] ='Female'
# df.head()

# how can we check statically view of data ? 
# print (df.describe())

# how can we check over all information of our dataframe?
# print (df.info())

# loc() and iloc() method 
# df.loc[row_range , column_name] -----> last index value will include .
# df.iloc[row_range , colume_range ] ------> last index value will exclude .

# print(df.loc[5:8,['age' , 'gender' , 'has_covid']]) 

# print (df.iloc[5:8 , [0,1,2,3,4]])

# if you want to check total sub_categories frequency in a column then we can use .
# pd.value_counts()

# print(df['gender'].value_counts())

# print(df['cough'].value_counts())

# print(df['city'].value_count())

# print(df['has_covid'].value_counts())

# how can we check missing values in a dataframe ?
# print (df.isnull().sum())

# a =df
# how can we drop the missing raws ?

# a = a.dropna()

# print (a.isnull().sum())

# print (a.shape)

# how can you fill the missing data?
# df['col'] ----> numerical -----> column's mean fill 
# df['col'] ----> categorical ----> column's most frequency value fill 

# print (df['fever'].mean())

# df['fever'] = df['fever'].fillna(df['fever'].mean())
# print (df.insull().sum())

# print(df.shape)

# print (df ['has_covid'].mode())

# print(df['has_covid'].value_counts)



df = pd.read_csv(r'C:\Users\hp\pandai\insurance - insurance.csv')
# print (df)

# print (df.head())
# print (df.tail())

# print(df.shape)

# print (df.columns)

# print (df.sample(3))

# print(df.head(5))

# df['sex'][0] ='Female'
# df.head()

# print (df.describe())

# print (df.info())

# print (df.loc[5:8,['age' , 'bmi' , 'children' , 'smoker']])

# print (df.iloc[5:8 , [0,1,2,3,4]])

# pd.value_counts()

# print(df['age'].value_counts())

# print(df['sex'].value_counts())

# print(df['smoker'].value_counts())

# print(df['region'].value_counts())

# print(df['children'].value_counts())

# print(df['charges'].value_counts())

# print (df.isnull().sum())

a = df 

a =a.dropna()

print (a.isnull().sum())

print (a.shape)