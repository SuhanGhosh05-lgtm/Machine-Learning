# Keyword	Purpose
# try	    Contains code that might cause an error.
# except	Executes if a matching error occurs in the try block.
# else	    Executes only if no exception occurs in the try block.
# finally	Executes whether an exception occurs or not.

try:
    a=int(input("Enter a int:-"))
    print(10/a)
except ZeroDivisionError:
    print("No. cant be divided by 0")
except ValueError:
    print("invalid input")
else:
    print("success")
finally:
    print("execution completed")
