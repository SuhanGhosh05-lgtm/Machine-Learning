data=data.frame(Experience=c(1,2,3,4,5),EducationLevel=c(10,12,14,16,18),Salary=c(25000,40000,80000,120000,150000))
model <- lm(Salary ~ Experience+EducationLevel,data=data) #linear regression
new_data<-data.frame(Experience=c(6,7),EducationLevel=c(21,22))
predicted_salary<-predict(model,newdata=new_data)
print(predicted_salary)    
# 6>  1      7>   2 
#   182000     215000 

#for plotting
library(ggplot2)
p <- ggplot(data, aes(x = Experience, y = Salary)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE, color = "red") +
  ggtitle("Linear Regression Line") +
  xlab("Experience (Years)") +
  ylab("Salary")
print(p)

train <-data[1:4,]
test<- [5,]