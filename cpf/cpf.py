# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Dígitos de Verificação do CPF

def calcula_digitos_verificacao(string):
	soma = 0
	soma2 = 0
	contador = 2
	lista_contrario = []
	for i in range(len(string)-1,-1,-1):
		soma += int(string[i]) * contador
		contador += 1
		lista_contrario.append(string[i])
	num1 = str((10 * soma) % 11)

	if num1 == '10':
		num1 = '0'

	lista = [num1]
	lista_contr = lista + lista_contrario 

	contador = 2
	for i in range(len(lista_contr)-1):
		soma2 += int(lista_contr[i]) * contador
		contador += 1
	num2 = str((10 * soma2) % 11)

	if num2 == '10':
		num2 = '0'	
	
	return 	num1 + num2


