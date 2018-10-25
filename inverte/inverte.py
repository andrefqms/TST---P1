# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818

def inverte2a2_condicional(seq):
	if len(seq) % 2 == 0:
		for i in range(0,len(seq),2):
			if seq[i] > seq[i+1]:
				seq[i],seq[i+1] = seq[i+1],seq[i]
			else:
				seq[i+1],seq[i] = seq[i+1],seq[i]
	elif len(seq) % 2 != 0:
		for i in range(0,len(seq)-2,2):
			if seq[i] > seq[i+1]:
				seq[i],seq[i+1] = seq[i+1],seq[i]
		
seq = [3,1,2,3,10,5,6]
inverte2a2_condicional(seq)
assert seq == [1,3,2,3,5,10,6]

seq = [5,4,3,2,1]
inverte2a2_condicional(seq)
assert seq == [4,5,2,3,1]



