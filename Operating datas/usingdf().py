import pandas as pd
df=pd.read_csv('D:/Btech CSE/AI_MachineLearning/imported datasets/Copy of diabetes.csv')
print(df.head())    #prints first 5 datas in the dataset
print(df.tail())    #prints last 5 datas in the dataset
print(df.info())
print(df.shape[0]) #tuple bole [0]= it gives rows
print(df.shape[1]) #[1] it gives no. of columns