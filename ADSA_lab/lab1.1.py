# linear search

n=10
print("Enter 10 numbers:")
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
    
print("Give the number to be searched:")
k=int(input())
for i in range(n):
    if numbers[i]==k:
        print("The number is found at index:",i)
        break
else:
    print("The number is not found.")