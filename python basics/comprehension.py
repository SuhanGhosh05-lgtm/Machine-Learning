
#list comprehension
square=[x**2 for x in range(6)] #includes 0 automatically
print(square) 

even=[x for x in range(10) if x%2==0]
print(even)


#dictionary comprehension
square_dict={x:x**2 for x in range(6)}
print(square_dict)



odd_dict={x:x%2!=0 for x in range(11)}
print(odd_dict)


#set ccomprehension
uniqueno_set={x for x in range(11)}
print(uniqueno_set)


nums={a for a in[1,1,1,1,2,2,2,1,1,3,3,3,3,4,4,1,1,5,5,3,3,4,4,6]}
print(nums)