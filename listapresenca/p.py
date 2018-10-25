# coding: utf-8
# Matricula: 116210818
# Aluno: André Filipe Queiroz de Melo e SOares
# Atividade: Lista Presença

def cria_lista_presenca(turmas, nomes, turma):
	lista = []
	for i in range(len(turmas)):
		if  turmas[i] == turma:
			lista.append(nomes[i])

	
	return lista

turmas = [1, 2, 2, 4, 5, 3, 5]
nomes = ["Maria", "Pedro", "Carlos", "Ana", "Carla", "Joao", "Jose"]
print cria_lista_presenca(turmas, nomes, 5) 
