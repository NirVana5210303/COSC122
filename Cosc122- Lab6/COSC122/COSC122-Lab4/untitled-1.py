def quick_power(x,n):
    """
    Computes x ^ n where n is an integer
    NOTE: You need to write the doc test for the base case.
    >>> quick_power(2,3)
    8
    >>> quick_power(2,8)
    256
    >>> quick_power(2,16)
    65536
    >>> quick_power(2,0)
    1
    """
    if n==0:
        return 1
    if n%2==0:
        return (quick_power(x,n/2))**2
    if n%2==1:
        return x*quick_power(x,n-1)
    
quick_power(2,4)