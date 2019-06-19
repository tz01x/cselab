print('welcome to Bi-section methode program')	
import math

def fantion(x):
	#return (-2)*(x**6)-1.5*(x**4)+10*x+2
        #return x**4 - 8*x**3 - 35*x**2 + 450*x - 1001
        #return -12*x**5-6*x**3+10
        return 4.4294*(math.sqrt(x))*math.tanh(1.3842*math.sqrt(x))-5
def Xm(xl,xu):
	return (xl+xu)/2.0

def Ea(xnew,xold):
	return math.fabs( (xnew-xold )/xnew ) *100

def main():

        lower=0
        uper=2.0
        ######	
        xm=None
        old_xm=None
        #######
        ea=None

        c=0
        print(f'{fantion(lower)}  {fantion(uper)} ')
        if fantion(lower)*fantion(uper)<0 : #checking the boundary is vaild  
                
                print('iteration\t Xl \t\t\t Xu \t\t\t Xm \t\t\t error ')
                while(c<5):
                        
                        
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
