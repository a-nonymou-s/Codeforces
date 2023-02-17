# Read the matrix
matrix = [list(map(int, input().split())) for _ in range(5)]

# Find the row and column index of the number one
row_index = 0
column_index = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            row_index = i
            column_index = j

# Calculate the number of row and column moves
row_moves = abs(row_index - 2)
column_moves = abs(column_index - 2)

# Print the total number of moves
print(row_moves + column_moves)
