# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Binary Coded Decimal

BCD = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001']
DECIMAL = [0,1,2,3,4,5,6,7,8,9]
numero = ""
cont = 0
x = 0
while True:
	entrada = raw_input()
	if entrada == 'fim':
		break
	if len(entrada) < 8:
		x += 1
	elif entrada != 'fim':

		for i in range(len(BCD)):
			if int(entrada[0:4]) != int(BCD[i]) or int(entrada[4:7]) != int(BCD[i]): 
				cont += 1
			elif int(entrada[0:4]) == int(BCD[i]) and int(entrada[4:7]) == int(BCD[i]):
				for e in len(DECIMAL):
					for i in BCD:
						if i[i] == e[i]:
							numero = numero + int(i[i])
				print '%d' % numero
	
		if cont > 0:
			print  'BCD inválido.'	
		
if x > 0:
	print 'Tente novamente.'
