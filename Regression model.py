import sys

def insert():
    x=input("Input all x values : ")
    y=input("Input all y values : ")
    #converting string into list
    return x,y
def convert(s):
    list=s.split()
    j=[]
    for i in list:
        j.append(eval(i))
    return j

def line(m,intercept,x,i):
    yest=m*x[i]+intercept   #line
    yest=round(yest,4)
    return yest

def reg():
    val=insert()
    x=convert(val[0])
    y=convert(val[1])
    print("X"+str(x)+"\nY"+str(y))
    if len(x)==len(y) and len(x)>1:
        z=len(x)
        xavg=sum(x)/z
        yavg=sum(y)/z
        xdiff,ydiff=[],[]
        for i in x:
            xdiff.append(i-xavg)
        for i in y:
            ydiff.append(i-yavg)
        run=0
        xyprod,xsq,ysq=[],[],[]
        while run<z:
            xyprod.append(xdiff[run]*ydiff[run])
            xsq.append(xdiff[run]**2)
            ysq.append(ydiff[run]**2)
            run+=1
        m=sum(xyprod)/sum(xsq)
        intercept=yavg-m*xavg
    else:
        print(" Error, number of x values should be same as of y values and more than 1 ")
        sys.exit()
        
    print("m = ",round(m,3))
    print("Intercept = ",round(intercept,3))
    #line(m,intercept,)
    yest=0
    yestdiffsq=[]
    yestdiffsqerror=[]
    print("actual","predicted")
    for i in range(0,len(x)):
        yest=line(m,intercept,x,i)
        yestdiffsq.append((yest-yavg)**2)
        yestdiffsqerror.append((yest-y[i])**2)
        print("  ",str(y[i])+"       "+str(yest)) 
        #for i in range(0,z):
    cod=sum(yestdiffsq)/sum(ysq) #coffiecient of determination
    print("\n Coffiecient of determination is : ",round(cod,4))
    print("\n Overall RMS error is : ",round((sum(yestdiffsqerror)/z)**0.5,5),"\n")
    predict(m,intercept)

def predict(m,intercept):
    x=input("Input new values of x: ")
    x=convert(x)
    print(x)
    print("given x","predicted y")
    for i in range(0,len(x)):
        yest=line(m,intercept,x,i)
        print("  ",x[i],"     ",yest)

reg() #start



