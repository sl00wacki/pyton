def linear_search(collection, element):
    for index in range(len(collection)):
        if collection[index] == element:
            return index
    return -1

collection = [4, 2, 7, 1, 9, 3]
element = 7
result = linear_search(collection, element)

print(result+1)
