a=int(input("Enter the number of features of dataset:"))
n=int(input("Enter the number of the data points:"))

data_points = []
for i in range (n):
    data_point = []
    for j in range(a):
        feature_value = float(input(f"Enter value for feature {j + 1} of data point {i + 1}: "))
        data_point.append(feature_value)
    data_points.append(data_point)
    
means=[]
for j in range(a):
    feature_sum = sum(data_points[i][j] for i in range(n))
    feature_mean = feature_sum / n
    means.append(feature_mean)
    
covariance_matrix = [[0 for _ in range(a)] for _ in range(a)]
for i in range(a):
    for j in range(a):
        covariance_sum = sum((data_points[k][i] - means[i]) * (data_points[k][j] - means[j]) for k in range(n))
        covariance_matrix[i][j] = covariance_sum / (n - 1)

print("Covariance Matrix:")
for row in covariance_matrix:
    print(row)

