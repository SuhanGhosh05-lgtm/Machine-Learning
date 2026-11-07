#sets:- unordered, mutable, unindexed collection of unique items
#it will return duplicate items only once, not all the duplicate times
my_set={1,2,3,4,5,1,2}
print(my_set) #last er 1,2 ta hobe na

#adding
my_set.add(436)
print(my_set)
my_set.add(4)
print(my_set)
my_set.add("abc")
print(my_set)

#deleting
my_set.remove(4)
print(my_set)

#set operations
set1={1,2,3,4,5}
set2={4,5,6,7,8,9,10}

set3=set1.union(set2)
print("Union:-",set1|set2)
print(set3)

set4=set1.intersection(set2)
print("intersection:-",set1 & set2)
print(set4)


set5=set1.difference(set2)
print("Difference(elem pres in set1 but not pres in set2):-",set1-set2)
print("Difference(elem pres in set2 but not pres in set1):-",set2-set1)
print(set5)
