secret_word = "Glove"
guess = "" #Stores the user's guess
guess_count = 0 #Inititally, user will not have guessed so it is 0
guess_limit = 3
out_of_guesses = False

print("Answer this riddle. One word answer.")
print("What has four fingers and a thumb, but is not alive?")

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        
if out_of_guesses:
    print("WRONG! You disgust me.")
else:
    print ("Dude, that is totally epic, you got it correct!")

