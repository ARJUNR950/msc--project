import numpy as np   #for mathematical calculations
import pandas as pd   #for data frame creation
import matplotlib.pyplot as plt  #for plotting
import math as mp #mathematical works
df = pd.read_csv("/home/user/Desktop/project/output data/mp1.txt",sep="\t")


X = np.array(df)  #convert df into array
Xn=X[:,4]         #array of x component
Yn=X[:,6]         #array of z component
Zn=X[:,5]         #array of y component

t_x=Xn[1]-Xn[0]/Zn[1]-Zn[0]
t_y=Yn[1]-Yn[0]/Zn[1]-Zn[0]

#h = k(q/p)(1+tx^2+ty^2)(1/2)
#k= 0.29979Gev(cTm)^(-1)
#tx=dx/dz   , instantaneous slope
#ty=dy/dz
#dz denote (ze-z0) is taken as 1mm
#initial assumption is taken as q/p as 0
#n takex the limit of no. of points we have to apply in priction formulae







n=len(Xn)

K=0.29979
(q_p)=0

h=K*(q_p)*mp.sqrt(1+t_x*t_x+t_y*t_y)


Bx=30000
By=0
dz=1
S_x= (1/2)*Bx*dz*dz
S_y= (1/2)* By*dz*dz
S_xx= (1/6)*Bx*Bx*dz*dz*dz
S_yy =(1/6)*By*By*dz*dz*dz
S_xy=(1/6)*Bx*By*dz*dz*dz
S_yx= (1/6)* Bx*By*dz*dz*dz
R_x=(Bx*dz)
R_y=(By*dz)

R_xx=((1/2)*(Bx*Bx)*(dz*dz))
R_xy=((1/2)*(Bx*By)*(dz*dz))
R_yx=((1/2)*(Bx*By)*(dz*dz))
R_yy=((1/2)*(By*By)*(dz*dz))

Y_z0=0
X_z0=0

#array declaration

Y_z=[0,0,0,0,0,0,0,0,0,0,0,0,0]

X_z=[0,0,0,0,0,0,0,0,0,0,0,0,0]


#perdiction formulae
#furthur points are find using prediction formulae
#loop run from x[1] to x[n-1] i.e upto the last number in the array
for i in range(1,n) :
    
     X_z[i]=X_z[i-1]+t_x*dz+h*(t_x*t_y*S_x-(1-t_x**2)*S_y) + (h**2)*(t_x*((3*(t_y**2))+1)*S_xx - t_y*((3*(t_x**2) )+1)*S_xy -t_y*((3*(t_x**2))+1)*S_yx+t_x*((3*(t_x**2))+3)*S_yy)
     print(X_z[i]) 
     Y_z[i]=Y_z[i-1] + t_y*dz + h*((1 + t_y**2 ) *S_x -t_x*t_y*S_y) + (h**2)*(t_y*(3*(t_y**2)+3)*S_xx-t_x*(3*(t_y**2)+1)*S_xy-t_x*(3*(t_y**2)+1)*S_yx+t_y*(3*t_x**2+1)*S_yy) 
     print(Y_z[i])
plot1=plt.figure(1)
plt.plot(X_z,Zn, )
plt.plot(Y_z,Zn, )
plt.xlabel('position(mm)')
plt.ylabel('Z-axis')

plt.title('plot obtained for the points from predicted  data (1Gev) anti muon')

plt.legend(["X vs Z", "Y vs Z"])
plt.show()













































