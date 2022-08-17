lines = []

while True:
    try:
        single = input('Enter a line (ctrl-D/ctrl-Z to stop): ')
        lines.append(single)
    except EOFError:
        break # leave the while loop
    
# print(lines)
# print(reversed(lines))
# print(list(reversed(lines)))

print('\n'.join(reversed(lines)))