# selection sort
a=[]
print("Enter the number of elements in the list:")
n=int(input())
for i in range(n):
    print("Enter element",i+1,":")
    a.append(int(input()))

for i in range(n):
    min = i
    for j in range(i+1, n):
        if a[min] > a[j]:
            min = j
    a[i], a[min] = a[min], a[i]

print("Sorted list is:")
for i in range(n):
    print(a[i])