# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Dígitos de Verificação do CPF

def calcula_digitos_verificacao(string):
	soma = 0
	cont = 2
	lista_espelhada = []
	for i in range(len(string)-1,-1,-1):
		soma += int(string[i]) * cont
		cont += 1
		lista_espelhada.append(string[i])
	num1 = str((10 * soma) % 11)
	if num1 == '10':
		num1 = '0'
	
	for i in range(len(lista_espelhada)-1,-1,-1):
		soma += int(string[i]) * cont
		cont += 1
	num2 = str((10 * soma) % 11)
	if num2 == '10':
		num2 = '0'	
	
	return num1+num2

print calcula_digitos_verificacao('0000000019') 
