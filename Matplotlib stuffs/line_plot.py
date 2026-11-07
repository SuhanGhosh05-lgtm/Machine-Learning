import matplotlib.pyplot as plt
#line plotting
x=[1,2,3,4,5]
y=[10,12,8,14,16]
plt.plot(x,y)
plt.show()
#title
a=[1,2,3,4,5]
b=[10,12,8,14,16]
plt.title('customised Line Plot')
plt.xlabel('time')
plt.ylabel('value')
plt.plot(a,b,color='Purple',linestyle='--',marker='o',linewidth=2) #marker is the point of intersection of elems of x and y axis
plt.show()

#bar chart with certain categories and values
categories=['A','B','C','D','E']
values=[10,24,2,15,11]
plt.bar(categories,values,color='red')
plt.title('Bar Graph')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()

#scatter plot
g=[12,42,54,23,13,1]
f=[2,3,4,6,7,8]
plt.scatter(g,f,color='violet',marker='*')
plt.xlabel('G')
plt.ylabel('F')
plt.show()