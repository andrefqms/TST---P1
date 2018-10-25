# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Merge

def merge(lista1, lista2):
	resultado = []
	i1 , i2 =  0 , 0
	while True:
		if i1 == len(lista1) or i2 == len(lista2):
			break
		if lista1[i1] <= lista2[i2]:
			resultado.append(lista1[i1])
			i1 += 1
		else:
			resultado.append(lista2[i2])
			i2 += 1
	if i1 == len(lista1):
		lista_restante =  lista2
		inicio = i2
	elif  i2 == len(lista2):
		lista_restante =  lista1
		inicio = i1
	for j in range(inicio, len(lista_restante)):
		resultado.append(lista_restante[j])
	return resultado
