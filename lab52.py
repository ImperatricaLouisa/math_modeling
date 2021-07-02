from sympy import symbols
from sympy import sin,cos,pi,exp
from sympy import Eq,simplify, factor

x , y , z , a =symbols('x y z a')

n=   ?    ((x*y**2 - 2*x*y + x*z**2 + y**2 - 2*y*z + z**2)/(x**2-1))
print(n)

m=simplify(((1+sin(a))/(1-sin(a)))*0.5 + ((1-sin(a))/(1+sin(a))))
print(m)