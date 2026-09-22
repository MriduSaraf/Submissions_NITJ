# insertion sort

a=[]
print("Enter the number of elements in the list:")
n=int(input())
for i in range(n):
    print("Enter element",i+1,":")
    a.append(int(input()))
    
for i in range(1, n):
    key = a[i]
    j = i-1
    while j >=0 and key < a[j] :
            a[j + 1] = a[j]
            j -= 1
    a[j + 1] = key

print("Sorted list is:")
for i in range(n):
    print(a[i])