x0=13

def move(t):
  x=x0*t
  return x

print(move(3))

a='good'

def my_fu():
  a='Bad'
  print(a)

my_fu()
print(a)

def changer(a, b):
    a = 2
    b[0] = 'Good'

x = 10
L = [1, 2]

changer(x, L)

print(x)
print(L)

L = [1, 2]
changer(x, L[:])

print(L)