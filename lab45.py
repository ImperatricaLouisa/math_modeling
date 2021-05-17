import numpy as np 

fig=int(input('1)круг   2)квадрат   3)треугольник '))
S=0

def fun():
  if fig==1:
    r=int(input('введите r '))
    S= r**2*3.14
  
  elif fig==2:
    a=int(input('введите сторону квадрата '))
    S= a**2
  
  elif fig==3:
    h=int(input('введите h '))
    b=int(input('введите длину основания '))
    S= 0.5*h*b
  return S
print(fun())
