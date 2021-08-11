

#employee_file = open("employees.txt", "a")          #Add text onto the end of the file

#employee_file.write("\nKelly - Customer Service")   #\n puts information onto a new line

#employee_file.close()

employee_file = open("employees1.txt", "w")          #Can use "w" to overwrite a file
                                                     #Can also use it to create a new file
employee_file.write("AHHHHHH")                  

employee_file.close()


#Can also use it to create a new webpage.
#E.g: 
#Variable = open(index.html, "w")
#Variable.write("<p>This is HTML</p>")
#Variable.close()