#Data preprocessing
#dataframe[rows, columns] this is the syntax in R

data <- data.frame(
	Name=c("a","b","c"),
	age=c(13,15,17),
	score=c(19,18,17)
)
print(data)
#now we are checking if there are any null values or not
colSums(is.na(data))  #in this case there are no missing values

hehe <- data.frame(
	Name=c("a","b","c",NA),
	age=c(NA,15,17,18),
	score=c(19,18,17,NA)
)
print(hehe)
colSums(is.na(hehe)) #name-1 miss val, age-1 miss val, score-1miss val

#to remove all the missing values
cleaned_data<-na.omit(hehe)
print(cleaned_data)

#to fill the missing values, we use data imputation
hehe$age[is.na(hehe$age)]<-mean(hehe$age,na.rm=TRUE) #if there is null in age, replace it with mean, if null in age, remove, put mean
print(hehe)

#sorting
sort<-hehe[order(hehe$age, decreasing=TRUE),]  #sorting age in descending order
print(sort)
sort<-hehe[order(hehe$age, decreasing=FALSE),] #sorting age in ascending order
print(sort)

#math ops, onlu works when hehe is numerical datas not strings
# print(rowSums(hehe))
# print(colSums(hehe))
# print(rowMeans(hehe))
# print(colMeans(hehe))



