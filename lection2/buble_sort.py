# using procedural(imperative and structural) Programming

def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# example usage
my_array = [64, 25, 12, 22, 11]
sorted_array= buble_sort(my_array)
print(sorted_array)
