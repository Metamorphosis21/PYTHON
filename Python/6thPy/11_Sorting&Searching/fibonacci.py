
n = 10
a, b = 0, 1
print(a, b, end = " ")
for i in range(2,n):
    a, b = b, a+b
    print(b, end = " ")
    
    
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = 10
print("Fibonacci sequence up to", n, ":")
for i in range(n):
    print(fibonacci(i), end=" ")