matrix = [[int(input("Enter element for row 1, col 1: ")), int(input("Enter element for row 1, col 2: "))],
          [int(input("Enter element for row 2, col 1: ")), int(input("Enter element for row 2, col 2: "))]]

transpose = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        transpose[j][i] = matrix[i][j]

print("The transpose of the matrix is:")
for row in transpose:
    print(row)
