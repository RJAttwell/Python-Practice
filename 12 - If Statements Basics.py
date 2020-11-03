 #Can have as much code as you wish in an if statement

is_male = True #Boolean Variable
is_tall = True

#if is_male:                                        #Give Condition
    #print("You are a Male") 

#else:
    #print("You are a Female")                      #Cover both conditions, true and false


#if is_male or is_tall:                             #or keyword means only one condition has to be true for this code to be executed
    #print("You are a Male, tall, or both")

#else: 
    #print("You are a neither a male nor tall.")
    

if is_male and is_tall:                             #and keyword means both conditions must be true
    print ("You are a tall male")

elif is_male and not(is_tall):                      #elif = else if 
    print ("You are male but not tall")

elif not(is_male) and is_tall:                      #not statement = Returns true if the condition is false
    print("You are not male but are tall")

else: 
    print ("You are either not male and not tall")




