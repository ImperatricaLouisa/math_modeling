n=int(input())

def fib(n):
  a=1
  if n>-1:
    if n==0:
      return 0
    elif n == 1:
      return 1
    else:
      a=fib(n-1)+fib(n-2)
      return a
  if n <= -1:
    a=fib(n+2)-fib(n+1)
    return a

print (fib(n))




