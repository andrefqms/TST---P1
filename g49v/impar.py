# coding: utf-8

x = int(raw_input())

if x % 2 == 0 :
	for numero_impar in range(x+1,x+12,2):
		print numero_impar
else:
	for numero_impar in range(x,x+12,2):
		print numero_impar
