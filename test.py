import pandas as pd
from scipy import interpolate
from scipy.interpolate import interp1d
import numpy as np
data=pd.read_csv("C:/Users/user/Desktop/data.csv")
to_drop=['Sol','px','py','pz','x2','y2','z2','vy2','vx2','vz2','sol and time','ang','ang1','ang3','hga']
data=data.drop(to_drop,axis=1)
df=data[['Ephemeris time','x1']].iloc[10:21]
print(df)
data.drop(data.index[10:20],inplace=True)
x=np.array(data['Ephemeris time'])
y = np.array(data['x1'])
#s = interpolate(x, y)
f = interp1d(x, y)
f2 = interp1d(x, y, kind='cubic')
import matplotlib.pyplot as plt
#plt.plot(x, y, 'o')
#plt.legend(['data', 'linear', 'cubic'], loc='best')
#plt.show()
ind=0
for i in range(515678478,515678488):
    print(ind,"        ",i,"     ",f2( i+0.2 ),"           ",df['x1'].iloc[ind])
    ind=ind+1
#1331 is sol id