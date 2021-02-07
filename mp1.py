import numpy as np       #for mathematical calculations
import matplotlib.pyplot as plt #for plotting
import pandas as pd      #for data frame creation
              
df = pd.read_csv("/home/user/Desktop/project/output data/mp15.txt",sep="\t")
X=np.array(df)         #convert df into array
Xn=X[:,4]               #array of x component
Yn=X[:,6]                #array of z component
Zn=X[:,5]                #array of y component
#perdiction formulae




#h = k(q/p)(1+tx^2+ty^2)(1/2)
#k= 0.29979Gev(cTm)^(-1)
#tx=dx/dz   , instantaneous slope
#ty=dy/dz
#dz denote (ze-z0) is taken as 1mm
#initial assumption is taken as q/p as 0 is improved
#n takex the limit of no. of points we have to apply in priction formulae



n=len(Xn)

#array declaration
X1 = []
Y1 = []
Z1  = []
Xf=[]
Yf=[]



t_x=(Xn[1]-Xn[0])/(Zn[1]-Zn[0])
t_y=(Yn[1]-Yn[0])/(Zn[1]-Zn[0])

#inserting 1st (0) element

X_z=Xn[0]
Y_z=Yn[0]
Z_z =Zn[0]

X1.append(X_z)
Y1.append(Y_z)
Z1.append(Z_z)
Xf.append(X_z)
Yf.append(Y_z)


q_p=10**-4
K=0.299792458

#k= 0.29979Gev(cTm)^(-1)
#tx=dx/dz   , instantaneous slope
#ty=dy/dz
#dz denote (ze-z0) is taken as 1mm
#initial assumption is taken as q/p as 0 is improved
#b is in Tesla
Bx=1.5
By=0.0

Bz = (0.0)

K1=0.5
#furthur points are find using prediction formulae
#loop run from x[1] to x[n-1] i.e upto the last number in the array





for i in range(n-1): #loop for 150 ironplate+air gap combo (ignoring the first hit)
    for j in range(57):   #loop for56 iron plates   
     if j==56:
      dz=-40 #in mm for air gap  (is negated to so that calculated z  value isin same direction as that of simulated) 
      if i==(n-2):
          continue # preventing an additional air gap after the last detector
     else: 
      dz=-1
     Z_z=Z_z+dz     #calculated z value
     S_x = (0.5*Bx*(dz*dz))
     S_y =(0.5*By*(dz*dz))
     S_xx =((1/6)*(Bx*Bx)*(dz*dz*dz))
     S_xy=((1/6)*(Bx*By)*(dz*dz*dz))
     S_yx=((1/6)*(Bx*By)*(dz*dz*dz))
     S_yy=((1/6)*(By*By)*(dz*dz*dz))
     R_x=(Bx*dz)
     R_y=(By*dz)
     R_xx=((1/2)*(Bx*Bx)*(dz*dz))
     R_xy=((1/2)*(Bx*By)*(dz*dz))
     R_yx=((1/2)*(Bx*By)*(dz*dz))
     R_yy=((1/2)*(By*By)*(dz*dz))

     h = (K*(q_p)*np.sqrt((1+(t_x*t_x)+(t_y*t_y))))

     X_z = X_z + (t_x*dz) + ( h * ( (t_x*t_y*S_x)-((1+(t_x*t_x))*S_y))) + ((h*h)*(((t_x*S_xx)*((3*(t_y*t_y))+1))-((t_y*S_xy)*((3*(t_x*t_x))+1))-((t_y*S_yx)*((3*(t_x*t_x))+1))+((t_x*S_yy)*((3*(t_x*t_x))+3))))
     
     
     Y_z = Y_z + (t_y*dz) + ( h * (((1+(t_y*t_y))*S_x)-(t_x*t_y*S_y) )) + ((h*h)*(((t_y*S_xx)*((3*(t_y*t_y))+3))-((t_x*S_xy)*((3*(t_y*t_y))+1))-((t_x*S_yx)*((3*(t_y*t_y))+1))+((t_y*S_yy)*((3*(t_x*t_x))+1))))
     
     t_x   = t_x +             ( h * ( (t_x*t_y*R_x)-((1+(t_x*t_x))*R_y))) + ((h*h)*(((t_x*R_xx)*((3*(t_y*t_y))+1))-((t_y*R_xy)*((3*(t_x*t_x))+1))-((t_y*R_yx)*((3*(t_x*t_x))+1))+((t_x*R_yy)*((3*(t_x*t_x))+3))))
     t_y   = t_y +             ( h * (((1+(t_y*t_y))*R_x)-(t_x*t_y*R_y) )) + ((h*h)*(((t_y*R_xx)*((3*(t_y*t_y))+3))-((t_x*R_xy)*((3*(t_y*t_y))+1))-((t_x*R_yx)*((3*(t_y*t_y))+1))+((t_y*R_yy)*((3*(t_x*t_x))+1))))  
    


     
#adding elements to X1 and Y1
    
     X_2=(1-K1)*X_z+K1*Xn[i]
     Y_2= (1-K1)*Y_z+K1*Yn[i]
     

    Yf.append(Y_2)
    Xf.append(X_2)

     
    X1 . append  (X_z)
    Y1 . append  (Y_z)   
    Z1 . append  (Z_z)

















plt.grid(b=None, which='major', axis='both')

#scatter plot
xval=plt.plot(Yf,Z1,label='posx prediction (mm)')
#labelling axis
plt.xlabel('pos(mm)')
plt.ylabel('posz(mm)')

yval=plt.plot(Yn,Zn,label='posy prediction (mm)')

#giving title to the graph
plt.title(' plot obtained from points using prediction formula (15Gev)')


#naming the data sets,getting label on plot
plt.legend(["Y predict vs Z", "Y vs Z"])
plt.show()

xval=plt.plot(Xf,Z1,label='posx prediction (mm)')
#labelling axis
plt.xlabel('pos(mm)')
plt.ylabel('posz(mm)')

yval=plt.plot(Xn,Zn,label='posy prediction (mm)')

#giving title to the graph
plt.title(' plot obtained from points using prediction formula (15Gev)')


#naming the data sets,getting label on plot
plt.legend(["X predict vs Z", "X vs Z"])


plt.show()














































































































































