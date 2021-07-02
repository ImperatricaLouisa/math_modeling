from sympy import sin,cos,trigsimp,sinh,cosh,symbols

a=1
p,sig=symbols('p sig')

p0=float(input('p'))

sig0=float(input('sig'))

x= (a*sinh(p))/(cosh(p)-cos(sig))
y= (a*sin(p))/(cosh(p)-cos(sig))

print(x.subs([(p,p0),(sig,sig0)]))
print(y.subs([(p,p0),(sig,sig0)]))