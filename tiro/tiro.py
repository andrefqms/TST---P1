# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Tiro ao Alvo

import math

lista = []
cont = 0
quantidade = 0
soma = 0.0
media = 0.0

while True:
	posicao = raw_input().split(",")
	distancia = math.sqrt((float(posicao[0]))**2 + (float(posicao[1]))**2)
	if distancia > 200.0:
		break
	elif distancia <= 200.0:
		cont += 1
		lista.append(distancia)
	
for i in lista:
  soma += float(i)
		
if ( cont > 0):
 media = soma / float(cont)

for i in lista:
  print '%.2f' % i

print "--"
print "num disparos: %d" % cont
print "distancia media: %.2f" % media
