#Read from external files in Python
#To open file, use open. Store inside a variable

employee_file = open("employees.txt", "r") #Both files in same directory

#print(employee_file.readable())         #.readable tells you if you can read from the file
#print(employee_file.read())             #.read gives you all the information in the file
#print(employee_file.readline())         #.readline reads a specific line
                                         #If you copy and paste .readline again it will read the next line

#print(employee_file.readlines()[1])     #Will take all lines in file and put them into a list                                    
                                         #Can get specific line from the list with []    

#Can use .readlines inside a for loop and it'll print out each line inside the file

for employee in employee_file.readlines():
    print(employee)


employee_file.close()                    #Must always close file when done






#"r" stands for read. Just want to read info in file
#"w" write. Allows you to edit information in the file.
#"a" = appends. Add new information into the file
#"r+" read and write
