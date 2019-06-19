print('welcome to False posiotn  methode program')	
import math

def fantion(x):
	#return (x**4)-8*(x**3)-35*(x**2)+450*x-1001 ##change funcion here 
        return 3.14165*x**2*(27-x)-90
def Xm(xl,xu):
    a= xu*fantion(xl) - xl *fantion(xu)
    b=fantion(xl) - fantion(xu)
    
    return a/b*1.0

def Ea(xnew,xold):
	return math.fabs( (xnew-xold )/xnew ) *100

def main():

        lower=0
        uper=3
        ######	
        xm=None
        old_xm=None
        #######
        ea=None

        c=1
        if fantion(lower)*fantion(uper)<0 : #checking the boundary is vaild  
                
                print('iteration\t Xl \t\t\t Xu \t\t\t Xm \t\t\t error ')
                while(c<=10):
                        
                        
                        xm=Xm(lower,uper) # Xm ,estimate root
                        
                        

                        fm=fantion(xm)
                        fl=fantion(lower)
                        
                        if fm*fl>0:
                                lower=xm
                        elif fm*fl<0:
                                uper=xm
                        elif fm*fl==0:
                                
                                break
                        
                        if xm and old_xm :

                                e=Ea(xm,old_xm) #error persentage 
                                print('%0.0d'%c,'\t\t %0.5f'%lower,'\t\t %0.5f'%uper,' \t\t %0.5f'%xm,' \t\t %0.2f'%e,'%' )
                        else:
                                e='N\A'
                                print('%0.0d'%c,'\t\t %0.5f'%lower,'\t\t %0.5f'%uper,' \t\t %0.5f'%xm,' \t\t %s'%e,'' )       
                        c+=1
                        old_xm=xm
        else:
                print (" Boundary is not valid \n")


if __name__=="__main__" :

        main()
