#                           LOOPS
for sex in range(0,6):
    print(sex)

i=0
while(i<=5):
    print(i)
    i+=1

for i in range(1,11):
    if i==5:
        break
    print(i)    


for a in range(1,6):
    if a==3: #current iteration/ oi no. ta sskip kore print hobe
        continue
    print(a)

for i in range(1,6):
    print(i)
else:
    print("loop completed")

list=["apple","guava","chilli"]
for x in list:
    print(x)

for i in range(1,21):
    if(i%2==0):
        print(i)

for x in range(1,21):
    if(x%2!=0):
        print(x)


i=1
sum=0
while i<=5:
    sum+=i
    i+=1
    print(sum)

i=1
sum=0
while i<=5:
    sum+=i
    i+=1
print(sum)
