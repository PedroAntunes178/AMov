import pandas as pd
import numpy as np

def plot_graph(tempo, var_acc, data):
	for k in range(len(data[0])-1):
		soma = 0
		for index in [2,3,4]:
			soma = soma + abs(data[index][k]-data[index][k+1])
		var_acc.append(soma)
	for k in range(1,len(data[0])):
		tempo.append(data[0][k]/200)

def clean_values(tempo, var_acc):
	for k in range(len(var_acc)):
		var_acc.pop()
		tempo.pop()

def get_file(str):
	#doc = input("Escreva o nome do documento: ")
	direc = 'files/' + str + '.txt'
	print(direc)
	data=pd.read_csv(direc, sep="\t", header=None, engine='python', skiprows=3)
	return data

def get_info(point, var_acc, val):
	#point = input("Em que sec queres começar a contar: ")
	val = 0
	for k in range(int(point)*200,int(point)*200+1200):
		val = val + var_acc[k]
