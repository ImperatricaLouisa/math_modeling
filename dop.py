from sympy import sin,cos,trigsimp,sinh,cosh,symbols

a=1
p,sig=symbols('p sig')

p0=float(input('p'))

sig0=float(input('sig'))

x= (a*sinh(p))/(cosh(p)-cos(sig))
y= (a*sin(p))/(cosh(p)-cos(sig))



print(x.subs([(p,p0),(sig,sig0)]))
print(y.subs([(p,p0),(sig,sig0)]))




import numpy as np
from sympy import symbols
from sympy.vector import CoordSys3D
from sympy import sin,cos,trigsimp,sqrt

N=CoordSys3D('N')
a,b,c= symbols('a b c')

v=  N.i -2*N.j +3*N.k
print(v/3)

v1 = 2*N.i +3*N.j - N.k
v2 = N.i -4*N.j + N.k

print(v1.dot(v2))

print(v1.cross(v2))
print(v2.cross(v1))

m=(v1.dot(v1))**0.5
print(m)


m=sqrt(v1.dot(v1)).evalf()
print(m)








from sympy import symbols
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Abs

x, y, z=symbols('x y z')

s= reduce_abs_inequality(Abs(x-5) - 3 ,'>',x)
print(s)

s= reduce_rational_inequalities([[y+2>0]],y)
print(s)






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
#print(s_s.args[0][0])

s=[x**2+x, x-y]
s_s= nonlinsolve(s,[x,y])
print(s_s)
print(s_s.args[1])

s=[x**2+x, y**2+1]
s_s= nonlinsolve(s,[x,y])
print(s_s)








