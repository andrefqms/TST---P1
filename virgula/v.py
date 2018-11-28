# coding: utf-8
# Aluno: André Filipe Queiroz
# Matricula: 116210818

resultado = ""
frase =  raw_input()
inicial = int(raw_input())
final = int(raw_input())

for indice in range (inicial,final):
    if indice != inicial or indice != final:
        if frase[indice] == " ":
            resultado += " ,"
        elif indice == inicial :
            resultado += frase[indice]
           
        else:
            resultado += " " + frase[indice]
print resultado
