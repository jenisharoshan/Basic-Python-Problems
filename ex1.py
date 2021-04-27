# Check for any number if it is a Fibonacci in Python:

n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes")
    else:
        print("No")

# EXPLANATION:
    
# If the input is 0 or 1 then it is the Fibonacci number and prints yes. Else the integer input will be compared with c(a variable in the code) because c is a Fibonacci number and it goes on by adding with its previous number and stops when c is not less than the integer input.
# If c is equal to n then it prints yes else it prints no.