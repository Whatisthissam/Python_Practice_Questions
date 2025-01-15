matrix1 = [[int(input("Enter element for matrix 1, row 1, col 1: ")), int(input("Enter element for matrix 1, row 1, col 2: "))],
           [int(input("Enter element for matrix 1, row 2, col 1: ")), int(input("Enter element for matrix 1, row 2, col 2: "))]]

matrix2 = [[int(input("Enter element for matrix 2, row 1, col 1: ")), int(input("Enter element for matrix 2, row 1, col 2: "))],
           [int(input("Enter element for matrix 2, row 2, col 1: ")), int(input("Enter element for matrix 2, row 2, col 2: "))]]

result = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print(f"The result of matrix addition is:")
for row in result:
    print(row)
