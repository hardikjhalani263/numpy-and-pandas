# (1) write a statment to import numpy ?

# import numpy loads the NumPy library.
# as np is an alias, so instead of typing numpy.array(), you can simply write np.array().

# (2)creat an array using numpy ?
# import numpy as np

# #creating a numpy array
# arr = np.array([1, 2, 3, 4, 5])

# print("Numpy Array:", arr)

# (3) creating an array of 10 random integers ?
# import numpy as np

# arr = np.random.randint(1, 101,10)

# print("Random Integer Array:", arr)

# (4) creating an array of element from 10-20?

# import numpy as np
# arr = np.arange(10, 21)   # 21 is exclusive
# print("Array from 10 to 20:", arr)

# (5) creating an array which contain value 5,10 time ? 
# import numpy as np

# arr = np.full(10, 5)
# print("Array:", arr)

# (6) create a one dmensional array and convert than into 3*3 matrix ?
# import numpy as np

# arr = np.arange(1, 10)   
# print( arr)

# matrix = arr.reshape(3, 3)
# print( matrix)

# (7) creat a 2d array of size 3*3 but all the elements should be between 0 to 1 ? 

# import numpy as np

# arr = np.random.rand(3, 3)   
# print(arr)

# (8) concatenate 2D array horizontally and vertically ?
# import numpy as np
# a = np.arange (1,5)
# b = np. arange(5,9)
# c =np.arange(9,13)

# print (np.hstack((a,b,c)))
# print (" it is a horizontally ")
# print (np.vstack((a,b,c)))
# print (" it is vertically ")