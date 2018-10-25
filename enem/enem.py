# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Aprovados no ENEM

lista = []

while True:
	entrada = raw_input()
	if entrada == 'fim':
		break
	lista.append(entrada)

corte = int(raw_input())

Verificador = True
for i in lista:
	aluno , nota = i.split()
	if int(nota) >= corte:
		print "%s, %s" %(aluno,nota)
		Verificador = False
if Verificador:
	print "Nenhum candidato aprovado."
