def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    

print(factorial(5)) # 120
print(factorial(10)) # 3628800
print(factorial(20)) # 2432902008176640000