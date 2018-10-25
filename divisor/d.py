# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade:  Divisor


def divisor(num, lista):
	indice = 0
	ind = 0
	for i in range(len(lista)):
		if lista[i] % num == 0:
			indice += i
			break
	for i in range(len(lista)):	
		if lista[i] % num != 0:
			ind += 1
	if ind == len(lista):
		return -1		
	else:		
		return indice

lista1 = [100,10,40,50]
lista2 = [3,15,50,23,5]
print divisor(10, lista1)
print divisor(5, lista2) 

