print("Enter the elements of covariance matrix:")
cov_matrix = []
for i in range(3):
    row = []
    for j in range(3):
        element = float(input(f"Enter element ({i+1},{j+1}): "))
        row.append(element)
    cov_matrix.append(row)