# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Quantos Comeram?

def quantos_comeram(N, fila):
	alimentados = 0
	for i in range(len(fila)):
		N -= fila[i]
		if N >= 0:
			if N < fila[i]:
				alimentados += fila[i]
			else:
				alimentados += fila[i]
	return alimentados


