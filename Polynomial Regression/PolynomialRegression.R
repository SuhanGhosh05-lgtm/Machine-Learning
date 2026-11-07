#sample datas
data <- data.frame(
    level=1:10,
    salary=c(45000,50000,60000,70000,80000,90000,100000,120000,140000,150000)
)

model<-lm(salary~poly(level,2),data=data)
predicted<- predict(model,data)
plot(data$level, data$salary, main="Polynomial Regression", xlab="Level",ylab="Salary", col="Pink")
lines(data$level,predicted, col='Blue',lwd=20)