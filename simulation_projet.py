"""
Programme réalisé par Guillaume VDREST (surtout)et  Théo VDD(allé un peu qd meme)
Novembre 2018
"""

import math
import matplotlib.pyplot as plt
import numpy as np


l1 = 30
l2 = 30
h2 = 10
l3 = 30
l4 = 7
h4 = 5
Elastic = 15
Volant = 20
Pot = 25
Poids_voiture = 2*9.806
Frot_mu = 0.3
travail_Frot = 0
dap = 0.3

spring_angle = np.pi
rigidity_k = 0.04


global step

step = 0.1    # pas de simulation [m]
end = l1+l2+l3+l4       # fin de la simulation [m]

def direction(l):
    """
    pre: l distance parcourue [m]
    post: retourne la direction du robot à la distance l [rad]
    """
    if 0<=l<=l1:
        return 0
    if l1<l<=l1+l2:
        a = -h2*math.sin(((math.pi*2)*l/l2)-l1)/2
        b = -h2*math.sin(((math.pi*2)*(l+step)/l2)-l1)/2
        return (b-a)
    if l1+l2<l<=l1+l2+l3:
        return 0
    if l1+l2+l3<l<=l1+l2+l3+l4:
        return (h4/l4)*step


def y_pos_array(x_lst):
    """
    Determine the y position of the car
    """
    y = np.empty(len(x_lst))
    y[0] = 0
    for i in range(len(y)+1):
        try:
            y[i] = y[i-1] + direction(x_lst[i])
        except:
            pass
    return y


def compute_distance(x_lst,y_lst):
    """
    Compute the distance done in a certain interval dy/dx.
    Return an np array of the dl (related to dx)
    """
    distance = np.empty(len(x_lst))
    for i in range(len(x_lst)):
        try:
            distance[i] = ((y_lst[i+1]-y_lst[i])**2 + (x_lst[i+1]-x_lst[i])**2)**0.5
        except:
            pass
    return distance


def compute_inclinaison(x_lst, y_lst):
    """
    Compute the inclinaison on dy/dx
    Return an np array of the angle (related to dx)
    """
    inclinaison = np.empty(len(x_lst))
    for i in range(len(x_lst)):
        try:
            inclinaison[i] = math.atan((y_lst[i+1]-y_lst[i])/(x_lst[i+1]-x_lst[i]))
        except:
            pass
    return inclinaison


def compute_kinetic_energy(x_lst):
    kinetic_energy = np.empty(len(x_lst))
    return


def compute_potential_energy(x_lst,y_lst):
    """
    Compute the potential energy of the car
    Return an np array of the potential energy (in Joules)
    """        
    potential_energy = np.empty(len(x_lst))
    for i in len(x_lst):
        potential_energy[i] = y_lst[i] * Poids_voiture        
    return potential_energy


def compute_elastic_energy(x_lst, theta, trigger_x_pos, rigidity_k):
    """
    Compute the energy contained in the spring. It's full until it is at a certain point on the track. 
    After this point the energy equals 0 
    """
    elastic_energy = np.empty(len(x_lst))
    for i in range(len(x_lst)):
        if x_lst[i] < trigger_x_pos:
            elastic_energy[i] = (1/2)*rigidity_k*theta**2
        else:
            elastic_energy[i] = 0
    return elastic_energy                                                                 


def internal_friction_work(distance_list, equ_friction_coef):
    """
    Compute the work done by internal friction during a certain distance.
    Return an np array of the work done in a certain interval of distance dl
    """
    friction_work = np.empty(len(distance_lst))
    for i in range(len(distance_lst)):
        try:
            friction_work[i] = -1 * distance_lst[i] * equ_friction_coef 
        except:
            pass
    return friction_work


def compute_friction_work(distance_lst, inclinaison, friction_coef, car_weight):
    """
    Compute the work done by friction during a certain distance. Take care of the inclinaison
    Return an np array of the work done in a certain interval of distance dl
    """
    friction_work = np.empty(len(distance_lst))
    for i in range(len(distance_lst)):
        try:
            friction_work[i] = -1 *step * friction_coef * car_weight 
        except:
            pass
    return friction_work


def compute_total_work(f_work_lst):
    total_work = np.empty(len(f_work_lst))
    total_work[0] = 140
    for i in range(len(f_work_lst)):
        try:
            total_work[i+1] = total_work[i] + f_work_lst[i]
        except:
            pass
    return total_work 

def compute_distance_balistic_no_air(Ecinetic, l4, h4):
    speed = Ecinetic * 2 / Poids_voiture / 9.806
    speedx = speed * (l4/((l4**2 + h4 **2)**0.5))
    speedy = speed * (h4/((l4**2 + h4 **2)**0.5))
    t = speedy + ((speedy)**2 + 4 * h4 * 9.81)**0.5 / 9.81
    distance = speedx * t
    return distance*100

def compute_energy_volant(rayon, hauteur, masse, omega):
    return masse/8*(rayon**2 + (hauteur**2)/3) * omega**2

x = np.arange(0, end, step)    # distance parcourue [m]
y = y_pos_array(x)
distance = compute_distance(x,y)
inclinaison = compute_inclinaison(x,y)
f_work = compute_friction_work(distance,inclinaison,Frot_mu,Poids_voiture)
elastic_energy = compute_elastic_energy(x,spring_angle,10,rigidity_k)
e_tot = compute_total_work(f_work)
print(compute_energy_volant(0.045,0.01,0.5,50))
print(compute_distance_balistic_no_air(0,33,12))


plt.subplot(221, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, y, 'red', label="trajectoire")

plt.subplot(222, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, f_work, 'blue', label="distance")

plt.subplot(224, aspect='equal')  # grille 2x1, 2e graphique
plt.plot(x, e_tot, 'red', label="friction")

plt.show()