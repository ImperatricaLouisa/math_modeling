import numpy as np 
import random as rnd

x=1
N=3
a=np.zeros((N))

for i in range(0,N):
  a[i]=rnd.randint(0,13)
  summa=a[0]+a[1]+a[2]

print(a)
print(summa)

def func_1331(summa,N,x):
  x=summa/N
  return x
  
print(x)



