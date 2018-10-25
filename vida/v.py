# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Vida Collatz

cont = 0
entrada = int(raw_input())
while True:
	cont += 1

	if entrada == 1:
		break
	if entrada % 2 == 0:
        	entrada = entrada / 2
	else:
		entrada = 3 * entrada + 1

print cont 
