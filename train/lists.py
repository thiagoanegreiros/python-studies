nested_list = [[1,2],[3,4]]

flattened = [item for sublist in nested_list for item in sublist]
for i in flattened:
    print(i)

help(range)