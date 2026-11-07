#       dictionaries:- it is the unordered collection of key & value pairs
#creation
my_dict={"name":"Suhan","age":19,"cgpa":9.8}
print(my_dict)
print(my_dict["name"])

#adding and updating
my_dict["GOAT"]="Suhan"
print(my_dict)
my_dict["cgpa"]=9.9
print(my_dict)
my_dict["age"]=20
print(my_dict)

#deleting
del my_dict["GOAT"]
print(my_dict)

#iterating
for key,value in my_dict.items():
    print(key,value)

