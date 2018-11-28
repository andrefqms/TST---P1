# coding: utf-8
# matricula : 161210818

semestre = int(raw_input())


pont_ensino = int(raw_input())

prod_intelectual = int(raw_input())

orientacao = int(raw_input())

adm = int(raw_input())

media = (pont_ensino + prod_intelectual + orientacao + adm) / 4


if semestre < 4:
	print 'Promoção indeferida. Número de semestres insuficiente.'

if pont_ensino < 320 or prod_intelectual < 100 or prod_intelectual < 20 or prod_intelectual <= 0:
	print 'Promoção indeferida. Pontuação mínima não alcançada.'

if media < 140:
	print 'Promoção indeferida. Média insuficiente.'

elif media >= 140 and semestre == 4 and pont_ensino >= 320 and prod_intelectual >= 100 and prod_intelectual >= 20 and prod_intelectual > 0:
	print 'Promoção deferida. Parabéns!'
