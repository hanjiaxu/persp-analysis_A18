# function needs to be tested in problem 1
def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1: return None
    for i in range(2, int(n**.5)+1):
        if n % i == 0: return i
    return n
