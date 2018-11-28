# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: Quantidade e Média de Números Pares

numero_quantidade = int(raw_input())
x = 0
y = 0
soma = 0
lista = []

for i in range(numero_quantidade):
    if numero_quantidade > 0:
        numeros = int(raw_input())
        lista.append(numeros)
        if numeros % 2 == 0:
            x = x + 1
            soma += numeros
            media = soma/x


print 'soma: %d' % soma
print 'média: %.1f' % media

for i in range(len(lista)):
     
    if float(lista[i]) < media:
         y = y + 1

print '%d número(s) abaixo da média' % y

