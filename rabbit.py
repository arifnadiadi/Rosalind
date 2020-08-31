#!/usr/bin/python
n = int(raw_input())
k = int(raw_input())

#This was my code
def recur_fibo(n):
   if n <= 1:
       return n
   elif n == 2:
       return 1
   else:
       return(recur_fibo(n-1) + (recur_fibo(n-2)*k))

#this was rosalind solution
memo = {}
def fib(n,k=1):
    args = (n, k)
    if args in memo:
        return memo[args]  # Aha! We have computed this before!

    # We haven't computed this before, so we do it now
    if n == 1:
        ans = 1
    elif n == 2:
        ans = 1
    else:
        ans = fib(n-1, k) + k * fib(n-2, k)
    memo[args] = ans  # don't forget to remember the result!
    return ans


print recur_fibo(n)
print fib(n, k)