# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: limite de gastos

lista_resultado = []
media = float(raw_input())
while True:
	lista_temporaria = 0
	media_temporaria  = 0
	somador_temporario = 0
	cont = 0
	entrada = raw_input()
	resultado = ""
	if entrada == "fim":
		break
	lista_temporaria = entrada.split()
	for elemento in lista_temporaria:
		somador_temporario += float(elemento)
		cont += 1
	media_temporaria = somador_temporario / cont
	if media_temporaria * 2 <= media:
		break
	if media_temporaria > media:
		for indice in range(len(lista_temporaria)):
			if indice == len(lista_temporaria) -1:

				resultado += "%.1f" % float(lista_temporaria[indice])
			else:
				resultado += "%.1f " % float(lista_temporaria[indice])

		lista_resultado.append(resultado)


for elemento in lista_resultado:

	if elemento != "":

		print elemento
