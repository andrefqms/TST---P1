# coding: utf-8
# matricula: 166210818


codigo = raw_input()

if codigo == 1:
	print'Deverá receber em dezembro R$ 25000.00.'
if codigo == 2:
	print'Deverá receber em dezembro R$ 15000.00.'
if codigo == 3:
	faltas = raw_input()
	G = (235 - faltas) * 2.00
	print'Valor da gratificação R$ 500.00'
	print'Deverá receber em dezembro R$ %.2f.' % (8000.00 + G)
if codigo == 4:
	faltas = raw_input()
	G = (235 - faltas) * 1.00
	print'Valor da gratificação R$ 300.00'
	print'Deverá receber em dezembro R$ %.2f.' % (5000.00 + G)
if codigo == 5:
	faltas = raw_input()
	G = (235 - faltas) * 0.70
	print'Valor da gratificação R$ 200.00'
	print'Deverá receber em dezembro R$ %.2f.' % (2800.00 + G)
