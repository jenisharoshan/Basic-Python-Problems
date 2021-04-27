# We are given a number, we need to find the nth multiple of a number k in Fibonacci number.

def FindPos(k,n):
    f1=0
    f2=1
    i=2;
    while i!=0:
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
        if f2%k == 0:
            return n*i
        i+=1
        
    return


n = int(input());
k = int(input());

print("Position of n\'th multiple of k in"
                "Fibonacci Seires is", FindPos(k,n));