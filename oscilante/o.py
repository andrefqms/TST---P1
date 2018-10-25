# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Números Oscilantes

def numero_oscilante(entrada):
	verificar = True
	for i in range(len(entrada)-1): 
		if int(entrada[i]) % 3 == 0 and int(entrada[i+1]) %3 != 0 or int(entrada[i]) % 3 != 0 and int(entrada[i+1]) % 3 == 0:
			verificar = True
		elif int(entrada[i]) % 2 == 0 and int(entrada[i+1]) % 2 != 0 or int(entrada[i]) % 2 != 0 and int(entrada[i+1]) % 2 == 0:
			verificar = True
		else:
			verificar = False
				
	if verificar == True:
		return 'verdadeiro'
	elif verificar == False:
		return 'falso'
	
entrada = raw_input()

print '%s: %d algarismos.' % (numero_oscilante(entrada),len(entrada))
