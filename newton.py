def fun(x):
    #a=-2*x**6-1.5*x**4+10*x+2
    #a=x**3-x**2+2
    a= -0.9*x**2 + 1.7*x + 2.5 
    return a
    #return -1+ 5.5*x-4*x**2+0.5*x**3
def Det_fun(x):
    #a=-12*x**5-6*x**4+10
    #a=3*x**2-2*x**1
    a= -1.8*x+1.7
    return a
    
    #return 5.5-8*x+1.5*x**2

import math 
def ea(n,o):
    return (math.fabs((n-o)/n*1.0))*100 

c=1
ini=5
print("iteration \t Xi \t\t Ea")
while(c<6):
    xm= ini - (fun(ini)/Det_fun(ini)*1.0)
    e=ea(xm,ini)
    ini=xm
    print("%d"%c,"\t\t%0.5f"%xm,"\t\t%0.2f"%e)
    c+=1
    #print(c)
    
