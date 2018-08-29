from sklearn.cluster import KMeans as KM
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd


datos=pd.read_csv("Base de datos UCB.csv",header=0)
dt=pd.DataFrame(datos)

dt =dt.drop(['Estado_civil','CUESTIONARIO','Nacimiento','Carrera','Asist_Clases','Trabajo','Col_Procedencia','Hijos_18','SemestreOutliers','InicioTesisOutliers','Malestar_emocional','Estado_Civil_carrera','Estado_Civil_tesis'],axis=1)

dt=dt.fillna(0)
print dt
#asignamo el numero de clusters
k=2
model=KM(n_clusters=k)
model=model.fit(dt)
labels=model.labels_

centro=model.cluster_centers_

colors=['blue','red','green','black']
y=0
for x in labels:
    plt.scatter(dt.iloc[y,0],dt.iloc[y,1]
    ,color=colors[x])
    y+=1
    
    
for x in range(k):
    lines=plt.plot(centro[x,0],
    centro[x,1],'kx')
    plt.setp(lines,ms=15.0)
    plt.setp(lines,mew=2.0)
    
    
title=('n de clus(k)={}').format(k)
plt.title(title)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
        