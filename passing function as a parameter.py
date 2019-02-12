def addd(a,b):
    return print(a+b)

def sub(a,b):
    return  print(a-b)
def mul(a,b):
    return print(a*b)

def math(a, b, fn=addd):
    return print(fn(a,b))
math(2,8)
addd(8,9)
sub(10,7)
math(7,7, mul)