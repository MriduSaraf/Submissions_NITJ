n = int(input("Enter number of data points: "))

h_L = []
w_L = []

for i in range(n):
    h = float(input("Enter height: "))
    w = float(input("Enter weight: "))
    h_L.append(h)
    w_L.append(w)

Uh = sum(h_L)/n
Uw = sum(w_L)/n

print("Mean Height =",Uh)
print("Mean Weight =",Uw)

X2 = 0
XY= 0
Y2 = 0

for i in range(n):

    X= h_L[i] - Uh
    Y= w_L[i] - Uw

    X2 += X*X
    Y2 += Y*Y
    XY += X*Y

X2 = X2 / (n - 1)
XY=XY / (n - 1)
Y2=Y2 / (n - 1)

covariance_matrix = [
    [X2, XY],
    [XY, Y2]
]

print("\nCovariance Matrix:")

for row in covariance_matrix:
    print(row)
    