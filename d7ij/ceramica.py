# coding: utf-8
#André Filipe Queiroz
# cerâmica
#andre.soares@ccc.ufcg.edu.br

w = float(raw_input('Capacidade de revestimento? '))

print "\n== Dados do vão a revestir =="

x = float(raw_input('Comprimento? '))
y = float(raw_input('Largura? '))
z = float(raw_input('Altura? '))
A = 4*x*z
B = y*x
T = A + B
N = T/w

print "\n== Resultados =="
print "Área total a revestir: %.1f m2" % T 
print "Número de caixas: %d"% N
