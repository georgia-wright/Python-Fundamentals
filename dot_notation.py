print("this is my notes page")
#this is how we see things

print("This is a string")
print("Strings are used for representing characters! =] ")


print(1234) 
#integers (whole numbers)
print(2+6)

print(12.34)
#this is a floaring point (decimal point)

print(None)

print(True)
print(False)
#this is a boolean data type

print("hello everyone".upper())
#results in HELLO WORLD in terminal

# object.method()

"hello"

print(len("hello"))

print("hello"[1])

print("hello"[0])

# 0 - h
# 1 - e
# space is equal to a ranking too

print("hello"[-1])



# Activity 1 


print("    |   |    ")
print("    |   |    ")
print("    |   |    ")
print("-------------")
print("    |   |    ")
print("    |   |    ")
print("    |   |    ")
print("-------------")
print("    |   |    ")
print("    |   |    ")
print("    |   |    ")



# Activity 2

print("hello world".upper())

# .upper() This method places all the characters in the string into uppercase

print("Hello World".lower())

# .lower() this method places all the characters in the string into lowercase

print("hello world".capitalize())

# .capitalize() this method makes the first letter of the string into a capital letter. It doesn't pick up other sentences.
# this will lower case every other letter in the string.

print("hello world".count("o"))

print("how much wood could a wood chuck chuck".count("wood"))

# .count() this method counts how many times a specific value appears in the string.
# here the values used are the letter 'o' and the word 'wood'. 
# you must put a value in the brackets for this method to work.

print("how much wood could a wood chuck chuck".find("wood"))

# .find() this method requires a value in the brackets. It returns the first occurence of the specified value.
# for example, in this case the terminal returns the number 9 as wood first occurs at the ninth index.

# You can also use the .find() method to search within certain perameters.
# for example, if you wanted to see the first time the letter 'c' appeared between the tenth and twentieth index.

print("how much wood could a wood chuck chuck".find("c", 10, 25))
# the terminal returns the number 14, meaning c first appears at the fourteenth index after the tenth position.

print("how much wood could a wood chuck chuck".find("chuck", 5, 35))
# this returns the value '27' as 'chuck' first appears at the 27th index between 5 and 35.


print("hello world".replace("world", "everyone"))

# the .replace() method replaces every occurence of a specified value with a new specified value.
# you have to use the format .replace("old", "new") 

# you can use a count variable (e.g, 2) to replace the first two occurences of the value.
print("hello world".replace("l", "x", 2))

# this replaces the first two occurences of an 'l' with an 'x'.

print("            hello        ".strip())

# the .strip() method 'strips' all leading and trailing specified characters of the string.
# by putting nothing in the brackets, the code will strip all the blank spaces.
# you can also strip specific characters.

print("xxxxxxx hello pppwwwcccc".strip(" xcwp"))

# ^ use a space in the method brackets here to strip spaces too.

# stripping only works by stripping from the beginning of the string or from the end.


                            











