# Python Program for Sum of squares of first n natural numbers

def squaresum(n):
    return (n * (n+1) * (2*n+1)) // 6

number = int(input())
print(squaresum(number))


************************** ANOTHER METHOD ******************************
def squaresum(n) :
  
    # Iterate i from 1 
    # and n finding 
    # square of i and
    # add to sum.
    sm = 0
    for i in range(1, n+1) :
        sm = sm + (i * i)
      
    return sm
  
# Driven Program
n = int(input())
print(squaresum(n))