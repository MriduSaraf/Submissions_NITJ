# Fibonacci Search

n = int(input("Number of elements in the array: "))

print("Enter", n, "numbers:")
numbers = []

for _ in range(n):
    num = int(input())
    numbers.append(num)

print("Give the number to be searched:")
k = int(input())

fib2 = 0
fib1 = 1
fib = fib1 + fib2

while fib < n:
    fib2 = fib1
    fib1 = fib
    fib = fib1 + fib2

offset = -1

while fib > 1:
    i = min(offset + fib2, n - 1)

    if numbers[i] < k:
        fib = fib1
        fib1 = fib2
        fib2 = fib - fib1
        offset = i

    elif numbers[i] > k:
        fib = fib2
        fib1 = fib1 - fib2
        fib2 = fib - fib1

    else:
        result = i
        break

else:
    result = -1

if result == -1 and fib1 and offset + 1 < n and numbers[offset + 1] == k:
    result = offset + 1

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")