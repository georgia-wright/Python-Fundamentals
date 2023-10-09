print("Here is a list of various dog breeds:")
print()
dog_breeds_list = [
    "Dalmatian",
    "Dachsund",
    "Doberman",
    "Dalmatian",
    "Cocker Spaniel",
    "Doberman",
    "Poodle",
    "Cocker Spaniel",
    "Dalmatian",
    "Dachsund",
    "Labrador",
    "Cocker Spaniel"
]

print(dog_breeds_list)
print()


print("To remove a certain value from the list, we use the .remove() method.")
print()
print("In this case, we will remove the value 'Labrador' using the format of list.remove(element).")
print()
dog_breeds_list.remove("Labrador")
print()
print(dog_breeds_list)
print()
print("To reverse the list, we use the .reverse() method:")
print()
dog_breeds_list.reverse()

print(dog_breeds_list)
print()
print("To sort the list in ascending (alphabetical) order, we use the .sort() function:")

dog_breeds_list.sort()
print()
print(dog_breeds_list)
print()
print("To sort the list in reverse alphabetical order, we use the method .sort(reverse=True):")
print()
dog_breeds_list.sort(reverse=True)
print()
print(dog_breeds_list)
print()
print("This method also works in the same way using integers, placing them into ascending or descending order.")
print()

print("The .count() method can be used to count how many of a certain value is in the list.")
print()
print("This differs to the .len() method, which tells us how many values are in the entire list.")

print()

print("Using the .count() method, there are " + str(dog_breeds_list.count("Dalmatian")) + " Dalmatians in the list and "  + str(dog_breeds_list.count("Dachsund")) + " Dachsunds in the list.")


print()

print("Finally, the .extend() method allows us to add another list on to our original list.")

print()

dog_breeds_list1 = [
    "Jack Russell",
    "Whippet",
    "Golden Retriever"
]

print("I will create a second list of dog breeds named 'dog_breeds_list1:")
print()
print(dog_breeds_list1)
print()
print("I will add this to the original list:")

print()

dog_breeds_list.extend(dog_breeds_list1)

print(dog_breeds_list)











