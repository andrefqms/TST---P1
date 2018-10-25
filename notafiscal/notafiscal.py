# coding: utf-8
valor_total = float(raw_input())
data = raw_input()
quantidade_de_produtos = int(raw_input())

media = (valor_total) / (quantidade_de_produtos)
print "Data:", data
print "O valor total da compra foi de R$ %.2f." %(valor_total) , "A média do preço dos produtos é de %.1f." %(media)
