monthConversions = {
    "Jan": "January",           #Jan is the key, January is the value
    "Feb": "February",          #Keys must be unique
    "Mar": "March",             #Can also have numbers instead of names for keys, as long as they're unique
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",

}

#print(monthConversions["Jul"])  #Can use this or monthConversions.get

print(monthConversions.get("Bum", "Not a valid key")) #Add a default value to fall back on if no key with that name is found.