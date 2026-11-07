
#  list:-mmutable/changebale, duplicates are allowed in list can contain diff types of data and duplicates aswell
lists=["apple","cherry","banana", 1, True, 69.67]
#acessing through indexing
print(lists[2])
print(lists[-2])

#adding to list
lists.append("orange")
print(lists)

#removing from list
lists.remove("cherry")
print(lists)

#iterating through lists
for list in lists:
    print(list)

#length of fruits
print(len(lists))

#existence of element in list
print(1 in lists)
print("cherry" in lists)
