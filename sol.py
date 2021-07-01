from sympy import symbols
from sympy import sin,cos,pi,exp
from sympy import Eq,solve,solveset,linsolve,nonlinsolve

x, y, z=symbols('x y z')

# f= sin(x)
# a= solve(f,x)
# b= solveset(f,x)
# print(a)
# print(b)



s=[x+y+z-1,x+y+2*z-3,x-2*y+z]
s_s=linsolve(s,(x,y,z)) 