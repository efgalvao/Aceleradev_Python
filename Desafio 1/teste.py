a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def teste(a, b):
    for x in a:
        for y in b:
            if x == y:
                print(x, y)

    return set(a) & set(b)


print(set(a) & set(b))