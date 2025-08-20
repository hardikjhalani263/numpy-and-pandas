# Introduction to Numpy  ---->
# Numpy is an open-source library that is used for scintific calculations .

# Why Numpy is better than List ?
# (1). Numpy is homogeneous data type and List is hetrogeneous data type .
# (2). Numpy is faster as compare to List .
# (3). Numpy take Less memory as compare to List .
# (4). If we apply any operations on an array then the operation will implement on all the values of an array
# but if we apply any operation on a list then it will replicate it .

import numpy as np 

# a = np.array([1,45,78,90])
# print(a)
# type(a)

# a.ndim

# p = [[1,2,3,5],[4,5,6,3],[7,8,9,10]]
# q = np.array(p)
# print(q)

# print("Total Dimension = " , q.ndim)
# print("Total rows and columns = " , q.shape)
# print("Total Elements =" , q.size)


# r1 = [1,2,3]
# r2 = [4,5,6]
# r3 = [7,8,9]
# c1 = [1,4,7]
# c2 = [2,5,8]
# c3 = [3,6,9]

# (1). zeros() ----> It will create an array in which all the values will be zero either in one-dimensional
# or multi-dimensional .

# a = np.zeros(4)
# print(a )

# a = np.zeros((3,4))
# print(a)

# (2). ones() ----> It will create an array in which all the values will be one .

# a = np.ones(4)
# print(a)

# a = np.ones((2,3))
# print(a)

# (3). eye() ---> It will create an array in which digonal positional elements will be 1 and
# rest all are 0 .

# a = np.eye(4)
# print(a)

# (4). diag() ----> Using this method , we can set our custom elements on digonal position .

# a = np.array([1,45,78,90])
# print(a)

# b = np.diag(a)
# print(b)

# (5). Random Module
# (a). Randint() ----> It will generate random numbers in a given range .

# a = np.random.randint(1,10,3)
# print(a)

# (b). Rand() ----> It will generate random numbers between 0-1 .

# Data ---> column add (random numbers) ---> model perforamcne 80% ---> after refresh ---> number update --->
# Model Perfrmance 50%

# (c). seed() ----> It will lock or fix your random generated data .

# np.random.seed(54)
# a = np.random.randint(1,10,4)
# print(a)

# view vs copy

# view means modification in original data.
# copy means create a duplicate data and when we change into it then it will not
# reflect original data .
# a = np.array([10,20,30,40,50,60,70,80])
# print (a)

# b = a[2:5]
# b [:]=0

# a = np.arry([10,20,30,40,50,60,70,80])
# print(a)

# b = a[2:5].copy()
# b[:] = 0

# reshaping the array

# a = np.random.randint(1,50,12)
# print(a)

# 12 element combination
# 1*12 , 12*1
# 2*6  , 2*6
# 3*4   , 4*3

# a.reshape(2,6)
# a.reshape(3,4)


# a = np.random.randint(1,100,36)
# print(a)

# a.reshape(2,18)
# a.reshape(4,9)
# a.reshape(6,6)

# operations on array
# a = np.arange(1,12,1)
# print(a)

# a = np.arange(1,20,3)
# print (a)

# a = np.arange(1,16)
# print(a)

# print (a >10)

# b = a>10
# a[b]

# a<5

# b = a<5
# a[b]

# a = np.arange(1,5).reshape(2,2)
# print(a)

# b = np.arange(5,9).reshape(2,2)
# print(b)

# print(a+b)
# print(a-b)
# print(a*b)

# print(a.dot(b))

# print( a/b)

# print (a)

# print(a*2)
# print(a**2)
# print(a**3)

# a =np.arange(1,10).reshape(3,3)
# print(a)
# print (np.sum(a))

# it we want only row wise sum 
# np.sum(a , axis = 1)

# if we want only colum wise sum
# np.sum (a , axis=0)

# unique() ----> it will remove duplicate element from array and it returns 3 array
# arr ----> return array of unique value 
# return_index = true -----> return array of unique index value 
# return_counts = true ----> return array of each unique value  frequency

# arr = np.array([10, 20, 30, 10, 10, 10, 10, 20, 20, 20, 20, 50])  
# print(arr)

# print(np.unique(arr , return_index=True , return_counts=True))

# linespace() ----> it will return an array in which we will get same gap of value.
# a = np.linspace(1,2,5)
# print(a)

# Hstack() and vstack() ----->  hstack () will combin all the arrays in horizontally
# while vstack() will combine all the array in vertically

# a = np.arange (1,5)
# b = np. arange(5,9)
# c =np.arange(9,13)

# print (np.hstack((a,b,c)))

# print (np.vstack((a,b,c)))


# full method and randim24 method 
