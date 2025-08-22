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

a = pd.read_csv(r"C:\Users\hp\pandai\flipcartphone.csv")
print (a)