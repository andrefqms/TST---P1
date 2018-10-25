# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818

def ordena_tipos(lista):
	numeros = []
	letras = []
	resto = []
	for i in range(len(lista)):
		if lista[i].isdigit():
			numeros.append(lista[i])
		elif lista[i].isalpha():
			letras.append(lista[i])
		else:
			resto.append(lista[i])
		
	return numeros + letras + resto



print ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8']) 


