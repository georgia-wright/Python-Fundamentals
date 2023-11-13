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
    59
]



def mean(list):

    
    list.sort()

    total = sum(list, 0)

    length = len(list)

    print(f"{total/length:.2f}")



mean(integers)

# print(sum(integers))

# sum = sum(integers)

# print(len(integers))

# len = len(integers)

# mean = (sum/len)

# print(f"{mean:.2f}")












