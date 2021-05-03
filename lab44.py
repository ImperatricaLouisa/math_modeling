import numpy as np 
import random

N=5
A=np.zeros((N))

a=1
b=3

for i in range(N):
  A[i]=random.randint(a, b) 
  print(A)



