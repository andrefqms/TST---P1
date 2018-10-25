# coding: utf-8
#André Filipe Queiroz
# triangulo
#andre.soares@ccc.ufcg.edu.br

import math

x1 = int(raw_input())
y1 = int(raw_input())

x2 = int(raw_input())
y2 = int(raw_input())

x3 = int(raw_input())
y3 = int(raw_input())

d = math.sqrt( ((x1-x2)**2) + ((y1-y2)**2) )
e = math.sqrt( ((x2-x3)**2) + ((y2-y3)**2) )
f = math.sqrt( ((x3-x1)**2) + ((y3-y1)**2) )



P =(e + f + d)

print "O perímetro é de %.2f" % P
