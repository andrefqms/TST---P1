# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Imprime Sequencias de Números Inteiros

entrada = int(raw_input())
contador = 0
while True:
	cont = 0
	seq = raw_input()
	if seq == 'fim':
		break
	num = seq.split()
	for i in num:
		if int(i) > entrada:
			cont += 1
	contador += 1
	if cont > (int(len(num))/2):
		print 'sequencia %d: %s' % (contador,seq)
	
