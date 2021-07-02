from sympy import symbols
from sympy.solvers.inequalities import reduce_abs_inequality
from sympy.solvers.inequalities import reduce_rational_inequalities
from sympy import Abs

 #( вырож, знак , переменная)
x =symbols('x')
s = reduce_abs_inequality(Abs(x**2 + 2*x -3) + 3*( x + 1) , '<' , x )
print(s)