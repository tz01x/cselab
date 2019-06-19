print("  secant method ")

def fun(x):
    #a=-2*x**6-1.5*x**4+10*x+2
    #a=x**3-0.165*(x**2)+3.993*(10**-4)
    #a=x**3 - 6*x**2+11*x - 6.1
    a=math.sin(x)+math.cos(1+x**2)-1
    return a
    #return -1+ 5.5*x-4*x**2+0.5*x**3

    
    #return 5.5-8*x+1.5*x**2

import math

def ea(n,o):
    return (math.fabs((n-o)/n*1.0))*100 

c=1
init_1=1
init=3.0


print("iteration \t Xi \t\t Ea")
while(c<6):
    xm= init - (fun(init)*(init_1-init)/(fun(init_1)-fun(init)  )*1.0)
    e=ea(xm,init)
    init_1=init
    init=xm
    print("%d"%c,"\t\t%0.5f"%xm,"\t\t%0.2f"%e)
    c+=1
    #print(c)
    
