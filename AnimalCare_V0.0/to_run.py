import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import time


fig = plt.figure(1)
ax = fig.add_subplot(111)
plt.ylabel('Variação da aceleração')
plt.xlabel('sec')
plt.axis([0, 60, 0, 6])

doc = input("Escreva o nome do documento: ")
direc = '/home/pedro/Documents/AnimalCare_V0.0/' + doc + '.txt'
print(direc)
data=pd.read_csv('/home/pedro/Documents/AnimalCare_V0.0/' + doc + '.txt', sep="\t", header=None, engine='python', skiprows=3)

index = 2
var_acc = list()
k = 0
for k in range(len(data[0])-1):
	tot = 0
	for index in [2,3,4]:
		tot = tot + abs(data[index][k]-data[index][k+1])
	var_acc.append(tot)

tempo = list()
k = 0
for k in range(1,len(data[0])):
	tempo.append(data[0][k]/200)

ax.plot(tempo, var_acc)

for k in range(len(var_acc)):
	var_acc.pop()


point = input("Em que sec queres começar a contar: ")
k = 0
val = 0
for k in range(int(point)*200,int(point)*200+1200):
	val = val + var_acc[k]
print(val)
