# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818

def ordena_tipos(inteiros,letras,alfanuméricos):
	lista = []
	for i in range(len(lista)):
		if lista[i].isdigit() == True:
			lista.append(lista[i])
		elif lista[i].isalpha() == True:
			lista.append(lista[i])
		else:
			lista.append(lista[i])
	return lista

print ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8']) 
