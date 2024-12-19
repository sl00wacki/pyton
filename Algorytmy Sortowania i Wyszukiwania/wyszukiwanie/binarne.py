def binary_search(collection, element):
    low = 0
    high = len(collection) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = collection[mid]

        if guess == element:
            return mid
        if guess > element:
            high = mid - 1
        else:
            low = mid + 1

    return None

sorted_list = [1, 3, 5, 7, 9]
element = 3
result = binary_search(sorted_list, element)

print(result+1)
