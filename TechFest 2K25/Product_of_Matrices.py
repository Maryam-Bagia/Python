# Program to multiply two 2D matrices

# Step 1: Take sizes of matrices
rows_a = int(input("Enter number of rows for first matrix: "))
cols_a = int(input("Enter number of columns for first matrix: "))

rows_b = int(input("Enter number of rows for second matrix: "))
cols_b = int(input("Enter number of columns for second matrix: "))

# Step 2: Check if multiplication is possible
if cols_a != rows_b:
    print("Matrix multiplication not possible!")
    print("Columns of first matrix must equal rows of second matrix.")
else:
    # Step 3: Input first matrix
    print("Enter elements of first matrix:")
    A = []
    for i in range(rows_a):
        row = []
        for j in range(cols_a):
            value = int(input(f"A[{i}][{j}] = "))
            row.append(value)
        A.append(row)

    # Step 4: Input second matrix
    print("Enter elements of second matrix:")
    B = []
    for i in range(rows_b):
        row = []
        for j in range(cols_b):
            value = int(input(f"B[{i}][{j}] = "))
            row.append(value)
        B.append(row)

    # Step 5: Create result matrix with zeros
    result = [[0 for j in range(cols_b)] for i in range(rows_a)]

    # Step 6: Multiply matrices using 3 nested loops
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += A[i][k] * B[k][j]

    # Step 7: Print result
    print("Resultant Matrix after multiplication:")
    for row in result:
        print(row)
