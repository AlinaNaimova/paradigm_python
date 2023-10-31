# Structured Programming
input_li = input('Enter list li: ') # [1, 2, 3, 4, 5, 6, 6, 5, 5, 1, 2, 3, 5]
input_n = input('Enter number n: ')# 6
counter = 0
for el in input_li:
    if el == input_n:
        counter += 1
print(counter) # 2


# Procedural Programming
input_li = input('Enter list li: ') # [1, 2, 3, 4, 5, 6, 6, 5, 5, 1, 2, 3, 5]
input_n = input('Enter number n: ')# 6


def countif(li, n):
    counter = 0
    for el in li:
        if el == n:
            counter += 1
    return counter


countif(input_li, input_n) # 2





