# AMov
Movement Analysis (with a Bitalino), Developed for a master student who worked at AnimalCare.
	O objectivo do programa desenvolvido para o mestrado do Daniel (ao qual dei o nome de AMov) é analisar o movimento de um animal com o bitalino preso, ao longo do tempo (em segundos).
	O programa foi desenvolvido em python e está disponivel no github (https://github.com/PedroAntunes178/AMov/) para qualquer pessoa que queira usufruir deste software.
	Os dados utilizados neste programa são os dados recolhidos pelo programa OpenSignals (r)evolution do bitalino (https://bitalino.com/en/software) guardados em ficheiro tipo .txt.
	A analise do movimento é feita a partir dos valores obtidos a partir do sensor de aceleração do bitalino (https://bitalino.com/datasheets/ACC_Sensor_Datasheet.pdf).
O sensor retorna a aceleração em três eixos (x, y, z).
A unidade dos valores é g (https://pt.wikipedia.org/wiki/G_(física)).
Destes valores retiro a variação da aceleração a cada intervalo de cinco milisegundos em cada eixo e é somado as três (x, y, z).
Isto para depois representar isso num gráfico da variação da aceleração ao longo do tempo.
A soma executada no programa é a seguinte: soma = abs(data[x][k]-data[x][k+1]) + abs(data[y][k]-data[y][k+1])+ abs(data[z][k]-data[z][k+1]).
