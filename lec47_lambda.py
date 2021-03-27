func=lambda x,y: x*3-y

print(func(3,4))

def my_func(N):
  for i in range(N):
    print((lambda i: i**2)(i))
   

    
my_func(13)