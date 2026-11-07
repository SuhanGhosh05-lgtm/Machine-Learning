# Create a personal library folder
dir.create(
  Sys.getenv("R_LIBS_USER"),
  recursive = TRUE,
  showWarnings = FALSE
)

# Install e1071 in your personal library
install.packages(
  "e1071",
  lib = Sys.getenv("R_LIBS_USER"),
  repos = "https://cloud.r-project.org"
)

# Load the package
library(e1071, lib.loc = Sys.getenv("R_LIBS_USER"))
data <-data.frame(Experience=c(1,2,3,4,5),Salary=c(5000,10000,15000,20000,50000))
svr_model<-svm(Salary~Experience,data=data,type="eps-regression")

new_data<-data.frame(Experience=c(2.5,5.5))
predicted_salary<-predict(svr_model,new_data)
print(predicted_salary)
plot(data$Experience,data$Salary,col='blue',main='SVR')
lines(data$Experience,pred(svr_model,data),col="red", ,lwd=2)
legend("topleft",legend=c("Actual","Svr pred"),col=c("blue","red"),pch=c(16,NA),lty=c(NA,1))