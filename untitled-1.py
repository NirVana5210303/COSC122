global count
def exp_rec(x,n):
    global count
    count=0
    #return x to the power of n
    if n==0:
        return 1
    elif n%2 == 1: #number is odd
        count+=1
        return x*exp_rec(x,n-1)
    else: #number is even
        count+=1
        p = exp_rec(x,n/2)
        return p*p
exp_rec(2,11)
