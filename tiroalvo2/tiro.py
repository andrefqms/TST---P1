# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Tiro ao Alvo 2

import math

lista = []
lista2 = []
cont = 0
melhores = []
quantidade = 0
soma = 0.0

while True:
	entrada = raw_input()
	lista.append(entrada)
	if len(lista) == 2:
		distancia = math.sqrt((float(entrada[0]))**2 + (float(entrada[1]))**2)
		if distancia > 200.0:
			break
		elif distancia <= 200.0:
			cont += 1
			lista2.append(distancia)

for i in lista2:
	if float(lista2[i]) < float(lista2[i+1]):
		print '%.2f cm (melhor tiro)' % float(i)
		melhores.append(i)
	else:
		print '%.2f cm' % float(i)

for i in lista2:
	quantidade += 1
	soma += float(i)

media = soma/quantidade

print '--'
for i in melhores:
	if float(melhores[i]) < float(melhores[i+1]):
		print 'melhor tiro: %.2f cm' % float(i)
print 'distancia media: %.2f' % media









