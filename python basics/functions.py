#   Functions
name=input()
def greet():
    print("Hello"+" "+name)
greet()

def add(a,b):
    return a+b
print("Sum is:-",add(5,5))

def mul(a,b,c):
    return a*b*c
print("Mull:-",mul(5,4,3))

def greet(name="Suhan"):
    print(f"Welcome,{name} !")
greet("chintu")

def profile(name,age):
    print(f"Name:{name},Age:{age}")
profile("chintu",20)

def total(*numbers): #*=no. of arguments
    return sum(numbers)
print(total(1,2,3,4,5,6,7,8))

def displayinfo(**info):
    for key,value in info.items():
        print(key,value)
displayinfo(name="suhan",year=2,age=19)

def calc(a,b):
    return a+b,a*b
sum_val,prod_val=calc(4,5)
print(sum_val,prod_val)

def findmax(lst):
    return max(lst)
print(findmax([69,12,14,62,81,34,62,53,1]))
