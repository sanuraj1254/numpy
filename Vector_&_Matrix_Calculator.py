import numpy as np
def get_matrix():
    matrix = []

    rows = int(input("Enter number of rows: "))
    columns = int(input("Enter number of columns: "))

    for i in range (rows):
        row = []

        for j in range(columns):
            number = float(input("Enter the numbers:"))
            row.append(number)
    
        matrix.append(row)
    return np.array(matrix)

matrix_1 = get_matrix()
print(matrix_1)

matrix_2 = get_matrix()
print(matrix_2)

addition = matrix_1 + matrix_2
print(addition)

