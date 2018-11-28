# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818

def ordena_tipos(lista1):
	lista = []
	for i in range(len(lista1)-1,-1,-1):
		if lista1[i].isdigit() == True:
			lista.append(lista1[i])
		elif lista1[i].isalpha() == True:
			lista.append(lista1[i])
		elif lista1[i].isalnum() == True:
			lista.append(lista1[i])
		else:
			lista.append(lista1[i])
	return lista

print ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8'])
