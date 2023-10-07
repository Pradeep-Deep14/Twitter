x=[1,2,3]
y=x
z=x.copy()
x.append(4)

result=(y==z,y is z)