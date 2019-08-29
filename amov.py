import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def creat_grath():
	fig = plt.figure(1)
	ax = fig.add_subplot(111)
	ax.axis([0, 60, 0, 6])
	plt.ylabel('Variação da aceleração')
	plt.xlabel('sec')

def plot_graph():
	var_acc = list()
	tempo = list()
	index = 2
	for k in range(len(data[0])-1):
		soma = 0
		for index in [2,3,4]:
			soma = soma + abs(data[index][k]-data[index][k+1])
		var_acc.append(soma)
	for k in range(1,len(data[0])):
		tempo.append(data[0][k]/200)
	ax.plot(tempo, var_acc)

def clean_graph():
	ax.clear()
	for k in range(len(var_acc)):
		var_acc.pop()
		tempo.pop()

def get_file(str):
	#doc = input("Escreva o nome do documento: ")
	direc = 'files/' + str + '.txt'
	print(direc)
	data=pd.read_csv(direc, sep="\t", header=None, engine='python', skiprows=3)
	print(data)

def get_info():
	point = input("Em que sec queres começar a contar: ")
	k = 0
	val = 0
	for k in range(int(point)*200,int(point)*200+1200):
		val = val + var_acc[k]
	print(val)
