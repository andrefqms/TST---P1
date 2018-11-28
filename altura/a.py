# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818

def insere_na_fila(lista,nome,altura):
	tupla = (nome,altura)
	lista.append(tupla)
	for indice in range(len(lista)-1,0,-1):
		if lista[indice -1][1] > lista[indice][1]:
			lista[indice -1] , lista[indice] = lista[indice] , lista[indice -1]
		else:
			break

fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]
insere_na_fila(fila, "jose", 1.12)

assert fila == [("maria", 1.05), ("joao", 1.09), ("jose", 1.12), ("ana", 1.16)]
