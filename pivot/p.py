# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: pivot

def pivot(lista):
	p = lista[0]
	for i in range(0,len(lista)-1):
		for i in range(len(lista)):
			if lista[i] < lista[0]:
					lista[0],lista[i] = lista[i], lista[0]
	
	# errado

	for i in range(len(lista)-1,2,-1):
		if lista[i] > lista[i+1]:
			lista[i],lista[i+1] = lista[i+1], lista[i]
	return lista

numeros = [6, 4, 8, 1, 7, 3]
pivot(numeros)
print numeros 
