def foo(x,y=[]):
    y.append(x)
    return y

a=foo(1)
b=foo(2)
print(a,b)