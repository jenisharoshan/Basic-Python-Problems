# Python Program for cube sum of first n natural numbers


def cube(n):
    
    sum = 0
    for i in range(1,n+1):
       sum = sum + (i * i * i)
    return sum

m = int(input())
print(cube(m))



****************************** ANOTHER METHOD *********************************

# Returns the sum of series 
def sumOfSeries(n):
    x = (n * (n + 1)  / 2)
    return (int)(x * x)
  
  
   
# Driver Function
n = int(input())
print(sumOfSeries(n))