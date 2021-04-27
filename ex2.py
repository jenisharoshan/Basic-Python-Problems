# Python Program for n-th Fibonacci number
def Fibonacci(n1):
    if n1 < 0:
        return("Enter Positive Interger")
    elif n1==1:
        return 0
    elif n==2: 
        return 1
    else:
        return Fibonacci(n1-1) + Fibonacci(n1-2)
n = int(input())
print(Fibonacci(n))
    