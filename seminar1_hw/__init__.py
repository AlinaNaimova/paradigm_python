# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.


def sort_lists_imperative(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers


# Пример использования
nums = [5, 2, 8, 3, 9, 1]
sorted_numbers = sort_lists_imperative(nums)
print(sorted_numbers)  # [9, 8, 5, 3, 2, 1]


# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

nums_list = [5, 2, 8, 3, 9, 1]
nums_list.sort(reverse=True)
print(nums_list)
