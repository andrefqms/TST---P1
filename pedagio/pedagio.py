# coding: utf-8
# matricula: 116210818

veiculo = raw_input()

if veiculo == 'Automóvel utilitário':
	
	print 'Valor a pagar: R$ 11.40.' 
elif veiculo == 'Ônibus':
	eixo = int(raw_input())
	print 'Valor a pagar: R$ %.2f.' % ( eixo * 11.40)
elif veiculo == 'Caminhão':
	eixo = int(raw_input())
	print 'Valor a pagar: R$ %.2f.' % ( eixo * 9.60)
elif veiculo == 'Motocicleta':
	print 'Valor a pagar: R$ 5.70.' 
else:
	print'Veículo não cadastrado.'
