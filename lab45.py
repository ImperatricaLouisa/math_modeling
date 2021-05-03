import numpy as np 

fig=int(input('1)круг   2)квадрат   3)треугольник '))
S=0
if fig==1:
  r=int(input('введите r '))
  def krug(S):
    S= r**2*3.14
    return S
  print(krug(S))

elif fig==2:
  a=int(input('введите сторону квадрата '))
  def kvadrat(S):
    S= a**2
    return S
  print(kvadrat(S))

elif fig==3:
  h=int(input('введите h '))
  b=int(input('введите длину основания '))
  def treug(S):
    S= 0.5*h*b
    return S
  print(treug(S))
