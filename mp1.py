import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/user/Desktop/project/output data/mp1.txt",sep="\t")
print(df)
print(df.shape)
X = np.array(df)
Xn = X[:,4]
print(Xn)

Zn = X[:,5]
Yn = X[:,6]
print(Yn)
plot1=plt.figure(1)
plt.scatter(Xn,Yn, )
plt.scatter(Zn,Yn, )
plt.xlabel('position')
plt.ylabel('y-axis')

plt.title('plot obtained for the points from given data (1Gev)')
sing prediction formul
plt.legend(["X vs Y", "Z vs Y"])
plt.show()