lucky_numbers = [3, 7, 12, 23, 28, 31]
friends = ["Kevin", "Raquis", "Rock Lee", "Pooface Mcgee", "AHHHH"]

friends.extend(lucky_numbers) #Adds two lists together
friends.append("Creed") #Adds an extra element onto the end of the list
friends.insert(1, "Karen") #Adds an element at a certain position.
friends.remove("Kevin") #Removes a certain element from the list
friends.clear() #Resets the list completely
friends.pop() #Removes the last element in the list


print(friends.index("Rock Lee")) #Tells the index of a certain element
print(friends.count("Kevin")) #Tells how much the value shows up in the list

friends.sort() #Sorts elements alphabetically/ascending 
print(friends)

lucky_numbers.reverse() #Sorts list from descending
print(lucky_numbers)

friends2 = friends.copy() #Copies a list
print(friends2)
