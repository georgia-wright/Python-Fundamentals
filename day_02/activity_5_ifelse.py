# word = input("Type a word    >    ")

# if word[0:1] == word[-1]:
#     print("True")
# else:
#     print("False")


# stretch:

word = input("Type a word    >    ")

if (len(word)%2 == 0) and (word[0:len/2 -1] == word[len/2:len]):
    print("True")
else:
    print("False")