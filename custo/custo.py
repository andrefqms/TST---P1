# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818
# Atividade: INSS
salario = float(raw_input())
a = (salario * 0.12)
x = 'O valor da contribuição do INSS a ser pago pelo empregador é de R$'
y = 'O valor da contribuição do INSS a ser pago pelo empregado é de R$'
if salario <= 1317.07:
    b = (salario * 0.08)
    print x, '%.2f' % a 
    print y, '%.2f' % b
elif salario >= 1317.08 and salario <= 2195.12:
    c = (salario * 0.09)
    print x, '%.2f' % a 
    print y, '%.2f' % c
else:
    d = (salario * 0.11)
    print x, '%.2f' % a 
    print y, '%.2f' % d

