# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Quantidade e Média de Números Pares

numero_quantidade = int(raw_input())
soma = 0
pares = 0
numeros = []
abaixo = 0

for i in range(numero_quantidade):
	numero = float(raw_input())
	numeros.append(numero)
	if numero%2 == 0:
		pares += 1
		soma += numero

media = soma/pares

for i in numeros:
	if i < media:
		abaixo += 1
	
print "soma: %d" % soma

print "média: %.1f" % media

print "%d número(s) abaixo da média" % abaixo

		
