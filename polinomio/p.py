# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Aplicação Polinômios

def aplicacao_polinomios(entrada,valor):
	
	if entrada[0] == 'p:':
		lista = []
		equacao = 0
		j = 0
		# print 'novo polinomio'
		for i in range(len(entrada)-1,0,-1):
			lista.append(entrada[i])
		for i in range(len(lista)-1,0):
			equacao += (int(lista[i]) ** i) * lista_valor[j]
			j += 1
		# problema no ultimo item da equação
		equacao += lista[len(lista)-1]
		



while True:
	entrada = raw_input().split()
	if entrada[0] == 'fim':
		break
	elif entrada[0] == 'p:':
		valor = int(raw_input())
		lista_valor = []
		lista_valor.append(valor)


