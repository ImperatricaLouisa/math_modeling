def my_fu(a, b):
    x = 3 * a - b
    return x

# tmp = my_fu()

def my_fu(a=1, b=0):
    x = 3 * a - b
    return x

print(my_fu())
print(my_fu(3, 4))
print(my_fu(3))
print(my_fu(b=3))
print(my_fu(b=3, a=9))

def my_func(a, b=0):
    x = 3 * a - b
    return x

# Так НЕЛЬЗЯ!
# def my_func(a=0, b):
#     x = 3 * a - b
#     return x

def my_func(*args):
    x = 3 * args[0] - args[1]
    return x

print(my_func(3, 4))
print(my_func(3, 4, 8))

def my_fu(*args):
  for i in range (0,len(args)):
    b=i**2
  return b

def my_func(**kwrgs):
    x = 3 * kwrgs['obj_1'] - kwrgs['obj_2']
    return x

print(my_func(obj_1=3, obj_2=4))
print(my_func(obj_1=3, obj_2=4, obj_3=8))
