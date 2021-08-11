number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]                                   #4 elements inside list which are all themselves lists. 

#print(number_grid[0][0]) #Access grid and print certain number 

for row in number_grid:
    #print(row)                     Prints all rows
    for col in row:
        print(col)                  #Access each individual value inside array elements
