# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Encontra elemento

lista = []
quantidade_numero = int(raw_input())
menor_extremos = 0
menor = 0
maior = 0

for i in range (quantidade_numero):
	numero = int(raw_input())
	lista.append(numero)

if lista[0] < lista[quantidade_numero-1]:
	menor_extremos = int(lista[0])
else:
	menor_extremos = int(lista[quantidade_numero-1])

for i in range (quantidade_numero):
	if lista[i] < menor_extremos:
		menor += 1
	elif lista[i] == menor_extremos:
		menor
	elif lista[i] > menor_extremos:
		maior += 1

print "Menor dos extremos: %d" % menor_extremos
print "%d número(s) abaixo do menor" % menor
print "%d número(s) acima do menor" % maior
