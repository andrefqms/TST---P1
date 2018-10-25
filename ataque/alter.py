# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818

num_times = int(raw_input())
gols_p = []
times_conjunto = []
med = 0.0

for i in range(int(num_times)) :
	time = raw_input()
	times_conjunto.append(time)
	gols = int(raw_input())
	gols_p.append(gols)
	med += gols

med = med / num_times
times_melhor_ataque = []
maior_ataque = gols_p[0]

for i in range(1, len(gols_p)) :
	if gols_p[i] >= maior_ataque :
			maior_ataque = int(gols_p[i])
for i in range(len(gols_p)):
	if gols_p[i] == maior_ataque:
		times_melhor_ataque.append(times_conjunto[i]) 
print "Time(s) com melhor ataque (%d gol(s)):" % maior_ataque
for i in range(len(times_melhor_ataque)) :
	print times_melhor_ataque[i]
print ""

print "Média de gols marcados: %.1f" % med
