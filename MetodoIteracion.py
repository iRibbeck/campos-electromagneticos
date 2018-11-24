"""
Created on Sat Nov 24 2018

@author: Ignacio Ribbeck 

@email: iRibbeck@outlook.com
"""

import numpy as np
import matplotlib.pyplot as plt


#Potencial de las lineas
v1=10
v2=100
v3=40
v4=0

#numero de puntos por eje 
nx=16
ny=11

#numero de iteraciones
ni=500

#crear una matriz de ceros de la dimension de los puntos
v = np.zeros((nx,ny))

#Asignar los potenciales
for i in range(1,nx):
    v[i][0] = v1        #Columna 0, fila 1 hasta nx
    v[i][-1] = v3       #Ultima culumna, fila 1 hasta nx

for j in range(1,ny):
    v[0,j] = v4
    v[-1,j] = v2

v[0,0] = 0.5*(v1 + v4)
v[-1,0] = 0.5*(v1 + v2)
v[0,-1] = 0.5*(v3 + v4)
v[-1,-1] = 0.5*(v2 + v3)



for k in range(ni):
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            v[i,j] = 0.25*( v[i-1,j] + v[i,j+1] + v[i+1,j] + v[i,j-1] )
            

#Hasta este punto todo funciona como lo esperado, verificado leyendo la variable v[] desde
#el explorador de spyder 3


plt.pcolormesh(v, shading='gouraud')
plt.show
