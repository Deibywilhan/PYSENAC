print("Desafio 2")
nota1=(input("Digite a sua primeira nota = "))
nota2=(input("Digite a sua segunda  nota = "))
ex=(input("Fez trabalho extra? S/N ")).lower
n1=float(nota1)
n2=float(nota2)
media=float((n1+n2)/2)
if (media >=7) or (ex=="s") :
    print("Voce tirou ",media, "|\o/ Parabêns você passou!")
else:("Sua média foi : ",media,":..( , e você não entregou o trabalho. Você foi reprovado!")
