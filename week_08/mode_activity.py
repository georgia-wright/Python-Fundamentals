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
    67,
    67
]


# def mode(list):
    
#     for i in list:
#         print(list.count(i))
#         print(list.index(i))

    


# mode(integers)

def find_mode(dataset):
    highest_count = 0
    mode  = dataset[0]
    for data in dataset:
        current_count = dataset.count(data)
        if current_count > highest_count:
            highest_count = current_count
            mode = data
    if highest_count == 1:
        return "No Mode"
    else:
        return mode

print(find_mode(integers))




        

        
