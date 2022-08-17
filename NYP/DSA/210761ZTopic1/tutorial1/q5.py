def num_vowels(text):
    count = 0
    for x in text:
        if x.lower() in ('a', 'e', 'i', 'o', 'u'):
            count += 1

    return count


print(num_vowels("TESTSTRING"))
