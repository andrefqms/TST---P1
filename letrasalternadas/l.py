# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Letras Alternadas

def letras_alternadas(string):
	nova_string = ""
	for i in range(0,len(string),2):
		nova_string += string[i]
	
	return nova_string

assert letras_alternadas("casa") == 'cs'
assert letras_alternadas("exemplo") == "eepo" 
