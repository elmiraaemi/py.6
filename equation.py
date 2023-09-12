import math

a=int(input("a ? "))
b=int(input("b ? "))
c=int(input("c ? "))
d=int(input("d ? "))

eq="a(x**3) + b(x**3) + c(x) + d"

delta=(b**2)-(4*a*c)
if delta>0:
    x1=(-1*b+ math.sqrt(delta))/(2*a)
    x2=(-1*b- math.sqrt(delta))/(2*a)
    x3=(-1*b- math.sqrt(delta))/(2*a)
    print("the solutions : ",x1,x2,x3)
elif delta==0:
    x=(-1*b)/(3*a)
    print("the solution : ",x)
elif delta<0:
    x11=((-1*b)/(3*a))+((math.sqrt((-1*delta))/(3*a)))
    x22=((-1*b)/(3*a))-((math.sqrt((-1*delta))/(3*a)))
    x33=((-1*b)/(3*a))-((math.sqrt((-1*delta))/(3*a)))
    print("the solutions : ",x11,x22,x33)