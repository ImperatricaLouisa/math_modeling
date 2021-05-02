import math
import numpy as np


N=int(input())
M=int(input())

a=np.zeros((N,M))

for i in range(0,N):
  for j in range(0,M):
    if i==0 or j==0:
      a[i,j]=np.sin(N*(i+1)+M*(j+1))
      if a[i,j]<0:
        a[i,j]=0
    else:
      a[i,j]=np.sin(N*i+M*j)
      if a[i,j]<0:
        a[i,j]=0
print(a)
 
x=int(input('введите x'))
y=int(input('введите y'))
for i in range(N):
    a[i][x], a[i][y] = a[i][y], a[i][x]
    print(a[i])