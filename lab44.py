import numpy as np 
import random

N=2
A=np.zeros((N))

a=0
b=4


for i in range(N):
  A[i]=random.randint(a, b) 
  print(A)



