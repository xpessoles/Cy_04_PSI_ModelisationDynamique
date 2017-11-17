import numpy as np
import matplotlib.pyplot as plt


fid = open("TestPendule.csv")
data = fid.readlines()
fid.close()

les_t=[]
les_angles=[]
data = data[1:]
for ligne in data:
    ligne  =ligne.split(";")
    les_t.append(float(ligne[0]))
    les_angles.append(float(ligne[1]))
    
plt.plot(les_t,les_angles)
plt.show()