def fact(n): 
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)

n = int(input("Enter a number: "))
print("Factorial =", fact(n))

n = int(input("Enter a number: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)

n = int(input("Enter a number: "))
if n > 1:
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")