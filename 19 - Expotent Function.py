#Expotent Function allows to take a certain number and raise to a specific power

#print(2**3)

#Using for loops we can do the calculation above 

def raise_to_power (base_num, power_num): #2 parameters
    result = 1 #defining variable. Store result of the math.
    for index in range(power_num): #Specify for loop. Loop through range of numbers.
        result = result * base_num 
    return result

print(raise_to_power(2, 3))

