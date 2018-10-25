# coding: utf-8
# matricula: 166210818


mtp = int(raw_input())

if mtp == 1:
	a = float(raw_input())
		
	print a
	print'Aluno ainda não aprovado na unidade'

 
if mtp == 2:
	a = float(raw_input())
	b = float(raw_input())
		
	m = (a+b)/2
	if m < 6:
		print m
		print'Aluno ainda não aprovado na unidade'
	elif m >= 6:
		print m
		print'Aluno aprovado na unidade'
if mtp == 3:
	a = float(raw_input())
	b = float(raw_input())
	c = float(raw_input())	
	m = ((a+b+c)/3) - 0.5
	if m < 6:
		print m
		print'Aluno ainda não aprovado na unidade'
	elif m >= 6:
		print m
		print'Aluno aprovado na unidade'
if mtp == 4:
	a = float(raw_input())
	b = float(raw_input())
		
	m = ((a+b+c+d)/4) - 0.5
	if m < 6:
		print m
		print'Aluno ainda não aprovado na unidade'
	elif m >= 6:
		print m
		print'Aluno aprovado na unidade'

