for letter in "Richard Attwell":           #Specify a variable that is used on each variation of our for loop. Will change value every time.
    print(letter)                          #For loop with a string


friends = ["Jason", "Karen", "Kevin"]      #For Loop with an array
for friend in friends:
    print(friend)

for index in range(len(friends)):
   print(friends[index])
    

for index in range(5):                      #If you wish to do something on the first iteration of a loop
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")