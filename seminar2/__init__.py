# structural trace
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]  # пример матрицы 3x3
trace = 0  # инициализируем след

for i, row in enumerate(matrix):
    trace += row[i]  # добавляем элементы на главной диагонали

print("Trace of matrix is:", trace)  # выводим результат

# procedural trace
def matrix_trace(matrix):
    trace = 0  # инициализируем след
    for i, row in enumerate(matrix):
        trace += row[i]  # добавляем элементы на главной диагонали
    return trace


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # пример матрицы 3x3
print("Trace of matrix is:", trace)  # выводим результат

