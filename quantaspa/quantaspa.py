# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Quantas PAs?


razao = int(raw_input())
lista_entrada = []
contador = 0
cont = 0

while True:
	entrada = raw_input()
	if entrada == 'fim':
		break
	lista_entrada = entrada.split()
	for i in range(len(lista_entrada)-1):
		if (int(lista_entrada[i]) + razao) == int(lista_entrada[i+1]):
			contador += 1
	if (len(lista_entrada) - 1) == contador:
		print "*"
		cont += 1

print '%d' % cont
