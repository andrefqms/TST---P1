# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Classifica Números

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

if (a+b+c) % 3 ==0:
	print'plif'
elif (a+b+c) % 5 ==0:
	print'plof'
else:
	print a+b+c
