# bubble sort
a=[]
print("Enter the number of elements in the list:")
n=int(input())
for i in range(n):
    print("Enter element",i+1,":")
    a.append(int(input()))

for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            
print("Sorted list is:")
for i in range(n):
    print(a[i])
    