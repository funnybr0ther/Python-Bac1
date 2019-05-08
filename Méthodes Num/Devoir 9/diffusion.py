from numpy import *
def diffusion(T, beta, nt):
    matrice = copy(T)
    for t in range(nt):
        matrice[1:-1,1:-1] = matrice[1:-1,1:-1] + beta*(matrice[2:,1:-1] + matrice[0:-2,1:-1]+ matrice[1:-1,0:-2] + matrice[1:-1,2:]-4*matrice[1:-1,1:-1])
    return matrice
def diffusionSmart(T,beta,nt):
    matrice = flip(T,1)
    matrice = hstack((matrice,matrice[:,-2].reshape(matrice.shape[0],1)))
    for t in range(nt):
        matrice[1:-1,1:-1] = matrice[1:-1,1:-1] + beta*(matrice[2:,1:-1] + matrice[0:-2,1:-1]+ matrice[1:-1,0:-2] + matrice[1:-1,2:]-4*matrice[1:-1,1:-1])
        matrice[:,-1]  = matrice[:,-3]
    return flip(matrice[:,:-1],1)
