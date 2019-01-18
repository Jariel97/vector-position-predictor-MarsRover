import pandas as pd
from scipy import interpolate
from scipy.interpolate import interp1d
import numpy as np
data=pd.read_csv("data.csv")
to_drop=['Sol','px','py','pz','x2','y2','z2','vy2','vx2','vz2','sol and time','ang','ang1','ang3','hga']
data=data.drop(to_drop,axis=1)
df=data.iloc[10:21]
print (df)
data.drop(data.index[10:20],inplace=True)
x=np.array(data['Ephemeris time'])
x1 = np.array(data['x1'])
y1 = np.array(data['y1'])
z1 = np.array(data['z1'])
vx1 = np.array(data['vx1'])
vy1 = np.array(data['vy1'])
vz1 = np.array(data['vz1'])

#s = interpolate(x, y)
fx = interp1d(x, x1, kind='cubic')
fy = interp1d(x, y1, kind='cubic')
fz = interp1d(x, z1, kind='cubic')
fvx = interp1d(x, vx1, kind='cubic')
fvy = interp1d(x, vy1, kind='cubic')
fvz = interp1d(x, vz1, kind='cubic')

import matplotlib.pyplot as plt
#plt.plot(x, y, 'o')
#plt.legend(['data', 'linear', 'cubic'], loc='best')
#plt.show()
ind=0
for i in range(515678478,515678489):
    print (ind,"   ",i+0.2,"    ",fx( i+0.2 ),"    ",fy( i+0.2 ),"    ",fz( i+0.2 ),"    ",fvx( i+0.2 ),"    ",fvy( i+0.2 ),"   ",fvz( i+0.2 ),"   ")
    ind=ind+1
#1331 is sol id
