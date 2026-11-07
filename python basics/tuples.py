# tuple:- ordered and immutable in nature, can contain diff types of data and duplicates aswell
my_tuple=("hi",5,25.52,False)
print(my_tuple)

#immutable:
# my_tuple[0]=2
# print(my_tuple)

#indexing:
print(my_tuple[-1])
print(my_tuple[2])

#tuple unpacking
tuple2=(1,2,3,4)
a,b,c,d=tuple2
print(b)
print(d)

#tuple iteration
tup=(5,6,7,8)
for x in tup:
    print(x)

#concatenation of tuples
tup1=(1,2,3,4,5)
tup2=(6,7,8,9,10)
print(tup1+tup2)
#or
tup3=(tup2+tup1)
print(tup3)

#tuple deletion
tup=(69,67)
del(tup)
print(tup)