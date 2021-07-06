import math
import numpy as np
from sympy import symbols
from sympy import sin, cos, pi, exp, Abs , acos
from sympy import Eq, solve, solveset, linsolve, nonlinsolve
from sympy.vector import CoordSys3D

N = CoordSys3D('N')

a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k
# c = -5*N.i − 6*N.j + 12

s = a.dot(b)
#l = a.dot(c)
#g = b.dot(c)

s1 = (a.dot(a))**0.5 * (b.dot(b))**0.5
#l1 = (a.dot(a))**0.5 * (c.dot(c))**0.5
# g1 = (c.dot(c))**0.5 * (b.dot(b))**0.5 

p = s / s1 
#p1 = l / l1
# p2 = g / g1

x = np.degrees(float(acos(p)))

# J = reduce_abs_inequality( s / (Abs(a) * Abs(b)) - cos(x)  , '=' , x )

print(x)