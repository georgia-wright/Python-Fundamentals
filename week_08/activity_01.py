print("Range function")


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



integers_2 = [
    24,
    26,
    88,
    234
]

def range_func(list):
    list.sort()

    range = (list[-1] - list[0])
    print(f"The range is {range}.")

range_func(integers)

range_func(integers_2)




