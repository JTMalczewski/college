import numpy as np
import matplotlib.pyplot as plt
import math


dz, X, Y = 0.001, 250, 80
y_1, y_2 = 0.4, -0.4
Q = -1
mi = 1

# i_k, j_k = 

def warunkiBrzegowe(macierz_1, macierz_2, X, Y):
    for j in range(40,Y):
        macierz_1[0][j] = Q/(2*mi) * (math.pow(j*dz,3)/3 + y_1*y_2*j*dz)
        macierz_1[X-1][j] = Q/(2*mi) * (math.pow(j*dz,3)/3 + y_1*y_2*j*dz)
        macierz_2[0][j] = Q/(2*mi) * (2*j*dz)
        macierz_2[X-1][j] = Q/(2*mi) * (2*j*dz)

    for j in range(0,40):
        macierz_1[0][j] = Q/(2*mi) * (math.pow(-j*dz,3)/3 + y_1*y_2*-j*dz)
        macierz_1[X-1][j] = Q/(2*mi) * (math.pow(-j*dz,3)/3 + y_1*y_2*-j*dz)
        macierz_2[0][j] = Q/(2*mi) * (2*-j*dz)
        macierz_2[X-1][j] = Q/(2*mi) * (2*-j*dz)

    for i in range(100,X):
        macierz_1[i][0] = Q/(2*mi) * (math.pow(j*dz,3)/3 + y_1*y_2*j*dz)
        macierz_1[i][Y-1] = Q/(2*mi) * (math.pow(j*dz,3)/3 + y_1*y_2*j*dz)
        macierz_2[i][0] = Q/(2*mi) * (2*j*dz)
        macierz_2[i][Y-1] = Q/(2*mi) * (2*j*dz)

    for i in range(0,100):
        macierz_1[i][0] = Q/(2*mi) * (math.pow(j*dz,3)/3 + y_1*y_2*j*dz)
        macierz_1[i][Y-1] = Q/(2*mi) * (math.pow(j*dz,3)/3 + y_1*y_2*j*dz)
        macierz_2[i][0] = Q/(2*mi) * (2*j*dz)
        macierz_2[i][Y-1] = Q/(2*mi) * (2*j*dz)


siatka_1 = np.zeros((X,Y))
siatka_2 = np.zeros((X,Y))

print(np.shape(warunkiBrzegowe(siatka_1,siatka_2,X,Y)))
print(1)
