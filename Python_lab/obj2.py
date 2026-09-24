a=int(input("Enter a number N1:"))
b=int(input("Enter another number N2:"))

# Arithmetic operators
print("\nArithmetic Operators:")
print("Addition(a+b):",a+b)
print("Subtraction(a-b):",a-b)
print("Multiplication(a*b):",a*b)
print("Division(a/b):",a/b)
print("Floor Division(a//b):",a//b)
print("Modulus(a%b):",a%b)
print("Exponent(a**b):",a**b)

# Comparison operators
print("\nComparison Operators:")
print("Greater than(a>b):",a>b)
print("Less than(a<b):",a<b)
print("Greater than or equal to(a>=b):",a>=b)
print("Less than or equal to(a<=b):",a<=b)
print("Equal to(a==b):",a==b)
print("Not equal to(a!=b):",a!=b)

# Logical operators
print("\nLogical operators:")
print("Logical AND(a>5 and b<50):",a>5 and b<50)
print("Logical OR(a>5 or b<50):",a>5 or b<50)
print("Logical NOT(not(a>5 and b<50)):",not(a>5 and b<50))

# Bitwise operators
print("\nBitwise operators:")
print("Bitwise AND(a&b):",a&b)
print("Bitwise OR(a|b):",a|b)
print("Bitwise XOR(a^b):",a^b)
print("Bitwise NOT(~a):",~a)
print("Left Shift(a<<2):",a<<2)
print("Right Shift(a>>2):",a>>2)

# Identity operators
print("\nIdentity operators:")
print("Identity (a is b):",a is b)
print("Identity (a is not b):",a is not b)

# Membership operators
print("\nMembership operators:")
print("Membership (a in [10, 20, 30]):",a in [10, 20, 30])
print("Membership (a not in [10, 20, 30]):",a not in [10, 20, 30])

# Assignment operators
print("Assignment operators:")
a+=b
print("Assignment (a+=b):",a)
a-=b
print("Assignment (a-=b):",a)
a*=b
print("Assignment (a*=b):",a)
a/=b
print("Assignment (a/=b):",a)
