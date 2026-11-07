import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
print(arr.ndim)     #prints no. of dimension 
print(arr.shape)    #prints no. of rows and columns, this ex has 5 rows 0 columns
print(arr.size)     #prints the size of the array
print(arr.dtype)    #prints the data type

hehe=np.array([1235.3,2.6,4,3.4,5,436])
print(hehe)
print(hehe.ndim)     #prints no. of dimension 
print(hehe.shape)    #prints no. of rows and columns, this ex has 5 rows 0 columns
print(hehe.size)    #prints the size of the array
print(hehe.dtype)   #prints the data type

#creating 2d array and performing operations in it
a=np.array([[1,2],[3,4]])
print(a)
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)

#                   using functions to create numpy arrays
print(np.arange(0,10,3)) #(starting index, ending index(non inclusive), steps)
print(np.arange(0,10,1))
print(np.arange(100,0,-10))


print(np.linspace(0,1,5))           #(starting num, ending num, no. of values to be generated)


print(np.zeros((2,3)))            #to create arrays containing all 0 of 2X3 matrics

print(np.ones((3,4)))            #to create arrays containing all 0 of 3X4 matrics

print(np.eye(3))                #3X3 er identity matric create korbe

print(np.eye(5))                #5X5 er identity matric create korbe
