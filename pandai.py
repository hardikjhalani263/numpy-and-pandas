# pandas ----> pandas is the open sourch liabrary that is used gor handle data manipulations .
# data structure of pandas 
#  (1). series -----> it is 1-dimensional array and it return only value not column name
#  (2). dataFrame -----> it is multi-dimensional array and it return column name with value .

# series
import pandas as pd

# a = pd.Series([1,34,67,90])
# print (a) 

# print (type(a))

# dataFrame 

# a = {
#     "emp_id" : [1,2,3,4,5],
#     "Name" :['sam ' , 'raj' , 'rahul' , 'ankit' , 'pallavi'],
#     "Department ": [ 'it' , 'sales' , 'sales' , 'hr ' , 'HR'],
#     "Working_hours" : [8,8,8,9,9],
#     "salary" : [ 20000, 25000, 34000, 31000, 28000]
# }

# df = pd.DataFrame(a)
# print (df)

# how can we export this data into csv format ?
# print(df.to_csv("emp_data.csv " , index =False ))

# how can we export this data into excel format?

# df.to_excel("updated_emp_data.xlsx" , index = False)

# # how do you import excel data ? 
# a = pd.read_excel(" file address")

# how do you import csv data ?
# a = pd.read_csv(r"C:\Users\hp\pandai\emp_data.csv")
# print(a)

# a = pd.read_csv(r"C:\Users\hp\pandai\flipcartphone.csv")
# print (a)

# df = pd.read_csv(r"C:\Users\hp\pandai\covid_toy - covid_toy.csv")
# print (df.head(3))

# print (df.dtypes)

# df['age'] = df['age'].astype(float)

# df = df.dropna()
# print (df)

# print (df.filter(items = ['age' , 'gender']))  ### column wise filteration

# print (df[['fever' , 'has_covid']])

# print (df.loc[5:8])   ## for row wise filteration

# print(df.head(4))

# print(df.values)   ### it will return all the values

# a = df.columns

# a = a.to_list()

# a[0] = "updated_age"
# a[4] = "updated_city"

# print (a)

# new_df = pd.DataFrame(df.values , columns = a)

# print (new_df)

# second method 

# df.head(3)

# df = df.rename(columns = {"age":"latest_age" , "city":"latest_city"})
# print (df)

# Concatenation in Pandas ---> Using this method we can combine multiple dataframe .


# data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'],
#          'Age': [27, 24, 22, 32],
#          'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#          'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}
# df1 = pd.DataFrame(data1 , index = [0,1,2,3])

# data2 = {'Name': ['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
#          'Age': [17, 14, 12, 52],
#          'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#          'Qualification': ['Btech', 'B.A', 'Bcom', 'B.hons']}
# df2 = pd.DataFrame(data2 , index = [4,5,6,7])

# a = [df1,df2]

# print(pd.concat(a))


# df1 = pd.DataFrame(data1 , index = [0,1,2,3])
# df2 = pd.DataFrame(data2 , index = [4,5,6,7])

# res2 = pd.concat([df1, df2], axis=1, join='outer')
# print(res2)

# Ignore_Index  ---> the indexes of the original DataFrames may not be relevant.
# We can ignore the indexes and reset them using the ignore_index argument.

# df1 = pd.DataFrame(data1,index=[0, 1, 2, 3])
# df2 = pd.DataFrame(data2, index=[2, 3, 6, 7])

# res = pd.concat([df2, df1], ignore_index=True)
# print(res)

# frames = [df1, df2 ]

# res = pd.concat(frames, keys=['x', 'y'])
# print(res)

# # Concat Mix data
# We can also concatenate a mix of Series and DataFrames. If we include a Series in the list,
# it will automatically be converted to a DataFrame and we can specify the column name.

# data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],
#         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#         'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

# df1 = pd.DataFrame(data1,index=[0, 1, 2, 3])
# s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')

# a = pd.concat([df1,s1]  , ignore_index=True)
# print(a.columns)

# a = a.rename(columns = {0:"Salary"})
# a.head(3)

# a['Salary'].mean()

# a['Salary'] = a['Salary'].fillna(a['Salary'].mean())

# a['Address'][4:8] = 'Jaipur'

# a.isnull().sum()

# a['Age'] = a['Age'].fillna(a['Age'].mean())

# print(a)

# data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],}

# data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#         'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

# Perform merginig based on key

# res = pd.merge(df1, df2, on='key')
# print (res)


# ----->  Merginig with different keys

# data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'key1': ['K0', 'K1', 'K0', 'K1'],
#          'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
#         'Age':[27, 24, 22, 32],}

# data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
#          'key1': ['K0', 'K0', 'K0', 'K0'],
#          'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
#         'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

# res1 = pd.merge(df1, df2, on=['key1', 'key'])
# print (res1)

# -------->  Joins using merginig
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],}

data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
# left joint 
res = pd.merge(df1, df2, how='left', on=['key', 'key1'])
print (res)





# EDA ----> Exploratory Data Analysis

# (1). Descrete Data ---> We cannot dividie furthur in more specific  parts .
# Ex. fever(yes,no) , martial status(yes, no) , total number of employees in a office(500,501)
# (2). Continous Data  ---> We can divide frthur in more specific parts .
# Ex. date_of_birth , distance , weight , height

# (1). Univariate Analysis ---> Perform operation on single column .
# (2). Bivariate Analysis  ---> Perform operation on 2 columns .
# (3). Multivariate Analysis  ----> Perform operation on more than 2 columns

# Data Visualization Libraries
# Matplotlib
# Seaborn

# df = pd.read_csv(r'C:\Users\hp\pandai\titanic.csv')
# # print (df.head(3))

# import matplotlib.pyplot as plt 
# import seaborn as sns

# # (1). Univariate Analysis
# print (df['Survived'].value_counts())
# sns.countplot(x = df['Survived'])

# # print (df['Survived'].value_counts().plot(kind = 'pie' , autopct= "%.2f"))
# # print (df['Pclass'].value_counts().plot(kind = "bar"))

# plt.hist(x = df['Age'])
# print(df['Fare'].isnull().sum())
# df['Fare'] = df['Fare'].fillna(df['Fare'].mean())