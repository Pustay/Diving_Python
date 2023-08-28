# Напишите функцию для транспонирования матрицы .

matrix = [[1, 2, 8, 7], [6, 12, 10, 5]]

print("Исходная матрица:\n", matrix)

def transposition(matrix):
    trans_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    print(trans_matrix)

print("Транспонированная матрица :")
transposition(matrix)