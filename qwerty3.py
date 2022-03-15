x=3
e=0.00001
b=True
while b==True:
    y=x**3-2.92*x**2+1.4355*x+0.791136
    if abs(x-y)<e:
        b=False
    x=y
    print(x)