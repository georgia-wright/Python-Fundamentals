integers = [
    12,
    13,
    78,
    43,
    56,
    33,
    27,
    30,
    71,
    67,
    59,
]

# access the middle index point n/2
# check if length is even or odd


integers.sort()

print(len(integers))

len = len(integers)

if len%2 != 0:
    print("The sum of the list's elements is odd")
    middle_index = len //2 # floor division
    median = integers[middle_index]
    print(median)
else:
    print("The sum of the list's elements is even")
    first_number = (len/2) -1
    second_number = len/2
    median = (first_number + second_number)/2
    print(median)





