def minmax(data):
    small = big = data[0]
    for i in data:
        if i > big:
            big = i
        elif i < small:
            small = i
    return(small, big)


print(minmax([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
