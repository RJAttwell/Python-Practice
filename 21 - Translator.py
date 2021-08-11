 def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou": #.lower checks for both upper and lower case letters
            if letter.isupper():
                translation = translation + "G"

            else:
                translation = translation + "g"

        else: 
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))