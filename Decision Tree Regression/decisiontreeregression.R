#install and load the required package
install.packages("rpart", repos = "https://cloud.r-project.org")
library(rpart)

#sample data
data <- data.frame(
    hours=c(1,2,3,4,5,6,7,8),
    attendance=c(60,65,70,75,80,85,90,95),
    pass=as.factor(c("no","no","no","no","yes","yes","yes","yes"))
)
#train the decision tree model1        rpart() uses pruning and stopping rules when constructing a decision tree
model<- rpart( 
  pass ~ hours + attendance,
  data = data,
  method = "class",
  control = rpart.control(cp = 0.001)
)
#predict on training data
predicted <- predict(model,data,type="class")
#show prediction
print(predicted)
#evaluation= confusion matrix
table(predicted=predicted,actual=data$pass)

confusion <- table(predicted, data$pass)

accuracy <- sum(diag(confusion)) / sum(confusion) * 100

print(paste("Accuracy:", accuracy, "%"))
