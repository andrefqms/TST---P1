# coding: utf-8
# Matricula: 116210818
# Aluno: André Filipe Queiroz de Melo e SOares
# Atividade: Ordena Tipos

def ordena_tipos(lista):
	numeros = []
	letras = []
	misto = []
	for i in range(len(lista)):
		if lista[i].isdigit():
			numeros.append(lista[i])
		elif lista[i].isalpha():
			letras.append(lista[i])
		else: 
			misto.append(lista[i])
	print numeros
	print letras

	return numeros + letras + misto


print ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8'])



digit = numeros
alpha = letra
isalnum = misto
