import pandas as pd
#Series                         #1D data sstructure
s=pd.Series([10,20,30,40])      #1D data sstructure
print(s)
#if i dont want the index to be like 0,1,2,3,4,
a=pd.Series([50,60,70,80],index=['a','b','c','d'])
print(a)


#DataFrame        #2d data structure
data={'Name':['Suhan','Shrayasi'],'Age':[19,20]}
df=pd.DataFrame(data)
print(df)

#dataframe from dictionary
datas={'name':["Suhan","shrayasi","antasree","tannistha"],'age':[19,20,20,21],'code':['A','B','C','D']}
dh=pd.DataFrame(datas)
print(dh)

#dataframe from list of 2 dictionaries
hehe=[{'a':1,'b':2},{'a':3,'b':4}]
de=pd.DataFrame(hehe)
print(de)