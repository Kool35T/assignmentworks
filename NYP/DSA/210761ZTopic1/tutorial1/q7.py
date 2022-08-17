def distinct(data):
    for k in range(1, len(data)):
        print('k:', k)
        print('data[k]:', data[k])
        for j in range(k):
            if data[j] == data[k]:
                return False
    return True

""" Test code """
print(distinct([1,2,3,4]))
print(distinct([1,1,3,4]))