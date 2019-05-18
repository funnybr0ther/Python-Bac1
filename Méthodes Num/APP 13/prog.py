from numpy import *
def waveSolve(beta, nx, nt, c, L, Uo):
    vector = copy(U_0) 
    delta_t = (L/nx) * beta / c
    T = delta_t * nt
    Uoo = (2*Uo + ((c*dt)**2)*D @ Uo)/2
    for t in range(nt):
        ancient_vector = vector
        vector[1:-1] = vector[1:-1] + beta*(matrice[2:] - 2*matrice[1:-1]+ matrice[0:-2]) - ancient_vector[1:-1]
    return matrice
def diffusionSmart(T,beta,nt):
    matrice = flip(T,1)
    matrice = hstack((matrice,matrice[:,-2].reshape(matrice.shape[0],1)))
    for t in range(nt):
        matrice[1:-1,1:-1] = matrice[1:-1,1:-1] + beta*(matrice[2:,1:-1] + matrice[0:-2,1:-1]+ matrice[1:-1,0:-2] + matrice[1:-1,2:]-4*matrice[1:-1,1:-1])
        matrice[:,-1]  = matrice[:,-3]
    return flip(matrice[:,:-1],1)
