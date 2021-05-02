import numpy as np 

a=[0,1,2,3,4,5]

def func(a):
  s=0
  for i in range (len(a)):
    s+=a[i]
  return s/len(a)

print(func(a))
