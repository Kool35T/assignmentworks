import array as arr

array_int = arr.array('i', [1, 5, 7, 9, 100])
print(array_int)

array_int.insert(1, 3)
print(array_int)

array_int.pop(-1)
print(array_int)

array_int.append(11)
print(array_int)

array_int.reverse()
print(array_int)