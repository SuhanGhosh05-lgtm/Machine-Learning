import pandas as pd
data={'Name':['Suhan','Shrayasi','Antasree','Tannistha','chintu'],
      'Age':[19,20,20,21,15],
      'Score':[1,2,3,4,0]}
df=pd.DataFrame(data)
print(df)

#extracting one col out of data frame
print(df['Name'])
print(df['Score'])
print(df[['Name','Age']]) #for multiple cols multiple sq bracks
print(df[['Name','Score']])

#extracting one row out of data frame
print(df.iloc[0])
print(df.iloc[1])

#slicing      last one is not included in slicing
print(df[0:2])
print(df[1:3])
print(df[2:4])


print([df['Age']<21])
print((df['Age']<21) & (df['Score']<3))

#to check null values
print(df.isnull())

#to remove null values
print(df.dropna())

#fill null values with 0
print(df.fillna(5))

#replace columns and rows
print(df.rename(columns={'Name':'Full name'},inplace=True))

#replace
print(df.replace('Tannistha','chashmish',inplace=True))

#mean
print(df['Age'].mean())
#median
print(df['Age'].median())
#SUM
print(df['Age'].sum())
#min
print(df['Age'].min())
#max
print(df['Age'].max())
#sort
print(df.sort_values(by='Age')) #ascending
print(df.sort_values(by='Age',ascending=False))#desccending
print(df.sort_values(by='Full name'))

#groupby
# print(df.groupby('Full name')['Age'])



#bonus operations

#Merging 2 dataframe
df1=pd.DataFrame({'id':[1,2,3],
                  'name':['Suhan','Shrayasi','Antasree']})
df2=pd.DataFrame({'id':[1,2,3],
                  'score':[90,89,85]})
merged=pd.merge(df1,df2)
merged=pd.merge(df1,df2,on='id') #merge with criteria
print(merged)
#concatenating
concat=pd.concat([df1,df2],axis=0)#axis =0 is for row wise concat
concat2=pd.concat([df1,df2],axis=1)#axis=1 is for column wise concat
print(concat) #concatenation happens row wise with null vals
remove_null_concat=concat.dropna() #remove nulls row wise
print(remove_null_concat)           # will produce empty data frame
remove_null_concatenation=concat2.dropna() #remove nulls col wise
print(remove_null_concatenation)


#file handling
#to read 
df=pd.read_csv('file_name.csv')
df=pd.read_excel('file_name.xlsx')
#saving dataframes into files
df.to_csv('file_name.csv',index=False)
df.to_excel('file_name.xlsx',index=False)
