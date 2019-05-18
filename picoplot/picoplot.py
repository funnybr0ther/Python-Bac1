from numpy import *
import matplotlib.pyplot as plt
file = open("/home/guillaume/Documents/python/picoplot/Tension_L2.txt","r")
lines = []
i = 0
for line in file:
    if i%12 ==0:
        lines.append(line.strip())
    i+=1
lines = lines[3:]
trucs_lines = [(float(i.split("\t")[0]) , float(i.split("\t")[1])) for i in lines]
x = array([i[0] for i in trucs_lines])
y = array([i[1] for i in trucs_lines])
plt.plot(x,y,label = "Tension sur L_2")
plt.legend(loc = 'upper right')
plt.show()