print(" modified secant method ")
import math
def fun(x):
    #a=-2*x**6-1.5*x**4+10*x+2
    #a=x**3-0.165*(x**2)+3.993*(10**-4)
    #a=7*math.sin(x)*math.exp(-x)-1
    a=x**5-16.05*x**4+88.75*x**3-192.0375*x**2+11.35*x+31.6875
    return a
    #return -1+ 5.5*x-4*x**2+0.5*x**3
def Det_fun(x):
    #a=-12*x**5-6*x**4+10
    a=3*x**2-2*x**1
    return a
    
    #return 5.5-8*x+1.5*x**2


def ea(n,o):
    return (math.fabs((n-o)/n*1.0))*100 

c=1
ini=0.5825
const=0.05

print("iteration \t Xi \t\t Ea")
while(c<6):
    xm= ini - (fun(ini)*(const*ini)/(fun(const*ini+ini)-fun(ini)  )*1.0)
    print("%0.6f"%fun(ini),"\t\t%0.5f"%(fun(const*ini+ini)))
    e=ea(xm,ini)
    ini=xm
    
    print("%d"%c,"\t\t%0.5f"%xm,"\t\t%0.2f"%e)
    c+=1
    #print(c)
    
