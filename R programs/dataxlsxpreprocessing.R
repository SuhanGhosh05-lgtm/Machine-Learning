.libPaths(c(Sys.getenv("USERPROFILE"), .libPaths()))
library(readxl)

#loading datasset
data <- read_excel("D:/Btech CSE/AI_MachineLearning/imported datasets/data.xlsx")

#exploring dataset
print(dim(data))
print(head(data))

#descriptive statstics
print(summary(data))

#data cleaning
#The as.numeric() function ensures that the Age and Fare columns are treated as numeric values for further analysis.
data$Age <- as.numeric(data$Age)
data$Fare <-as.numeric(data$Fare)

#Handling missing values
data$Age[is.na(data$Age)<-median(data$Age,na.rm=TRUE)]
data$Sex[is.na(data$Sex)]<-"Male"

#feature scaling, 2 methods, standardization, normalisation

#Scaling This method is useful when features have different units. The scale() function standardizes
#the Fare column by converting it to have a mean of 0 and a standard deviation of 1 which is
#essential for models that rely on distance metrics.
                                                    #Scaling:-
data$Fare<-scale(data$Fare)
data$Age<-scale(data$Age)
#Normalisation:-Normalization scales the data to a fixed range, usually [0, 1]. This is useful when features
#need to be within a specific range for machine learning algorithms.
                                                    #Normalization
data$Fare<-(data$Fare - min(data$Fare)) / (max(data$Fare) - min(data$Fare))
print(data$Fare)

#                                               ENCODING
#                                                   One Hot encoding
#One-hot encoding creates binary columns for each category in a categorical variable.
# model.matrix() creates binary columns for each level of the Sex column and cbind()
# combines these columns with the original data.
>encoded_data <- cbind(data, model.matrix(~ Sex - 1, data))

#                                                        Ordinal Encoding
# Ordinal encoding is used for categorical variables with an inherent order. We can assign
# numerical values based on the order of categories. We assign numerical values to the
# categories "male" and "female" based on their order and replaces the categorical values in
# Sex with the corresponding numeric values.
>mapping <- c("male" = 0, "female" = 1)
>data$Sex <- mapping[data$Sex]


#                                                      Handling Outliers
# Outliers can distort statistical analyses and machine learning models. We can use box plots to
# detect and handle outliers. We will define an Interquartile Range (IQR) for Fare column and
# removes values outside of the calculated bounds.
>boxplot(data$Fare,main="Before Removing Outliers")
>IQR_value <- IQR(data$Fare)
>lower_bound <- quantile(data$Fare, 0.25) - 1.5 * IQR_value
>upper_bound <- quantile(data$Fare, 0.75) + 1.5 * IQR_value
>data <- data[data$Fare >= lower_bound & data$Fare <= upper_bound, ]
>boxplot(data$Fare, main="After Removing Outliers")



