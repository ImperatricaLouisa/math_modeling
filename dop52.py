from sympy import symbols
from sympy import sin, cos, pi, exp, Abs
from sympy import Eq, solve, solveset, linsolve, nonlinsolve
from sympy.vector import CoordSys3D

N = CoordSys3D('N')

a = 7*N.i + 2*N.j - 8*N.k
b = -4*N.i + x*N.j + 9*N.k

s = a.dot(b)

# J = reduce_rational_inequality( s , '=' ,2 x )

D = solveset(s, x )

print( D )
