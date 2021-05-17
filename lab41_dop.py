import numpy as np

def ste(a,n):
  b=1   
  for i in range(abs(n)):
    b*=a
  if n >= 0:
    return b
  else:
    return 1/b
 
l=ste(float(input('число')), int(input('степень')))

print(l)


