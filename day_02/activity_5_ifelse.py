# word = input("Type a word    >    ")

# if word[0:1] == word[-1]:
#     print("True")
# else:
#     print("False")


# stretch:

word = input("Type a word    >    ")

if (len(word)%2 == 0) and (word[0:int(len(word)/2 -1)] == word[int(len(word)/2):len(word)]):
    print("True")
else:
    print("False")

    
# print(word[0:int(len(word)/2 -1)])
