import numpy as np
import lab30

g=10
m=int(input('масса '))
h=int(input('высота '))
v=int(input('скорость '))
E=0


def func(E,m,h,v):
  E=(m*v**2)/2 + m*lab30.g*h
  return E

print(func(E,m,h,v))




