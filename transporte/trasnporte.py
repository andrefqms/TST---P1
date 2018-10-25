# coding: utf-8
# matricula: 166210818



pessoa = int(raw_input())
dinheiro = float(raw_input())


if dinheiro < 101:
	if dinheiro == 100:
		print'TAV. R$ 100.00'
	elif dinheiro < 100:
		if dinheiro < 22:
			print'Não é possível realizar a viagem.'

		elif dinheiro > (pessoa*22):
			print'Ônibus. R$ %.2f' % (pessoa * 22)
		elif dinheiro == 22:
			print'Ônibus. R$ 22.00'

elif dinheiro > 100:
	if pessoa >= 2 and pessoa < 5:
		print'Táxi. R$ 200.00'
	elif pessoa > 4:
		if dinheiro > 88:
			print'Ônibus. R$ %.2f' % (pessoa * 22)
		elif dinheiro < 88:
			print'Não é possível realizar a viagem.'
	elif pessoa == 1:
		print'TAV. R$ 100.00'

