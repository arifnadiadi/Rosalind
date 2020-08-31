#!/usr/bin/python
memo = {}
def fib(n):
    args = (n)
    if args in memo:
        return memo[args]  # Aha! We have computed this before!

    # We haven't computed this before, so we do it now
    if n == 1:
        ans = 1
    elif n == 2:
        ans = 1
    else:
        ans = fib(n-1) + fib(n-2)
    
    memo[args] = ans  # don't forget to remember the result!
    return ans

#'n' is number of months, 'm' is months rabbits live
def rabbit(n, m):
    
    