import numpy as np
#                                       indexing using numpy


arr=np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr[1,2])

#                                       slicing using numpy
print(arr[0,:])
print(arr[1,:])


#                                   array operations in numpy
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
c=np.array([[1,0],[0,-1]])
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b**3)
print(a**4)
Trans_c=arr.T
print(Trans_c)

#comparison bool
ab=np.array([1,2,3,4])
print(ab<=3)
print(ab==3)

#mathematical ops using numpy
print(np.sqrt([1,4,9]))

print(np.exp([1,2,3]))

print(np.sin([0,np.pi/2]))


#broadcasting
shrayasi=np.array([[1],[2],[3]]) #3d array
suhan=np.array([1,2,3]) #1D array
print(shrayasi+suhan)

#reshaping matrics
bhetki=np.array([[1,2],[3,4],[5,6]])
print(bhetki)
print(bhetki.reshape(2,3))
print(bhetki.flatten())

#bonus operations
sh=np.array([[1,2,3],[4,5,6]])
print(sh.ndim)
print(sh.sum()) #total sum of all the elems present in array
print(np.sum(sh)) #total sum of all the elems present in array
print(np.mean(sh)) 
print(np.max(sh))
print(np.min(sh))

su=np.array([[10,11,12],[13,14,15]])
print(su.ndim)
print(su)
print(su.dot(sh.T)) #MATRIX MUL=(COL OF FIRST * ROWS OF SEC)


print(np.random.seed(5))
print(np.random.rand(2,3))
print(np.random.randint(1,10,size=5))
