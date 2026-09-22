n=10
print("Enter 10 numbers:")
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
    
print("Give the number to be searched:")
k=int(input())
mid=n/2
