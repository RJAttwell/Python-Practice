#This exercise allows us to catch and handle errors

#number = int(input("Enter a number: "))
#print(number)                              

#If you don't enter a number, code doesn't work
#Use try/except block

try:
    number = int(input("Enter a number: "))
    print(number)   
except ZeroDivisionError as err:           #Catch specific errors by putting multiple excepts
    print(err)                             #Can store error as variable
except ValueError:
    print("Invalid Input")