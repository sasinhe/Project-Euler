Fibonacci_Array = [0 for i in range(4000000)]

def Fibonacci(n):
    if(n == 1 or n == 2):
        return 1
    elif(Fibonacci_Array[n] == 0):
        Fibonacci_Array[n] = Fibonacci(n-1) + Fibonacci(n-2)
    
    return Fibonacci_Array[n]



n = 3
while(Fibonacci(n) < 4000000):
    n += 1

sum = 0
i = 1
while(3*i <= n):
    sum += Fibonacci(3*i)
    i+= 1

print(sum)