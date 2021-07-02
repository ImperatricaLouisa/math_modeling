from sympy import symbols
from sympy import sin, cos, pi, exp, Abs
from sympy import Eq, solve, solveset, linsolve, nonlinsolve
from sympy.vector import CoordSys3D

N = CoordSys3D('N')


a = 4*N.i + 3*N.j + 8*N.k
b = -2*N.i + 8*N.j + 7*N.k


J = reduce_abs_inequality(( a * b )/ (Abs(a) * Abs(b)) - cos(L) , '=' , L)