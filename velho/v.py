# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Mais Velhos Primeiro

def idosos_inicio(lista):
	contador = 0
	for i in range(len(lista)):
		if lista[i] >= 60:
			lista[i], lista[contador] = lista[contador], lista[i]
			contador += 1
	
fila = [25, 33, 67, 61, 35, 8, 12, 15, 22, 63, 75, 30, 34]
idosos_inicio(fila)
assert fila == [67, 61, 63, 75, 35, 8, 12, 15, 22, 25, 33, 30, 34]

