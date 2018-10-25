# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Encontra elemento

numero = int(raw_input())
numeros = raw_input()
numeros_lista = numeros.split()
verificador = False

for elemento in numeros_lista:
    if int(elemento) == numero:
        print "sim"
	verificador = True
        break
        
if verificador != True:
    print "não"
