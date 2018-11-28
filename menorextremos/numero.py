# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Classifica Números pelo Menor dos Extremos

numero = int(raw_input())
lista = []
y = 0
z = 0
w = 0
k = 0
for i in range (int(numero)):
    if numero > 1 :
        sequencia = raw_input()
        lista.append(sequencia)

for i in range(len(lista)):
        if lista[0] > lista[i]:
            y = y + 1
        elif lista[0] < lista[i]:
            z = z + 1
for i in range(len(lista)):
        if lista[len(lista)-1] > lista[i]:
            w = w + 1
        elif lista[len(lista)-1] < lista[i]:
            k = k + 1

if lista[0] > lista[len(lista)-1]:
    print 'Menor dos extremos: %s' % (lista[len(lista)-1])
    print '%d número(s) abaixo do menor' % w 
    print '%d número(s) acima do menor' % k
elif lista[0] < lista[len(lista)-1]:  
    print 'Menor dos extremos: %s' % (lista[0])
    print '%d número(s) abaixo do menor' % y 
    print '%d número(s) acima do menor' % z
elif lista[0] == lista[len(lista)-1]:
    print 'Menor dos extremos: %s' % (lista[len(lista)-1])
    print '%d número(s) abaixo do menor' % y
    print '%d número(s) acima do menor' % z

